# app.py

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent
from PIL import Image
from threading import Thread
import asyncio
import json
import random
import time

from data import usuarios, votes, selected_questions, voting_open, debe_correr_cliente_tiktok, cliente_tiktok_conectado, tema_evaluar
from utils import convertir_imagen_a_base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='threading')
cliente_tiktok = TikTokLiveClient("@angelo.gamer")

# Funciones auxiliares
def cargar_preguntas():
    with open('./static/js/questions.json', encoding='utf-8') as file:
        return json.load(file)

questions = cargar_preguntas()

def actualizar_votos(usuario):
    global voting_open
    if not voting_open:
        return

    usuario["comment"] = usuario["comment"] if usuario["comment"] in votes else "otros"
    votes[usuario["comment"]] += 1
    total_valid_votes = sum(vote for option, vote in votes.items() if option != "otros")
    percentages = {option: (votes[option] / total_valid_votes * 100 if total_valid_votes > 0 else 0) for option in votes if option != "otros"}
    
    print("Comentario:",usuario["comment"] )
    print("Votos:",votes[usuario["comment"]])
    print("Total de votos:",total_valid_votes)
    print("%:",percentages)
    
    socketio.emit('vote update', {'userId': usuario["unique_id"], 'voteChoice': usuario["comment"], 'votes': votes, 'percentages': percentages})

def seleccionar_pregunta_aleatoria(tema):
    preguntas_disponibles = [q for q in questions[tema] if q not in selected_questions]
    if not preguntas_disponibles:
        return None, None, None

    pregunta_seleccionada = random.choice(preguntas_disponibles)
    selected_questions.append(pregunta_seleccionada)
    numero_pregunta = len(selected_questions)
    inicio_pregunta = time.time()
    
    for key in votes.keys():
        votes[key] = 0
        
    return pregunta_seleccionada, numero_pregunta, inicio_pregunta

# Eventos y rutas

@socketio.on('submit score')
def manejar_envio_puntuacion(data):
    unique_id = data['unique_id']
    puntaje_adicional = data['puntaje']
    usuario_existente = next((u for u in usuarios if u['unique_id'] == unique_id), None)
    
    print("Id:",unique_id)
    print("Puntaje:",puntaje_adicional)
    print("Existe?:",usuario_existente)
    
    if usuario_existente:
        usuario_existente['puntaje'] += puntaje_adicional

    print("Nuevo Puntaje:",usuario_existente['puntaje'])
    
    socketio.emit('update ranking', {'usuarios': usuarios})
    
@cliente_tiktok.on("comment")
async def manejar_comentario(event: CommentEvent):
    try:
        avatar_data = await event.user.avatar.download()
        avatar_base64 = convertir_imagen_a_base64(avatar_data)

        # Verificar si el usuario ya existe
        usuario_existente = next((u for u in usuarios if u['unique_id'] == event.user.unique_id), None)
        
        if usuario_existente:
            # Si el usuario ya existe, actualizamos su información
            usuario_existente['nickname'] = event.user.nickname
            usuario_existente['avatar'] = avatar_base64
            usuario_existente['comment'] = event.comment.strip()

            # Emitimos una actualización para este usuario
            socketio.emit('user update', usuario_existente)
        else:
            # Si el usuario no existe, lo agregamos a la lista
            usuario = {
                "nickname": event.user.nickname,
                "unique_id": event.user.unique_id,
                "puntaje": 0,
                "avatar": avatar_base64,
                "comment": event.comment.strip()
            }
            usuarios.append(usuario)

        # Llamar a la función que actualiza los votos con la información del usuario
        socketio.start_background_task(actualizar_votos, usuario_existente if usuario_existente else usuario)
        
    except Exception as e:
        print(f"Error handling comment: {e}")


def iniciar_cliente_tiktok():
    try:
        asyncio.set_event_loop(asyncio.new_event_loop())
        print("RUN Cliente TikTok: ")
        cliente_tiktok.run()

    except Exception as e:
        print(f"Error running TikTok client: {e}")


def conectar_cliente_tiktok():
    global cliente_tiktok_conectado
    if not cliente_tiktok_conectado:
        hilo_tiktok = Thread(target=iniciar_cliente_tiktok)
        hilo_tiktok.start()
        cliente_tiktok_conectado = True

def desconectar_cliente_tiktok():
    global cliente_tiktok_conectado
    global cliente_tiktok
    print("STOP Cliente TikTok")
    cliente_tiktok.stop()
    cliente_tiktok_conectado = False

@app.route('/')
def inicio():
    tema = tema_evaluar
    pregunta_seleccionada, numero_pregunta, inicio_pregunta = seleccionar_pregunta_aleatoria(tema)
    total_preguntas = len(questions[tema])
    respuesta_correcta = pregunta_seleccionada['correcta']
    return render_template('index.html', question=pregunta_seleccionada, question_number=numero_pregunta, total_questions=total_preguntas, tema=tema, correcta=respuesta_correcta, usuarios=usuarios, question_start_time=inicio_pregunta)

@app.route('/stop_voting')
def detener_votacion():
    global voting_open
    voting_open = False
    desconectar_cliente_tiktok()
    return "Voting stopped"

@app.route('/get_next_question')
def obtener_siguiente_pregunta():
    conectar_cliente_tiktok()
    tema = tema_evaluar
    pregunta_seleccionada, numero_pregunta, _ = seleccionar_pregunta_aleatoria(tema)

    if pregunta_seleccionada is None:
        return jsonify({"end_of_quiz": True})
    else:
        pregunta_seleccionada['question_number'] = numero_pregunta
        print("Num_pregunta:",numero_pregunta)
        print(jsonify(pregunta_seleccionada))
        return jsonify(pregunta_seleccionada)

if __name__ == '__main__':
    print("Inicio")
    conectar_cliente_tiktok()
    socketio.run(app, debug=True)
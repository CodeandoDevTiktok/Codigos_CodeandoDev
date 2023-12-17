//timerUIHandlers.js

import { showCorrectAnswer, loadNextQuestion } from './questionUIHandlers.js';
import { setVotingEnabled, totalTime, getCurrentTime, setCurrentTime, getRankingTemporal, setShowingRanking, UPDATE_INTERVAL, RANKING_DELAY, NEXT_QUESTION_DELAY } from './config.js';
import { updateRankingUI } from './rankingHandlers.js';
import { socket } from './main.js';

function setupTimer() {
    const timeSpan = document.querySelector('.timer-time');
    initializeTimer(timeSpan); // Reinicia currentTime a totalTime cuando se inicia o se reinicia el temporizador
}

function initializeTimer(timeSpan) {
  setCurrentTime(totalTime);
  timeSpan.textContent = `${getCurrentTime()}s`;
  clearPreviousTimer();
  window.timerInterval = setInterval(() => updateTime(timeSpan), UPDATE_INTERVAL);
}

function clearPreviousTimer() {
  if (window.timerInterval) {
      clearInterval(window.timerInterval);
  }
}


function updateTime(timeSpan) {
    const newTime = getCurrentTime() - 1;
    setCurrentTime(newTime);
    timeSpan.textContent = `${newTime}s`;

    if (newTime <= 0) {
      endTimerActions();
  }
}

async function endTimerActions() {
  clearInterval(timerInterval); // Detener el intervalo cuando el tiempo llegue a 0
  await new Promise(resolve => setTimeout(resolve, 100));
  showCorrectAnswer(); // Mostrar la respuesta correcta
  setVotingEnabled(false); // Asegúrate de desactivar la votación
  console.log("Socket Fin Tiempo: ", socket)

  await new Promise(resolve => setTimeout(resolve, RANKING_DELAY));
  await handleRankingUpdate();
}

function handleRankingUpdate() {
  console.log("Iniciando actualización del ranking");
  const rankingData = getRankingTemporal();
  console.log("Ranking Data : ", rankingData);
  updateRankingUI(rankingData);
  setShowingRanking(true);

  return new Promise(resolve => {
    setTimeout(() => {
        setShowingRanking(false);  
        loadNextQuestion();
        setVotingEnabled(true);
        resolve(); // Resuelve la promesa después de cargar la siguiente pregunta
    }, NEXT_QUESTION_DELAY);
  });
  
}

function handleEndOfQuestion() {
    return new Promise((resolve) => {
      // Esperar a que termine el temporizador o que el usuario envíe una respuesta
      let tiempoRestante = getCurrentTime();
      let intervaloDeChequeo = setInterval(() => {
        if (tiempoRestante <= 0) {
          clearInterval(intervaloDeChequeo);
          resolve();
        }
        tiempoRestante = getCurrentTime();
      }, UPDATE_INTERVAL);
    });
  }

export {
  setupTimer,
  handleEndOfQuestion
};
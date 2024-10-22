//voteUIHandlers.js

import { calculateScore, submitScore } from './scoring.js';
import { getVotingEnabled, getCurrentTime, getCorrectAnswer, setCorrectAnswer, currentQuestionNumber} from './config.js';

setCorrectAnswer(document.querySelector('.question-container').getAttribute('data-correct-answer'));

console.log("Respuesta correcta:",getCorrectAnswer());

function updateUIOnVote(data, socket) {
    
    console.log("Votos habilitado: ",getVotingEnabled())
    
    if (!getVotingEnabled()) return;
    
    try {
        
        let { userId, voteChoice } = data;
        let isCorrect = voteChoice === getCorrectAnswer(); // Necesitas obtener correctAnswer de alguna manera
        let timeTaken = getCurrentTime(); // Suponiendo que tienes una función para obtener el tiempo actual de la pregunta
        let score = calculateScore(timeTaken, isCorrect);

        // Envía el puntaje actualizado al servidor si la respuesta es correcta
        if (isCorrect) {
            submitScore(userId, score, socket);
        }
        
        console.log("Usuario: ",userId);
        //console.log("Eleccion: ",voteChoice);
        //console.log("Correcto?: ",isCorrect);
        //console.log("Tiempo actual: ",timeTaken);
        //console.log("Puntaje: ",score);
        
        //Actualiza votos en el HTML
        updateVoteUI(data);

            
    } catch (error) {
        console.error('Error in vote update:', error);
    }
    
}

function updateVoteUI(data) {
    console.log("Actualiza votos y %")
    Object.keys(data.votes).forEach(function(option) {
        var counter = document.getElementById('vote-counter-' + option);
        if (counter) {
            counter.textContent = 'Votos: ' + data.votes[option] + ' (' + data.percentages[option].toFixed(2) + '%)';
        }
    });
}

export {
    updateUIOnVote
};
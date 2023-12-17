//scoring.js

import { MAX_SCORE, SCORE_DECREMENT } from './config.js';

function calculateScore(timeTaken, isCorrect) {
    console.log("Calcula puntajes");
    
    if (!isCorrect) return 0;
    
    let score = MAX_SCORE - Math.floor(timeTaken / SCORE_DECREMENT) * SCORE_DECREMENT;
    console.log("isCorrect: ",isCorrect);
    console.log("timeTaken: ",timeTaken);
    console.log("score: ",Math.max(score, 0));
    return Math.max(score, 0);
}

function submitScore(userId, score, socket) {
    console.log("Envía puntajes");
    console.log("unique_id : ", userId);
    console.log("puntaje : ", score);
    socket.emit('submit score', { unique_id: userId, puntaje: score });
}

export {
    calculateScore,
    submitScore
};
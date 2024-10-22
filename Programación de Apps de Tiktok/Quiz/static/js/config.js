// config.js

let votingEnabled = true;
let loadingQuestion = false;
let quizEnded = false;
let showingRanking = false;
let totalTimeInSeconds = 10; // Tiempo total en segundos
let currentTime = totalTimeInSeconds;
let rankingTemporal = [];
const SOCKET_URL = 'http://127.0.0.1:5000';
//const SOCKET_URL = 'http://172.16.5.4:5000';
const UPDATE_INTERVAL = 1000; // Intervalo de actualización del temporizador en milisegundos
const RANKING_DELAY = 3000; // Retraso antes de mostrar el ranking
const RANKING_DISPLAY_TIME = 5000; //
const NEXT_QUESTION_DELAY = 5000; // Retraso antes de cargar la siguiente pregunta
const MAX_SCORE = 200;
const SCORE_DECREMENT = 50;
let currentQuestionNumber = 1;
let totalQuestions = 4;
let correctAnswer = null;



function setCorrectAnswer(answer) {
    correctAnswer = answer;
}

function getCorrectAnswer() {
    return correctAnswer; 
}

function getRankingTemporal() {
    return rankingTemporal;
}

function setRankingTemporal(value) {
    rankingTemporal = value;
}

function getCurrentTime() {
    return currentTime;
}

function setCurrentTime(value) {
    currentTime = value;
}

function getVotingEnabled() {
    return votingEnabled;
}

function setVotingEnabled(value) {
    votingEnabled = value;
}

function getLoadingQuestion() {
    return loadingQuestion;
}

function setLoadingQuestion(value) {
    loadingQuestion = value;
}

function setQuizEnded(value) {
    quizEnded = value;
}

function getQuizEnded() {
    return quizEnded;
}

function setShowingRanking(value) {
    showingRanking = value;
}

function getShowingRanking() {
    return showingRanking;
}

export {
    getCorrectAnswer,
    setCorrectAnswer,
    getRankingTemporal,
    setRankingTemporal,
    getCurrentTime,
    setCurrentTime,
    getVotingEnabled,
    setVotingEnabled,
    getLoadingQuestion,
    setLoadingQuestion,
    setQuizEnded,
    getQuizEnded,
    setShowingRanking,
    getShowingRanking,
    currentQuestionNumber,
    totalQuestions,
    SOCKET_URL,
    UPDATE_INTERVAL,
    RANKING_DELAY,
    NEXT_QUESTION_DELAY,
    MAX_SCORE,
    SCORE_DECREMENT,
    RANKING_DISPLAY_TIME,
    totalTimeInSeconds as totalTime
};
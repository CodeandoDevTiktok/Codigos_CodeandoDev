//questionUIHandlers.js

import { setupTimer, handleEndOfQuestion } from './timerUIHandlers.js';
import { setVotingEnabled, setLoadingQuestion, getLoadingQuestion, setQuizEnded, getQuizEnded, getShowingRanking, setCorrectAnswer } from './config.js';

function updateQuizHeader(questionData, totalQuestions) {
    const quizStatus = document.querySelector('.quiz-header .quiz-status');
    quizStatus.innerHTML = `
        <div>
            <h4>Tema</h4>
            <h2>Pregunta ${questionData.question_number}/${totalQuestions}</h2>
        </div>
        <div class="timer">
            <span class="timer-icon">⏱</span>
            <span class="timer-time">10s</span>
        </div>`;
}


function updateAnswers(questionData) {
    console.log("Actualizacion updateAnswers")
    const answersContainer = document.querySelector('.answers-container');
    answersContainer.innerHTML = '';
    questionData.respuestas.forEach((respuesta, index) => {
        const answerDiv = document.createElement('div');
        answerDiv.className = 'answer';
        answerDiv.setAttribute('data-correct', index + 1 === questionData.correcta);
        answerDiv.innerHTML = `
            <span class="letter">${index + 1}</span>
            <span class="text">${respuesta}</span>
            <p class="vote-counter" id="vote-counter-${index + 1}">Votos: 0 (0%)</p>`;
        answersContainer.appendChild(answerDiv);
    });
}


function updateProgressBar(questionNumber, totalQuestions) {
    const progressBar = document.getElementById('progress-bar');
    let progressPercentage = (questionNumber / totalQuestions) * 100;
    progressBar.style.width = `${progressPercentage}%`;
}

function updateQuestionUI(questionData) {
    const appContainer = document.querySelector('.app-container');
    appContainer.setAttribute('data-question-number', questionData.question_number);
    const totalQuestions = appContainer.getAttribute('data-total-questions');
    setCorrectAnswer(questionData.correcta.toString());
    const questionContainer = document.querySelector('.question-container');
    questionContainer.setAttribute('data-correct-answer', questionData.correcta);
    questionContainer.innerHTML = `<p>Pregunta: ${questionData.pregunta}</p>`;

    console.log("totalQuestions", totalQuestions)
    console.log("Numero", questionData.question_number)

    updateAnswers(questionData);
    updateQuizHeader(questionData, totalQuestions);
    updateProgressBar(questionData.question_number, totalQuestions);
    setupTimer(); // Iniciar el temporizador aquí asegura que comienza con cada nueva pregunta
}

async function stopVoting() {
    try {
        console.log("Deteniendo la votación.");
        const response = await fetch('/stop_voting');
        const data = await response.text();
        console.log(data); // Esto debería imprimir "Voting stopped"
    } catch (error) {
        console.error('Error al detener la votación:', error);
    }
}

async function loadNextQuestion() {
    
    if (getLoadingQuestion() || getQuizEnded() || getShowingRanking()) {
        console.log("Una pregunta ya se está cargando, el cuestionario ha terminado, o se está mostrando el ranking. Omitiendo esta llamada.");
        return;
    }
    
    setLoadingQuestion(true);
    console.log("Cargando la siguiente pregunta.");
    try {
        await handleEndOfQuestion();
        const response = await fetch('/get_next_question');
        const data = await response.json();
        if (data.end_of_quiz) {
            console.log("Fin del cuestionario.");
            setQuizEnded(true); // Indicar que el cuestionario ha terminado
            setVotingEnabled(false);
        } else {
            setCorrectAnswer(data.correcta.toString());
            updateQuestionUI(data);
        }
    } catch (error) {
        console.error('Error al cargar la siguiente pregunta:', error);
    } finally {
        setLoadingQuestion(false);
    }

}

function showCorrectAnswer() {
    
    const answers = document.querySelectorAll('.answer');
    console.log("respuesta", answers)
    answers.forEach(answer => {
        console.log("Comparacion", answer.getAttribute('data-correct') === 'true')
        if (answer.getAttribute('data-correct') === 'true') {
            answer.style.backgroundColor = '#53c6ff';
            answer.style.borderColor = '#0066ba';
        }
    });
    
    console.log("Muestra respuesta de la pregunta")
}



export {
    updateQuizHeader,
    updateProgressBar,
    loadNextQuestion,
    showCorrectAnswer,
    updateAnswers
};

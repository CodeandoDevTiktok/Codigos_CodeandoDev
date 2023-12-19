//main.js

import { setupSocketListeners } from './socketListeners.js';
import { updateProgressBar } from './questionUIHandlers.js';
import { setupTimer } from './timerUIHandlers.js';
import {SOCKET_URL, currentQuestionNumber, totalQuestions} from './config.js';

export let socket = io(SOCKET_URL);

document.addEventListener('DOMContentLoaded', () => {
    setupSocketListeners();
    updateProgressBar(currentQuestionNumber, totalQuestions);
    setupTimer();
});
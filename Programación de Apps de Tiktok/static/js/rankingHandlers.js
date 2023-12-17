//rankingHandlers.js

import { loadNextQuestion } from './questionUIHandlers.js';
import { RANKING_DISPLAY_TIME } from './config.js';

function createRankingEntry(data, index) {
    const nickname = truncateString(data.nickname, 20);
    const uniqueId = truncateString(`@${data.unique_id}`, 20);
    return `
        <div class='ranking-entry'>
            <div class='ranking-position'>${index + 1}</div>
            <div class='ranking-photo'><img src='data:image/jpeg;base64,${data.avatar}' alt='Avatar'></div>
            <div class='ranking-info'>
                <div class='ranking-name'>${nickname}</div>
                <div class='ranking-nick'>${uniqueId}</div>
            </div>
            <div class='ranking-exp'>${data.puntaje} exp</div>
        </div>`;
}

function truncateString(string, maxLength) {
    return string.length > maxLength ? string.substring(0, maxLength - 3) + '...' : string;
}

function updateRankingUI(ranking) {
    const rankingContainer = document.getElementById('ranking-container');
    rankingContainer.innerHTML = '';
    document.getElementById('rankingPopup').style.display = 'block';
    
    ranking.sort((a, b) => b.puntaje - a.puntaje);

    let rankingHTML = '';
    ranking.slice(0, 7).forEach((data, index) => {
        rankingHTML += createRankingEntry(data, index);
    });

    rankingContainer.innerHTML = rankingHTML;

    setTimeout(() => {
        document.getElementById('rankingPopup').style.display = 'none';
        loadNextQuestion();
    }, RANKING_DISPLAY_TIME);
}

export {
    updateRankingUI
};
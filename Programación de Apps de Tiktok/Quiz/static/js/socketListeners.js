//socketListeners.js

import { updateUIOnVote } from './voteUIHandlers.js';
import { socket } from './main.js';
import { setRankingTemporal } from './config.js';


export function setupSocketListeners() {
    console.log("Inicio de ejecución Socket");
    socket.on('vote update', data => handleVoteUpdate(data));
    socket.on('update ranking', data => handleUpdateRanking(data));
    

function handleVoteUpdate(data) {
    //console.log("Ejecucion Socket : Actualiza Voto");
    //console.log("Data :", data);
    //console.log("Socket :", socket);
    updateUIOnVote(data, socket);
    
}
}

function handleUpdateRanking(data) {
    //console.log("Ejecucion Socket : Actualiza Ranking");
    //console.log("Data del Ranking :", data);
    setRankingTemporal(data.usuarios);
}

"use strict";
function handleData({ nome, tamanho }) {
    return tamanho;
}
const obj = {
    nome: "Objeto",
    tamanho: 10,
    data: "janeiro",
};
console.log(handleData(obj));

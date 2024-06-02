"use strict";
async function fetchData() {
    const response = await fetch("https://api.origamid.dev/json/vendas.json");
    const json = await response.json();
    handleFetch(json);
}
function handleFetch(data) {
    const p_somaVendas = document.getElementById("somaVendas");
    let soma = 0;
    data.forEach((e) => {
        soma += e[1];
    });
    p_somaVendas.innerText = String(soma);
}
fetchData();

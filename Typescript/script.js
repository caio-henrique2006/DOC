"use strict";
async function fetchProduct() {
    const response = await fetch("https://api.origamid.dev/json/notebook.json");
    const data = await response.json();
    showProduct(data);
}
fetchProduct();
function showProduct(data) {
    document.body.innerHTML = `
    <div>
      <h2>${data.nome}</h2>
        <p>${data.preco}</p>
        <p>${data.garantia}</p>
        <p>${data.descricao}</p>
        <p>${data.seguroAcidente ? "Com seguro acidente" : "Sem seguro acidente"}</p>
      <h3>Empresa Fabricante: </h3>
        <p>${data.empresaFabricante.nome}</p>
        <p>${data.empresaFabricante.fundacao}</p>
        <p>${data.empresaFabricante.pais}</p>
      <h3>Empresa Montadora: </h3>
        <p>${data.empresaMontadora.nome}</p>
        <p>${data.empresaMontadora.fundacao}</p>
        <p>${data.empresaMontadora.pais}</p>
    </div>
  `;
}

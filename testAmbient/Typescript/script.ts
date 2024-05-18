interface Produto {
  nome: string;
}

async function fetchProduto() {
  const response = await fetch("https://api.origamid.dev/json/notebook.json");
  // Retorna o valor como a interface Produto:
  return response.json() as Promise<Produto>;
}

async function fetchP() {
  const result = await fetchProduto();
  console.log(result.nome);
}

fetchP();

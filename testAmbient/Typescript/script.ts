async function fetchData() {
  const response = await fetch("https://api.origamid.dev/json/vendas.json");
  const json = await response.json();
  handleFetch(json);
}

interface propriedades {
  marca: string;
  cor: string;
}

type Vendas = [string, number, string, propriedades];

function handleFetch(data: Vendas[]) {
  const p_somaVendas = <HTMLElement>document.getElementById("somaVendas");
  let soma = 0;
  data.forEach((e) => {
    soma += e[1];
  });
  p_somaVendas.innerText = String(soma);
}

fetchData();

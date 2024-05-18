function handleData({ nome, tamanho }: { nome: string; tamanho: number }) {
  return tamanho;
}

const obj = {
  nome: "Objeto",
  tamanho: 10,
  data: "janeiro",
};

console.log(handleData(obj));

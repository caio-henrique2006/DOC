interface Livro {
  nome: string;
  autor: string;
  preco: string;
}

let chave: keyof Livro;

chave = "preco";

console.log(chave);

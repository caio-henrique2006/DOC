# TypeScript

## Conceitos

### Utilidades do typescript

- Permite que o editor localize erros runtime antes mesmo da execução do código.
- Typescript já instalado por padrão no VS code.

## Comandos

```tsx
npm install -g typescript // Instalar TS globalmente

tsc [nomeDoArquivoJS] // Compilar em TS em JS

tsc --init // Cria o arquivo tsconfig.json

tsc // Compila todos os arquivos TS em JS

tsc -w // Compila a todo novo salvamento TS em JS
```

## tsconfig

```tsx
    {
        "compilerOptions": {
            "target": "ESNext", // Define a versão do JS que será usada
            "strict": true // Define o modo strict no JS e é mais restrito no TS
        }
    }
```

## @ts-check

Comentário no começo do código de um arquivo js que permite o VS code checar erros de TS.

```tsx
//@ts-check
...
```

## Type Annotation

Forma de definir o tipo de um dado em TS.

```tsx
// Váriavel comum (não recomendado, inferência)
const nome: string = "Caio";

// Váriavel com dois tipos:
const idade: number | string = 17;

// Objeto comum (não recomendado, inferência)
const pessoa: {
  nome: string;
  idade: number;
} = {
  nome: "Caio",
  idade: 17,
};

// Parâmetros da função:
function soma(a: number, b: number): number {
  return a + b;
}

function object(objeto: { nome: string; idade: number }) {
  return objeto;
}

// Array:

const numeros = [1, 2, 3, 4, 5, 6];
const numerosTextos = [1, "a", 2, "b"];
const arrayArray = [
  ["a", 1],
  ["b", 2],
];

function numeros(data: number[]); // Alt: Array<number>
function numerosTextos(data: (number | string)[]); // Alt: Array<number | string>
function arrayArray(data: (number | string)[][]);
```

Caso a informação do tipo da váriavel já esteja explícito o TS faz a inferência, ou seja, não é necessário definir o tipo.

## Checar se o valor é null

```tsx
const button = document.querySelector("button");

// Optional chaining
button?.click(); // Checa se button é null
```

## Type guard

```tsx
if (typeof value === "number") {
  // code
}
```

## Type e interface

Forma de guardar em uma variável tipos personalizados;

```tsx
// Variável comum:
type NumberOrString = string | number;
const valor: NumberOrString = 20;

// Object:
interface Pessoa {
  // pode ser type tmb
  nome: string;
  idade: number;
  cpf: string;
  usaOculos?: boolean;
}

// Personalizado:
type Categoria = "profissional" | "estudante" | "professor";
```

## Class

```tsx
class Produto {
  nome: string;
  constructor(nome: string) {
    this.nome = nome;
  }
}

class Livro extends Produto {
  autor: string;
  constructor(nome: string, autor: string) {
    super(nome); // Atributos criados no cronstrutor do extend
    this.autor = autor;
  }
}

const fruta = new Produto("Banana");
```

## Instanceof

Observa se um objeto é uma instância de uma classe específica.

```tsx
class Livro {
  nome: string;
  autor: string;
  constructor(nome: string, autor: string) {
    this.nome = nome;
    this.autor = autor;
  }
}

objeto = new Livro("Atomic Habits", "James Clear");

if (objeto instanceof Livro) {
  console.log("objeto é instância de Livro");
}

// objeto instaceof HTMLElement
```

## This ou event.currentTarget

```tsx

function (this: HTMLButtonElement, event: MouseEvent) {
	console.log(this);
}

// OU

button?.addEventListener("click", handleClick);
```

## Tipos genéricos

Utilizado para declarar o tipo de parâmetro da função.

```tsx
function retorno<Tipo>(param: Tipo): Tipo {
  return param;
}

retorno(200);
retorno("Ola");
retorno(true);

function retLista<T>(param: T[]): T {
  return param[0];
}

retLista([0, 1, 2, 3]);
```

Utilizando extends

```tsx
function element<T extends HTMLElement>(param: T): string {
  return T.innerText;
}

const p = document.getElementById("texto");
element(p);
```

Métodos nativos

```tsx
const link = document.getElementById<HTMLAnchorElement>(".link");
```

## Optional arg

Formas de gerar argumentos|parâmetros opcionais.

```tsx
function soma(a, b, c = 0);

function soma(a: number, b: number, c?: number); // c = number | undefined

function soma(a: number, b: number, c: number = 0); // c = number
```

## Never

Palavra chave para definir que uma função vai retornar um erro, abortando a aplicação.

```tsx
function erro(mensagem: string): never {
  throw new Error(mensagem);
}

erro("Deu erro");
console.log("Continua?");
```

## Overload

```tsx
Utilizado para definir possibilidades: entrada -> retorno

function retorno<T>(param: boolean): boolean;
function retorno<T>(param: string): number;
function retorno<T>(param: number): string;
function retorno<T>(param: T) {
  if (typeof param === "string") {
    return Number(param);
  } else if (typeof param === "number") {
    return String(param);
  } else {
    return !param;
  }
}

retorno("200");
console.log(typeof NaN);
retorno(200);
retorno(20.2);
retorno(true);

```

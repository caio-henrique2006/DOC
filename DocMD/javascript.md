# Javascipt

## LocalStorage

```jsx
localStorage.setItem("total", value);
localStorage.getItem("total");
```

## ${ }

```jsx
`${data.name}`;
```

## EventListener

```tsx
button?.addEventListener("click", handleClick);
```

## document.body.innerHTML

```jsx
function show() {
  document.body.innerHTML = `
		<h1>Título</h1>
	`;
}
```

## Fetch API

```jsx
async function fetch() {
  const response = await fetch("URL");
  const json = await response.json();
  handleFetch(json);
}
```

## ...rest

Define um número infinito de parâmetros.

```jsx
function data(operacao, ...numeros) {
  // numeros = Array
  numeros.forEach((e) => console.log(e));
}
```

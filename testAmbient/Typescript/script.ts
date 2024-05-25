window.onload = onRefresh;

interface userData {
  nome: string;
  email: string;
  cpf: string;
}

interface Window {
  userData: userData;
}

function isUserData(value: unknown): value is userData {
  if (
    value &&
    typeof value === "object" &&
    "name" in value &&
    "email" in value &&
    "cpf" in value
  ) {
    return true;
  } else {
    return false;
  }
}

function onRefresh() {
  const nome = document.getElementById("nome");
  const email = document.getElementById("email");
  const cpf = document.getElementById("cpf");

  const data = localStorage.getItem("userData");
  if (isUserData(data)) {
    if (nome instanceof HTMLInputElement) {
      nome.value = data.nome;
    }
    if (email instanceof HTMLInputElement) {
      email.value = data.email;
    }
    if (cpf instanceof HTMLInputElement) {
      cpf.value = data.cpf;
    }
  }
}

function storage(event: Event) {
  const elemento = event.currentTarget;

  if (elemento instanceof HTMLInputElement) {
    if (elemento.id === "nome") {
      window.userData.nome = elemento.value;
    }
    if (elemento.id === "email") {
      window.userData.email = elemento.value;
    }
    if (elemento.id === "cpf") {
      window.userData.cpf = elemento.value;
    }
    localStorage.setItem("userData", JSON.stringify(window.userData));
  }
}

const nome = document.getElementById("nome");
const email = document.getElementById("email");
const cpf = document.getElementById("cpf");

nome?.addEventListener("keyup", storage);
email?.addEventListener("keyup", storage);
cpf?.addEventListener("keyup", storage);

/*
localStorage.setItem("total", value);
localStorage.getItem("total");
*/

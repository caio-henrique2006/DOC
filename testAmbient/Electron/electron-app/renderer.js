console.log(window.versions.node());
console.log(window.versions.chrome());
console.log(window.versions.electron());

const text = document.getElementById("text");

async function getPingPong() {
  const response = await window.versions.ping();
  console.log("Pong is being pressed");
  text.innerText = response;
}

document.getElementById("btn").addEventListener("click", getPingPong);

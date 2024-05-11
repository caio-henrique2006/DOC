"use strict";
const button = document.querySelector("button");
function handleClick(event) {
    const menu = document.getElementById("nav");
    const button = event.currentTarget;
    if (button instanceof HTMLElement && menu) {
        if (menu.hasAttribute("class")) {
            menu.removeAttribute("class");
            button.setAttribute("aria-expanded", "false");
            button.setAttribute("aria-label", "Abrir menu");
        }
        else {
            menu.setAttribute("class", "active");
            button.setAttribute("aria-expanded", "true");
            button.setAttribute("aria-label", "Fechar Menu");
        }
    }
}
button.addEventListener("click", handleClick);

"use strict";
function retorno(param) {
    if (typeof param === "string") {
        return Number(param);
    }
    else if (typeof param === "number") {
        return String(param);
    }
    else {
        return !param;
    }
}
retorno("200");
console.log(typeof NaN);
retorno(200);
retorno(20.2);
retorno(true);

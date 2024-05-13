"use strict";
function normaliza(param) {
    if (isString(param)) {
        return param.toLowerCase;
    }
    return null;
}
function isString(value) {
    return typeof value === "string";
}

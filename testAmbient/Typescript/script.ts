function normaliza(param: unknown) {
  if (isString(param)) {
    return param.toLowerCase;
  }
  return null;
}

function isString(value: unknown): value is string {
  return typeof value === "string";
}

# Node JS

## Conceitos

### O que é Node JS?

Node JS é um ambiente de execução de código javascript que utiliza do poder da engine V8 fora do navegador google chrome. V8 executes node JS in just-in-time(JIT) compilation.

### O que npm?

É o administrador de pacotes padrão do node JS. Ele serve para administrar as dependências de projetos.

### Enviroment variables

São variáveis colocadas em um arquivo .env para serem carregadas no programa. Em node.js é comum usar a biblioteca "dotenv" para esse tipo de trabalho.
O nome do arquivo deve ser exatamente: ".env" e o script deve iniciar com:

```js
require("dotenv").config();
// OU
require("dotenv").config({ path: "./ini.env" }); // Quando o arquivo não é apenas .env.
```

## Código

### NPM commands:

```bash
# Instala as dependências presentes no package.json
npm install

# Instala package específico
npm install <package-name>
--save-dev # Salva no package.json como uma dev dependencie
--no-save # Não salva no package.json
--save-optional # Salva no package.json como uma optional dev dependencie
--no-optional # Impede a instalação de optional dev dependencies

# Instala a versão específica de um package:
npm install <package-name>@<version>

# Atualiza os packages
npm update
npm update <package-name>

# Executa tasks definidas pelo package.json
npm run <task-name>
```

### dev and prod enviroment:

```js
process.env.NODE_ENV;
// "development"
// "production"
// "Testing"
// "Staging"
```

# Electron

## Conceitos:

### O que é Electron js?

É um framework que permite criar aplicativos desktop com HTML, CSS e JS. Ele incorpora dentro de sua estrutura o Chromium e o Node.js. Permite criar aplicativos desktop cross-platform.

### Como é o modelo de processamento do electron?

Electron utiliza um modelo de multi-processamento parecido com os de navegadores, em que cada aba tem sem próprio processamento. Isso é devido a utilização do chromium na sua estrutura.

### main.js em electron?

main.js é a entrada da aplicação electron (entry point). Ela roda em um ambiente node.js, então pode usar require e utilizar as APIs do node. Ela tem a função primaria de criar e administrar as janelas da aplicação (cada uma tendo o seu próprio processador de renderização) através do módulo BrowserWindow. Como a BrowserWindow é um EventEmitter, ela pode manejar (handle) eventos na janela.

### O que é renderer process in electron?

Toda nova janela recebe um processo de renderização que obedece as regras comuns da web (A entrada é um html, se estiliza com css e javascript é carregado pela tag script). Entretanto o "renderer process" não tem acesso as APIs node e nem as funcionalidades nativas de desktop do electron. Para resolver isso existem os "Preload scripts".

### O que são preload scripts?

Preload scripts executam antes que o conteúdo da web seja carregado no "renderer process" e tem os privilégios de acessar a API no node e as funcionalidades nativas desktop do electron.

### O que a contextBridge?

Mesmo que o renderer e o preload compartilham a mesma interface global Window, devido a contextIsolation (Medida de segurança para que o browser não acesse APIs internas do electron) é necessário usar o módulo contextBridge para passar variáveis entre o preload.js e o renderer.js

### O que é IPC (Inter-Process Communication):

IPC é utilizado para comunicar o processamento do renderer com o main. Ele permite criar aplicações mais complexas que utilizam das ferramentas nativas do electron e das windows.

### App module e apps lifecycle:

Controla o lifecycle do seu app, ele é um event emitter do node.js e vai escutar eventos dentro da sua aplicação electron.

## Código:

### Default package.json:

```json
{
  "name": "my-electron-app",
  "version": "1.0.0",
  "description": "Hello World!",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Jane Doe",
  "license": "MIT",
  "devDependencies": {
    "electron": "23.1.3"
  }
}
```

### main.js basic template code:

```js
const { app, BrowserWindow } = require("electron/main");

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
  });

  win.loadFile("index.html");
};

app.whenReady().then(() => {
  createWindow();

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});
```

### Definindo um preload script para uma janela:

```js
const win = new BrowserWindow({
  webPreferences: {
    preload: "path/to/preload.js",
  },
});
```

### Usando a contextBridge:

```js
// preload.js
const { contextBridge } = require("electron");

contextBridge.exposeInMainWorld("myAPI", {
  desktop: true,
});

// renderer.js
console.log(window.myAPI);
```

### Exposing ipcRenderer on Renderer process:

```js
// preload.js
contextBridge.exposeInMainWorld("myAPI", {
  loadPreferences: () => ipcRenderer.invoke("load-prefs"),
});
```

### Comunicação IPC One-way (Renderer -> Main):

```js
// Main.js
function createWindow() {
  const mainWindow = new BrowserWindow({
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
    },
  });

  ipcMain.on("set-title", (event, title) => {
    const webContents = event.sender;
    const win = BrowserWindow.fromWebContents(webContents);
    win.setTitle(title);
  });
}

// Preload.js
const { contextBridge, ipcRenderer } = require("electron/renderer");

contextBridge.exposeInMainWorld("electronAPI", {
  setTitle: (title) => ipcRenderer.send("set-title", title),
});

// Renderer.js
const setButton = document.getElementById("btn");
const titleInput = document.getElementById("title");
setButton.addEventListener("click", () => {
  const title = titleInput.value;
  window.electronAPI.setTitle(title);
});
```

### Comunicação IPC Two-Way (Renderer -> Main -> Renderer):

```js
// Main.js
async function handleFileOpen() {
  const { canceled, filePaths } = await dialog.showOpenDialog();
  if (!canceled) {
    return filePaths;
  }
}

app.whenReady().then(() => {
  ipcMain.handle("dialog:openFile", handleFileOpen);
  createWindow();
  app.on("activate", function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

// preload.js:
const { contextBridge, ipcRenderer } = require("electron/renderer");

contextBridge.exposeInMainWorld("electronAPI", {
  openFile: () => ipcRenderer.invoke("dialog:openFile"),
});

// Renderer.js:
const btn = document.getElementById("btn");
const filePathElement = document.getElementById("filePath");

btn.addEventListener("click", async () => {
  const filePath = await window.electronAPI.openFile();
  filePathElement.innerText = filePath;
});
```

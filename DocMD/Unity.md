# Unity

## Conceitos

### New Input System (input actions)

É necessário primeiro configurar um arquivo **input action** para definir as opções de input e depois gerar o código c# correspondente pelo inspetor.

Lembre-se que o **input debugger** é necessário para testar com o mouse o sistema de touch:

- window -> Analysis -> Input Debugger -> Options -> Simulate touch from the mouse or pen

## Código:

### console:

```c#
Debug.Log("Text");
```

### Pegar o input do teclado

```c#
Input.GetKeyDown(KeyCode.D)
Input.GetKeyUp(KeyCode.D)
```

### Usando a propriedade transform

```c#
GameObject.transform.Rotate(0, -90, 0, Space.Self);
GameObject.transform.position = new Vector3(0, 4, 0);
```

### Pegar referência do GameObject

```c#
GameObject = GameObject.Find("RotateOrienter");
```

### Força do pulo com altura definida

```c#
// Fórmula de Torriceli
jumpForce = Mathf.Sqrt(jumpHeight * -2 * (Physics.gravity.y * gravityScale));
```

### Criar rotação

```c#
Quaternion rotation = Quaternion.identity;

transform.parent.rotation = Quaternion.Euler(0, Angle, 0);
```

### Instanciar um GameObject

```c#
Instantiate(GameObject, coordinates, rotation);
```

### Get child of a GameObject

```c#
transform.GetChild(index)
```

### Using the new Input System

```c#
// Importando
using UnityEngine.InputSystem;

// Instanciando
private Touch touchControls;

// Iniciando o inputSystem antes de todos os outros processos:
private void Awake() {
    touchControls = new Touch();
}

// Criando uma resposta do sistema de input
private void Start() {
    touchControls.[input_map].[input_action].started += ctx => onAction(ctx);
}

private void onAction (InputAction.CallbackContext context) {
    // can do some actions and get values with context
    Debug.Log(context.ReadValue<float>());
}
```

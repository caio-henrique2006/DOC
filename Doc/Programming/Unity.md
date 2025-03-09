# Unity

## PlayBook:

### Error: Property doesn`t exist:

- Cheque se não há conflito entre os namespaces nos imports, é possível que outro import tenha uma mesma chamada.

## New Input System (input actions)

- links: [https://docs.unity3d.com/Packages/com.unity.inputsystem@1.0/manual/Touch.html], []

When using the new input system you can use either the interactive **input actions**, or you can use the API called **EnhancedTouch**.

> Se tentar usar os dois: **input actions** e **EnhancedTouch** vai ser necessário especificar os caminhos dos objetos, pois os dois tem reservado a palavra Touch. Exemplo: UnityEngine.InputSystem.EnhancedTouch.Touch.

```c#
// Ligar e desatiar a simulação de toque com o mouse:
private void onEnable()
{
    TouchSimulation.Enable();
}

private void onDisable()
{
    TouchSimulation.Disable();
}
```

### EnhancedTouch:

```c#
// importando:
using UnityEngine.InputSystem.EnhancedTouch;

// Ligar e desativar a simulação de toque com o mouse e Executa funcao definida:
private void onEnable() {
    TouchSimulation.Enable();
    Touch.onFingerDown += FingerDown;
}

private void onDisable() {
    TouchSimulation.Disable();
    Touch.onFingerDown -= FingerDown;
}

private void FingerDown(Finger finger) {
    if (OnStartTouch != null) OnStartTouch(finger.screenPosition, Time.time);
}
```

### Input actions:

É necessário primeiro configurar um arquivo **input action** para definir as opções de input e depois gerar o código c# correspondente pelo inspetor.

Lembre-se que o **input debugger** é necessário para testar com o mouse o sistema de touch:

- window -> Analysis -> Input Debugger -> Options -> Simulate touch from the mouse or pen

```c#
// Importando
using UnityEngine.InputSystem;

// Instanciando
private Touch touchControls;

// Iniciando o inputSystem antes de todos os outros processos:
private void Awake() {
    touchControls = new Touch();
}

// Lembre de Enable e Disable o sistema:
private void onEnable()
{
    touchControls.Enable();
}

private void onDisable()
{
    touchControls.Disable();
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

// Lembre de Enable e Disable o sistema:
private void onEnable()
{
    touchControls.Enable();
}

private void onDisable()
{
    touchControls.Disable();
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

```

```

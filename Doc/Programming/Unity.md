# Shortcuts:

- Ctrl + Shift + f // Move Gameobject para a posição da câmera

# PlayBook:

## Error: Property doesn`t exist:

- Cheque se não há conflito entre os namespaces nos imports, é possível que outro import tenha uma mesma chamada.

# New Input System

## Links:

- Written tutorials: https://gamedevbeginner.com/input-in-unity-made-easy-complete-guide-to-the-new-system/

## Concepts:

- **Input Actions Assets**: "Objeto" que armazena um conjunto de Control Schemes, Actions Maps.
- **Control Scheme**: Esquema de controles para dispositivos diferentes (Controle, teclado). Permite diferenciar de onde vem as entradas.
- **Action maps**: Conjunto de Actions que fazem sentido juntos (é arbitrário).
- **Action**: Abstração de alto nível, simplesmente significa a ação que deve ser executada quando algum input acontece. É independente do input. Pode ser pular, correr, interagir, atacar.
- **Binding**: Conexão entre uma ação (action) e um ou mais inputs do sistema. Depende do input.
- **Usages controls**: Usages controls let yourself assign controls that are usually binded to certain inputs on different devices, like the "back" action only is put on the "Circle", "B" and "Escape" on different devices.
- **Middle Step**: There is a middle step before the functions that executes the actions, so that it is possible to change the input of it.

### Enhanced Touch and Input Actions

When using the new input system you can use either the interactive **input actions**, or you can use the API called **EnhancedTouch**.

> Se tentar usar os dois: **input actions** e **EnhancedTouch** vai ser necessário especificar os caminhos dos objetos, pois os dois tem reservado a palavra Touch. Exemplo: UnityEngine.InputSystem.EnhancedTouch.Touch.

### Input actions:

É necessário primeiro configurar um arquivo **input action** para definir as opções de input e depois gerar o código c# correspondente pelo inspetor.

Lembre-se que o **input debugger** é necessário para testar com o mouse o sistema de touch:

- window -> Analysis -> Input Debugger -> Options -> Simulate touch from the mouse or pen

## Snippets:

### Util:

```c#
// Import:
using UnityEngine.InputSystem;
```

### Fast Input Reading:

```c#
Vector2 mousePosition = Mouse.current.position.ReadValue();

if (Keyboard.current.aKey.IsPressed()) {
    Debug.Log("Mouse Position: " + mousePosition);
}

if (Keyboard.current.wKey.IsPressed()) {
    Debug.Log("W key was pressed");
}

if (Gamepad.current.aButton.isPressed) {
    Debug.Log("A button is pressed");
}
```

### Input actions:

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

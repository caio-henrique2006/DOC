# New Input System

## Importante:

- Para fazer a movimentação com WASD com o novo input system, aperte com o botão direito do mouse no binding e escolha: "composite binding". Lembra que a movimentação retorna algo como um Vector2.

- Lembre-se que o **input debugger** é necessário para testar com o mouse o sistema de touch no computador: window -> Analysis -> Input Debugger -> Options -> Simulate touch from the mouse or pen

## Concepts:

- **Input Actions Assets**: "Objeto" que armazena um conjunto de Control Schemes, Actions Maps.
- **Control Scheme**: Esquema de controles para dispositivos diferentes (Controle, teclado). Permite diferenciar de onde vem as entradas.
- **Action maps**: Conjunto de Actions que fazem sentido juntos (é arbitrário).
- **Action**: Abstração de alto nível, simplesmente significa a ação que deve ser executada quando algum input acontece. É independente do input. Pode ser pular, correr, interagir, atacar.
- **Binding**: Conexão entre uma ação (action) e um ou mais inputs do sistema. Depende do input.
- **Composite binding**: Binding para movimentação como WASD.
- **Modifier binding**: Binding para combos de inputs, dois inputs apertados ao mesmo tempo.
- **Usages controls**: Usages controls let yourself assign controls that are usually binded to certain inputs on different devices, like the "back" action only is put on the "Circle", "B" and "Escape" on different devices.
- **Middle Step**: There is a middle step before the functions that executes the actions, so that it is possible to change the input of it.

## Enhanced Touch and Input Actions

When using the new input system you can use either the interactive **input actions**, or you can use the API called **EnhancedTouch**.

> Se tentar usar os dois: **input actions** e **EnhancedTouch** vai ser necessário especificar os caminhos dos objetos, pois os dois tem reservado a palavra Touch. Exemplo: UnityEngine.InputSystem.EnhancedTouch.Touch.

## Component Player Input:

Para facilitar a conexão entre o código e o Input Actions existe o componente Player Input que permite conectar o Input Actions e depois referenciar diretamente pelo código. Para referenciar pelo código c# em **Invoke C Sharp Events**:

```c#
private PlayerInput playerInput;
private InputAction pressAction;
private InputAction positionAction;
private float start_position;
void Awake()
{
    playerInput = GetComponent<PlayerInput>();
    pressAction = playerInput.actions["action_name"];
    positionAction = playerInput.actions["position"];
    positionAction.performed += ctx => {start_position = ctx.ReadValue<float>()};
    // ou
    positionAction.performed += GetStartPosition;
    void GetStartPosition(InputAction.CallbackContext context) {
        start_position = context.ReadValue<float>();
    }
}
```

## Examples:

### Example keyboard code:

```c#
    private PlayerInput playerInput;
    private InputAction jumpAction;
    private InputAction moveAction;
    private void Awake()
    {
        playerInput = GetComponent<PlayerInput>();
        jumpAction = playerInput.actions["Jump"];
        moveAction = playerInput.actions["Move"];
    }
    private void OnEnable()
    {
        jumpAction.Enable();
        moveAction.Enable();
    }
    private void OnDisable()
    {
        jumpAction.Disable();
        moveAction.Disable();
    }
    private void Update()
    {
        Debug.Log(jumpAction.ReadValue<float>());
        Debug.Log(moveAction.ReadValue<Vector3>());
        transform.position += moveAction.ReadValue<Vector3>();
    }
```

### Touch Example:

```c#
    private PlayerInput playerInput;
    private InputAction position;
    private InputAction touch;
    private float last_touch_state;
    private void Awake()
    {
        playerInput = GetComponent<PlayerInput>();
        position = playerInput.actions["position"];
        touch = playerInput.actions["touch"];
    }

    private void OnEnable()
    {
        position.Enable();
        touch.Enable();
    }

    private void OnDisable()
    {
        position.Disable();
        touch.Disable();
    }

    private void Update()
    {
        float touch_state = touch.ReadValue<float>();
        if (touch_state != last_touch_state) {
            Debug.Log(position.ReadValue<UnityEngine.Vector2>());
        }
        last_touch_state = touch_state;
    }
```

### Swipe Example:

```c#
private const float SWIPE_THRESHOLD = 100.0f;
private PlayerInput playerInput;
private InputAction pressAction;
private InputAction positionAction;
private Vector2 start_position;
void Awake()
{
    playerInput = GetComponent<PlayerInput>();
    pressAction = playerInput.actions["press"];
    positionAction = playerInput.actions["position"];
    pressAction.performed += GetTouchStartPosition;
}
void OnEnable()
{
    pressAction.Enable();
    positionAction.Enable();
}
void OnDisable()
{
    pressAction.Disable();
    positionAction.Disable();
}
void GetTouchStartPosition(InputAction.CallbackContext ctx)
{
    if (ctx.ReadValue<float>() == 1.0f)
    {
        start_position = positionAction.ReadValue<Vector2>();
    }
    else
    {
        DetectSwipe(start_position, positionAction.ReadValue<Vector2>());
    }
}
void DetectSwipe(Vector2 start_position, Vector2 end_position)
{
    float move_x = 0;
    float move_y = 0;
    float swipe_x = end_position.x - start_position.x;
    float swipe_y = end_position.y - start_position.y;
    if (Mathf.Abs(swipe_x) > SWIPE_THRESHOLD)
    {
        move_x = Mathf.Clamp(swipe_x, -1, 1);
    }
    if (Mathf.Abs(swipe_y) > SWIPE_THRESHOLD)
    {
        move_y = Mathf.Clamp(swipe_y, -1, 1);
    }
    transform.position += new Vector3(move_x, move_y, 0);
}
```

## Snippets:

### Import:

```c#
// Import:
using UnityEngine.InputSystem;
```

### Debug the Input Action Triggering with C Sharp Events on:

```c#
void Awake()
{
    playerInput = GetComponent<PlayerInput>();
    playerInput.onActionTriggered += PlayerInput_onActionTriggered;
}
void PlayerInput_onActionTriggered(InputAction.CallbackContext context)
{
    Debug.Log(context);
}
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

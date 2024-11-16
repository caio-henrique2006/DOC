# Unity

## Conceitos

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

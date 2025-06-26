# Conceitos:

## Materials:

É um recurso que define como a superfície de um objeto 3D será renderizado. NO Unity ele é aplicado ao Mesh renderer.

### PBRMaps:

São texturas específicas implementadas em materiais PBR (Physically Based Rendering) que controlam a aparência física de um objeto, tentando renderizar visualmente um material com realismo físico.

## Shaders:

São programas que rodam na GPU e determinam como os pixels, vértices ou objetos serão desenhados na tela.

# Shortcuts:

- Ctrl + Shift + f // Move Gameobject para a posição da câmera

# PlayBook:

## Error: Property doesn`t exist:

- Cheque se não há conflito entre os namespaces nos imports, é possível que outro import tenha uma mesma chamada.

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

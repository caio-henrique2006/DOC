# ORM (Object Relational Mapper)

É uma técnica de mapeamento de objetos de programação orientada a objetos em bancos de dados relacionais. Ela nasceu com o intuito de ser uma ponte entre a tecnologia de banco de dados relacional e a orientada a objetos. Uma das motivações é a diferença entre os conceitos das duas tecnologias, prorgamadores não gostarem de ter que escrever código SQL e sua produtividade. Existência diversos frameworks que implementam essa técnica.

```js
// Code in SQL like this:
SELECT "id", "name", "type" FROM "item" AS "item" WHERE "item"."type" = 'veg';

// Whould be transformed in this (Sequelize ORM library for JS):
Item
  .findAll({where: {type: 'veg'}})
  .then(rows => {
    console.log('Veggies:');
    for (let row of rows) {
      console.log(`${row.dataValues.id}t${row.dataValues.name}`);
    }
    sequelize.close();
  });
```

# O que é PostgreeSQL?

PostgreeSQL é um banco de dados relacional muito utilizado e com um grande suporte da comunidade. Sua origem data de 1987.
PostgreeSQL tem features mais versáteis do que outros modelos de banco de dados relacional, podendo armazenar tipos diferentes de dados como JSON, Arrays, Matrizes e outros, além de permitir a criação de próprios tipos. É dito como um banco de dados object-relational porque permite features com objetos.

# O que é um singleton?

Um singleton é um padrão de design que garante apenas que exista uma instância de uma classe. Ele tem resolve dois problemas:

- Garante a existência de apenas uma instância de uma classe.
- Fornece um ponto de acesso global a essa instância.

Muito usado para garantir o controle sobre o acesso de um recurso compartilhado como um arquivo ou um banco de dados. Entretanto viola SRP, precisa de tratamento especial quando necessidade de multi-threading e pode ser dificil de testar.

### Como implementar:

```python
'''
1. Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.
2. Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.
'''
# https://refactoring.guru/design-patterns/singleton/python/example#example-0
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

```

# CORS (Cross-origin Resource Sharing)

https://aws.amazon.com/what-is/cross-origin-resource-sharing/?nc1=h_ls

Nos primórdios da internet era muito comum os casos de CSRF(Cross-Site Request Forgery), em um threat actor mandava uma requisição falsa para outro servidor usando os cookies de credenciais de um usuário. Para corrigir isso todos os browsers adotaram o same-origin, ou seja, toda requisição a um servidor só poderia ser feita se ela tivesse sido feita na mesma origem. Entretanto, same-origin é pouco flexível para utilização de APIs de terceiros, por esse motivo existe o mecanismo CORS (Cross-origin Resource Sharing) que permite um servidor observar se a origem de uma requisição é válida.

### CORS Preflight:

Quando uma requisição a um servidor é considerada "complexa" ou de "risco" o browser manda primeiro uma requisição de confirmação para o servidor, que devolve as seguintes configurações:

- Access-Control-Allow-Methods
- Access-Control-Allow-Headers
- Access-Control-Allow-Origin

Essas configurações indicam os métodos (GET, POST, DELETE), Headers (Content-type, Authorization) e Origem (www.new.com) permitidos pelo servidor. Caso a requisição não obedeça essas configurações ela gera um erro.

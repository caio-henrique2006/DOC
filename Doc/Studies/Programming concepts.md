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

Iai man, fiquei sabendo que vc saiu da Smart.

Fico triste, pq desde que eu entre lá você foi o cara que eu mais me senti apoiado e confortável, vou sentir sua falta man, dos papo de jogo e das zoeira. Mas vida que segue, força.

O discord vai tá sempre aberto se tu quiser mandar um papo e jogar, e qualquer coisa de programação até fazer um projeto nós dois só falar.
```

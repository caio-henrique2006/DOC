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

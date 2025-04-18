# Notas

- SQL é uma linguagem de programação declarativa de domínio específico.
- **Never** build a query string by concatenating your query arguments directly into your query strings, beacause of SQL Injection.
- SQL can be used to accelerate "business logic" having the SQL query handles parts of it, instead of making simple queries that need to be repeated.

### Transaction, Atomic, Consistent, Isolated, Durable

Atomic means a transaction is really specific, affects little. Isolated permits that a database has online backups. Consistent means it doesnt change with time and durable means that whatever happens the database will be intact.

### SQL standard 4 isolation levels

The 4 isolation levels are a series of phenomenous when doing a transaction that can or cant happen in every isolation level. They define if its possible to read uncommited transactions, re-read data that had been modified and others. The default for PostgreeSQL is "read commited" which means it reads other transactions changes after they are commited.

### Stored procedures

Stored procedures are server-side functions on the server of PostgreSQL that can store queries to be reused in code.

### Database dump

Um backup de um banco de dados

### Join Statements in SQL

(INNER) JOIN: Returns records that have matching values in both tables
LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table
![join statement](../../img/join%20statement.png)

### Database Indexing

Indexing is a data modeling strategy to sort with pointer the rows of a table so it can be faster to find certain data inside it. Like sorting alphabetically. Cluster index are those that come from automatic by the primary keys and unique constraints. Non-Cluster are the ones defined by us. In postgreSQL is possible to define the algorithm that will be used in the index.

### Amdahl`s law

# Code

### Import and Export DB PostgreSQL

```bash
psql -U user_name -d db_name -f "file_absolute_path"
```

### PostgreSQL indexing

```SQL
-- When a database is created a clustered index is created on the primary key. Any other index you create is called a Non-clustered index.
-- When new data is put inside the DB the index takes time to update, so usually indexes are more usuable in rare changing tables.
-- Create index
CREATE INDEX friends_name_asc ON friends(name ASC);
-- Test the velocity of the query (analyze, verbose, buffers)
EXPLAIN ANALYZE SELECT * FROM friends WHERE name = 'Blake';
-- Delete index
DROP INDEX friends_name_asc;
```

### PostgreeSQL psql commands

```bash
\l # Lista todos os bancos de dados
\c database_name; # Conecta um banco de dados
\dt # Lista as tabelas do banco de dados
\d # Observa o esquema de uma tabela
\set ECHO_HIDDEN true # Mostra as Query SQL escondidas nos comandos.
```

### Examples

```SQL
-- Join
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;
LEFT JOIN album USING(artistid);
```

### Util

```SQL
coalesce(element, 0) -- Retorna o primeiro argumento que não seja NULL.
cast(element as date) -- Transforma o element no tipo dito como "as".

-- PostgreSQL Only:

```

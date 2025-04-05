# Notas

- SQL é uma linguagem de programação declarativa de domínio específico.
- **Never** build a query string by concatenating your query arguments directly into your query strings, beacause of SQL Injection.
- SQL can be used to accelerate "business logic" having the SQL query handles parts of it, instead of making simple queries that need to be repeated.

# Conceitos

### SQL Injection

SQL Injection is a security breach where a query sintax in SQL is mistakingly not considered a dinamic argument and executes even though it should not.

### Transaction, Atomic, Consistent, Isolated, Durable

Atomic means a transaction is really specific, affects little. Isolated permits that a database has online backups. Consistent means it doesnt change with time and durable means that whatever happens the database will be intact.

### SQL standard 4 isolation levels

The 4 isolation levels are a series of phenomenous when doing a transaction that can or cant happen in every isolation level. They define if its possible to read uncommited transactions, re-read data that had been modified and others. The default for PostgreeSQL is "read commited" which means it reads other transactions changes after they are commited.

# Code

### Util

```SQL
coalesce(element, 0) -- Retorna o primeiro argumento que não seja NULL.
cast(element as date) -- Transforma o element no tipo dito como "as".

-- PostgreSQL Only:

```

# Notas

- SQL é uma linguagem de programação declarativa de domínio específico.
- **Never** build a query string by concatenating your query arguments directly into your query strings, beacause of SQL Injection.

# Conceitos

### SQL Injection

SQL Injection is a security breach where a query sintax in SQL is mistakingly not considered a dinamic argument and executes even though it should not.

### Transaction, Atomic, Consistent, Isolated, Durable

Atomic means a transaction is really specific, affects little. Isolated permits that a database has online backups. Consistent means it doesnt change with time and durable means that whatever happens the database will be intact.

# Code

### Util

```SQL
coalesce(element, 0) -- Retorna o primeiro argumento que não seja NULL.
cast(element as date) -- Transforma o element no tipo dito como "as".

-- PostgreSQL Only:

```

# Notas

- SQL é uma linguagem de programação declarativa de domínio específico.
- **Never** build a query string by concatenating your query arguments directly into your query strings, beacause of SQL Injection.
- SQL can be used to accelerate "business logic" having the SQL query handles parts of it, instead of making simple queries that need to be repeated.
- Always put SQL code inside an .sql file.

## Transaction, Atomic, Consistent, Isolated, Durable

Atomic means a transaction is really specific, affects little. Isolated permits that a database has online backups. Consistent means it doesnt change with time and durable means that whatever happens the database will be intact.

## SQL standard 4 isolation levels

The 4 isolation levels are a series of phenomenous when doing a transaction that can or cant happen in every isolation level. They define if its possible to read uncommited transactions, re-read data that had been modified and others. The default for PostgreeSQL is "read commited" which means it reads other transactions changes after they are commited.

## Stored procedures

Stored procedures are server-side functions on the server of PostgreSQL that can store queries to be reused in code.

## Database dump

Um backup de um banco de dados

## Join Statements in SQL

(INNER) JOIN: Returns records that have matching values in both tables
LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table
![join statement](../../img/join%20statement.png)

## Database Indexing

Indexing is a data modeling strategy to sort with pointer the rows of a table so it can be faster to find certain data inside it. Like sorting alphabetically. Cluster index are those that come from automatic by the primary keys and unique constraints. Non-Cluster are the ones defined by us. In postgreSQL is possible to define the algorithm that will be used in the index.

## Amdahl`s law

## Areas of SQL

DML - Data Manipulation Language: Insert, Update and Delete.
DDL - Data Definition Language: Create, Alter and Drop.
TCL - Transaction Control Language: Begin, Commit, Transaction commands.
DCL - Data Control Language: Grant and Revoke.
Query - Select, table, values and with.

# Code

## Import and Export DB PostgreSQL

```bash
psql -U user_name -d db_name -f "file_absolute_path"
```

## Pagination

```SQL
-- offset is inneficient in big tables, so its better to use keyset even though you need to remember the last row.
-- offset
SELECT *
FROM your_table
ORDER BY id
LIMIT 20 OFFSET 40; -- jumps the 40 first rows, but skips going through then which make it slow

-- keyset
SELECT *
FROM your_table
WHERE id > 50  -- key set part
ORDER BY id
LIMIT 10;
```

## PostgreSQL indexing

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

## PostgreeSQL psql commands

```bash
\l # Lista todos os bancos de dados
\c database_name; # Conecta um banco de dados
\dt # Lista as tabelas do banco de dados
\d # Observa o esquema de uma tabela
\set ECHO_HIDDEN true # Mostra as Query SQL escondidas nos comandos.
```

## Examples

```SQL
-- Join
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;
LEFT JOIN album USING(artistid);
-- Limit
select * from races limit 1;
-- as
select quantity as coins from pigbank;
-- in, not in, not exist
select title, count(*) from track join album using (album_id) where title in ('Balls to the Wall', 'Restless and Wild') group by title;
-- order by
order by name asc, number desc, ... -- order by can take multiple orders.
-- case when then else end
order by
        case when left(name, 1) in ('A', 'E', 'I', 'O', 'U') -- Um if else
                then 1
                else 2
        end
-- with
with decades as -- Creates a "variable"
(
   select extract('year' from date_trunc('decade', date)) as decade
     from races
 group by decade
)
select name, ... from decades
-- Lateral join
...
FROM
  users
LEFT JOIN LATERAL ( -- Lateral means that the subquery can use rows from the left table.
  SELECT item
  FROM orders
  WHERE orders.user_id = users.id
  LIMIT 1
) ord ON true;
-- Row
WHERE ROW(first_name, last_name) = ROW('John', 'Doe'); -- Comparing various variables at the same time.
```

## Util

```SQL
-- coalesce
coalesce(element, 0) -- Retorna o primeiro argumento que não seja NULL.
-- cast
cast(element as date) -- Transforma o element no tipo dito como "as".
-- extract
extract(element from date) -- Extrai dados de data (normalmente utilizado com datas).
SELECT EXTRACT(YEAR FROM DATE '2024-04-24') AS year;
-- generate_series
generate_series(date '2000-01-01',
                date '2010-01-01',
                interval '1 year')
as t(date);
SELECT * FROM generate_series(1, 5) AS num; -- Gera uma sequência.
select num, num+3 as soma from generate_series(1, 5) as num;
```

## Util PostgreeSQL only

```SQL
-- explain
EXPLAIN SELECT ... -- Explain before any query will show the postgreSQL plan
explain (costs off, buffers, analyze) select ...
-- point, <->
order by point(lng, lat) <-> point(2.349014, 48.864716) -- <-> operator for getting the distance between then
-- point is a datastructure in PostgreeSQL.
```

## Others

```SQL
select date::date,
    extract('isodow' from date) as dow,
    to_char(date, 'dy') as day,
    extract('isoyear' from date) as "iso year",
    extract('week' from date) as week,
    extract('day' from
            (date + interval '2 month - 1 day')
            )
    as feb,
    extract('year' from date) as year,
    extract('day' from
            (date + interval '2 month - 1 day')
            ) = 29
    as leap
from generate_series(date '2000-01-01',
                    date '2010-01-01',
                    interval '1 year')
    as t(date);
```

select
name, composer
from
track
order by
name desc
limit 20;

# Week05
## Task 1: Install MySQL server
## Task 2: Create database and table in your MySQL server
- Create a new database named website
- - ```MySQL
    mysql> CREATE DATABASE website;
    mysql> SHOW DATABASES;
    mysql> USE website;
    ```
- Create a new table named member, in the website database, designed as below:
- - ```MySQL
    mysql> CREATE TABLE member(
        -> `Column Name` VARCHAR(255),
        -> `Data Type` VARCHAR(255),
        -> `Additional Settings` VARCHAR(255),
        -> `Description` VARCHAR(255)
        -> );
    mysql> SHOW TABLES;
    mysql> INSERT INTO member(`Column Name`,`Data Type`, `Additional Settings`, `Description`)VALUES -> ('id', 'bright', 'primary key, auto increment', 'Unique ID');
    Query OK, 1 row affected (0.00 sec)

    mysql> INSERT INTO member(`Column Name`,`Data Type`, `Additional Settings`, `Description`)VALUES -> ('name', 'varchar(255)', 'not null', 'Name');
    Query OK, 1 row affected (0.00 sec)

    mysql> INSERT INTO member(`Column Name`,`Data Type`, `Additional Settings`, `Description`)VALUES -> ('username', 'varchar(255)', 'not null', 'Username');
    Query OK, 1 row affected (0.00 sec)

    mysql> INSERT INTO member(`Column Name`,`Data Type`, `Additional Settings`, `Description`)VALUES ('password', 'varchar(255)', 'not null', 'Password');
    Query OK, 1 row affected (0.00 sec)

    mysql> INSERT INTO member(`Column Name`,`Data Type`, `Additional Settings`, `Description`)VALUES ('follower_count', 'int unsigned', 'not null, default to 0', 'Follower Count');
    Query OK, 1 row affected (0.00 sec)

    mysql> INSERT INTO member(`Column Name`,`Data Type`, `Additional Settings`, `Description`)VALUES ('time', 'datetime', 'not null, default to current time', 'Signup Time');
    Query OK, 1 row affected (0.00 sec)
    ```
- Screenshot: ![task02](/week5/source/screenshot-task02.png)


# Week05
## Task 1: Install MySQL server


## Task 2: Create database and table in your MySQL server
- Create a new database named website
- - ```MySQL
    mysql> CREATE DATABASE website;
    mysql> SHOW DATABASES;
    mysql> USE website;
    ```
- Create a new table named member, in the website database, designed as below.
- - ```MySQL
    mysql> CREATE TABLE member(
        -> id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
        -> name VARCHAR(255) NOT NULL COMMENT 'Name',
        -> username VARCHAR(255) NOT NULL COMMENT 'Username',
        -> password VARCHAR(255) NOT NULL COMMENT 'Password',
        -> follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',
        -> time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time');
    ```
- Screenshot: ![task02](/week5/source/screenshot-task02.png)


## Task 3: SQL CRUD
- INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
- - ```MySQL

    ```
- SELECT all rows from the member table.
- - ```MySQL

    ```
- SELECT all rows from the member table, in descending order of time.
- - ```MySQL

    ```
- SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
- - ```MySQL

    ```
- SELECT rows where username equals to test.
- - ```MySQL

    ```
- SELECT rows where name includes the es keyword.
- - ```MySQL

    ```
- SELECT rows where both username and password equal to test.
- - ```MySQL

    ```
- UPDATE data in name column to test2 where username equals to test.
- - ```MySQL

    ```


## Task 4: SQL Aggregation Functions
- SELECT how many rows from the member table.
- - ```MySQL

    ```
- SELECT the sum of follower_count of all the rows from the member table.
- - ```MySQL

    ```
- SELECT the average of follower_count of all the rows from the member table.
- - ```MySQL

    ```
- SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
- - ```MySQL

    ```

## Task 5: SQL JOIN
- Create a new table named message, in the website database.
- - ```MySQL

    ```
- SELECT all messages, including sender names. We have to JOIN the member table to get that.
- - ```MySQL

    ```
- SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
- - ```MySQL

    ```
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
- - ```MySQL

    ```
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
- - ```MySQL

    ```
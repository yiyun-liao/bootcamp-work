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
    - ```MySQL
    mysql> INSET INTO member(name, username, password) VALUES('test', 'test', 'test');
    mysql> INSERT INTO member(name, username, password, follower_count) VALUES
        ->  ('Yun', 'Yun4356', '12345678', 8),
        ->  ('Yi', 'Yi9878', '87654321', 12),
        ->  ('Cindy', 'Lin9934', '21212121', 24),
        ->  ('An', 'wang984984', '98989898', 40);
    ```
- SELECT all rows from the member table.
    - ```MySQL
    mysql> SELECT * FROM member;
    ```
    - Screenshot: ![task03-1](/week5/source/screenshot-task03-1.png)
- SELECT all rows from the member table, in descending order of time.
    - ```MySQL
    # 因為資料同一時間創建，導致 time 一樣，所以增加更改資料即更新時間
    mysql> ALTER TABLE member MODIFY time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
    mysql> UPDATE member SET username = 'YI8778' WHERE name='Yi';
    mysql> UPDATE member SET password = '48573953' WHERE id='2';
    mysql> UPDATE member SET follower_count = '36' WHERE id='5';
    # 本題實際需求
    mysql> SELECT * FROM member ORDER BY time DESC;
    ```
    - Screenshot: ![task03-2](/week5/source/screenshot-task03-2.png)
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
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
    mysql> INSET INTO member(name, username, password) VALUES('test', 'test', 'test');
    mysql> INSERT INTO member(name, username, password, follower_count) VALUES
        ->  ('Yun', 'Yun4356', '12345678', 8),
        ->  ('Yi', 'Yi9878', '87654321', 12),
        ->  ('Cindy', 'Lin9934', '21212121', 24),
        ->  ('An', 'wang984984', '98989898', 40);
    ```
- SELECT all rows from the member table.
- - ```MySQL
    mysql> SELECT * FROM member;
    ```
- - Screenshot: ![task03-1](/week5/source/screenshot-task03-1.png)
- SELECT all rows from the member table, in descending order of time.
- - ```MySQL
    # 因為資料同一時間創建，導致 time 一樣，所以增加更改資料即更新時間
    mysql> ALTER TABLE member MODIFY time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
    mysql> UPDATE member SET username = 'YI8778' WHERE name='Yi';
    mysql> UPDATE member SET password = '48573953' WHERE id='2';
    mysql> UPDATE member SET follower_count = '36' WHERE id='5';
    # 本題需求
    mysql> SELECT * FROM member ORDER BY time DESC;
    ```
- - Screenshot: ![task03-2](/week5/source/screenshot-task03-2.png)
- SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
- - ```MySQL
    # 因為 2~4 筆排序剛好跟 id 2~4 一樣，所以再次更新資料
    mysql> UPDATE member SET password=3849583 WHERE id=4;
    # 本題需求
    mysql> SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
    ```
- - Screenshot: ![task03-3](/week5/source/screenshot-task03-3.png)
- SELECT rows where username equals to test.
- - ```MySQL
    mysql> SELECT * FROM member WHERE username='test';
    ```
- - Screenshot: ![task03-4](/week5/source/screenshot-task03-4.png)
- SELECT rows where name includes the es keyword.
- - ```MySQL
    mysql> SELECT * FROM member WHERE name LIKE '%es%';
    ```
- - Screenshot: ![task03-5](/week5/source/screenshot-task03-5.png)
- SELECT rows where both username and password equal to test.
- - ```MySQL
    mysql> SELECT * FROM member WHERE username='test' AND password='test';
    ```
- - Screenshot: ![task03-6](/week5/source/screenshot-task03-6.png)
- UPDATE data in name column to test2 where username equals to test.
- - ```MySQL
    mysql> UPDATE member SET name='test2' WHERE username='test';
    ```
- - Screenshot: ![task03-7](/week5/source/screenshot-task03-7.png)


## Task 4: SQL Aggregation Functions
- SELECT how many rows from the member table.
- - ```MySQL
    mysql> SELECT count(*) FROM member; 
    ```
- - Screenshot: ![task04-1](/week5/source/screenshot-task04-1.png)
- SELECT the sum of follower_count of all the rows from the member table.
- - ```MySQL
    mysql> SELECT sum(follower_count) FROM member;
    ```
- - Screenshot: ![task04-2](/week5/source/screenshot-task04-2.png)
- SELECT the average of follower_count of all the rows from the member table.
- - ```MySQL
    mysql> SELECT avg(follower_count) FROM member;
    ```
- - Screenshot: ![task04-3](/week5/source/screenshot-task04-3.png)
- SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
- - ```MySQL
    mysql> SELECT avg(follower_count) FROM (
        -> SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS first_two_avg;
    ```
- - Screenshot: ![task04-4](/week5/source/screenshot-task04-4.png)

## Task 5: SQL JOIN
- Create a new table named message, in the website database.
- - ```MySQL
    mysql> CREATE TABLE message(
        -> id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
        -> member_id BIGINT NOT NULL COMMENT 'Member ID for Message Sender',
        -> FOREIGN KEY (member_id) REFERENCES member(id),
        -> content VARCHAR(255) NOT NULL COMMENT 'Content',
        -> time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
    # 調整 time comment
    mysql> ALTER TABLE message 
        -> MODIFY COLUMN time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Publish Time';
    # 補上 like_count
    mysql> ALTER TABLE message
        -> ADD COLUMN like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Like Count' AFTER content;
    mysql> SHOW FULL COLUMNS FROM message;
    ```
- - Screenshot: ![task05-1](/week5/source/screenshot-task05-1.png)
- - Screenshot: ![task05-2](/week5/source/screenshot-task05-2.png)
- SELECT all messages, including sender names. We have to JOIN the member table to get that.
- - ```MySQL
    # 增加 message 資料
    mysql> INSERT INTO message (member_id, content, like_count)VALUES(5,'How to make the cake in 30 mins', 246);
    mysql> INSERT INTO message (member_id, content, like_count)VALUES(1,'How to make a delicious homemade pasta from scratch',120);
    mysql> INSERT INTO message (member_id, content, like_count)VALUES(4,'The secret to perfecting the art of French pastry baking', 375);
    mysql> INSERT INTO message (member_id, content, like_count)VALUES(2,'Exploring the vibrant flavors of Thai street food', 429);
    mysql> INSERT INTO message (member_id, content, like_count)VALUES(2,'Step-by-step guide to making the perfect sushi rolls', 346);
    mysql> INSERT INTO message (member_id, content, like_count)VALUES(3,'A beginner''s guide to Mediterranean cuisine: Must-try dishes', 56);
    mysql> INSERT INTO message (member_id, content, like_count)VALUES(1,'The best techniques for grilling steak to perfection', 48);
    mysql> INSERT INTO message (member_id, content, like_count)VALUES(5,'How to make authentic Mexican tacos with homemade tortillas', 293);
    mysql> INSERT INTO message (member_id, content, like_count)VALUES(4,'Top 5 vegan recipes that everyone will love', 112);
    mysql> INSERT INTO message (member_id, content, like_count)VALUES(1,'Mastering the art of Indian curry with spices and herbs', 392);
    # 本題需求
    mysql> SELECT message.id, member.name AS sender_name, message.content, message.like_count, message.time FROM member INNER JOIN message on message.member_id=member.id;
    ```
- - Screenshot: ![task05-3](/week5/source/screenshot-task05-3.png)
- SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
- - ```MySQL
    mysql> SELECT message.id, member.name AS sender_name, message.content, message.like_count, message.time
        -> FROM member INNER JOIN message on message.member_id=member.id
        -> WHERE member.username='test';
    ```
- - Screenshot: ![task05-4](/week5/source/screenshot-task05-4.png)
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
- - ```MySQL
    mysql> SELECT AVG(message.like_count) FROM member INNER JOIN message ON message.member_id=member.id where member.username='test';
    ```
- - Screenshot: ![task05-5](/week5/source/screenshot-task05-5.png)
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
- - ```MySQL
    mysql> SELECT member.username, AVG(message.like_count) FROM member INNER JOIN message ON message.member_id=member.id GROUP BY member.username;
    ```
- - Screenshot: ![task05-6](/week5/source/screenshot-task05-6.png)
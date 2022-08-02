CREATE DATABASE test;
DROP TABLE IF EXISTS employee_comments;
CREATE TABLE employee_comments(comment_id integer not null primary key auto_increment,employee_id integer,employee_comments varchar(2000));

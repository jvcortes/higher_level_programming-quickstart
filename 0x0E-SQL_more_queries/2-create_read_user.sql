-- Creates a new user called 'user_0d_2'
-- The user will contain SELECT privileges on the database 'hbtn_0d_2'
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';

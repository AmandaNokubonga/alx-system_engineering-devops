-- Script that creates the MySQL server user holberton_user
CREATE USER
       IF NOT EXISTS 'holberton_user'@'localhost'
       IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT
      ON . TO 'holberton_user'@'localhost';
-- GRANT CREATE
--      ON . TO 'holberton_user'@'localhost';
-- GRANT INSERT
--      ON . TO 'holberton_user'@'localhost';
GRANT SELECT
      ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

GRANT SELECT
      ON mysql.user TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;

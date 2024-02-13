cript that creates the MySQL server user replica_user
CREATE USER
       IF NOT EXISTS 'replica_user'@'%'
       IDENTIFIED BY 'replica_user_pwd';

GRANT REPLICATION SLAVE
      ON .
      TO 'replica_user'@'%';
FLUSH PRIVILEGES;

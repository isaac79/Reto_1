CREATE DATABASE IF NOT EXISTS R_SQL;
USE R_SQL;

DROP TABLE IF EXISTS tweets;
CREATE TABLE IF NOT EXISTS tweets (
	id BIGINT,
    texto VARCHAR(1000),
    usuario CHAR(36),
    hashtags JSON,
    fecha DATETIME,
    retweets INT,
    favoritos INT);
    
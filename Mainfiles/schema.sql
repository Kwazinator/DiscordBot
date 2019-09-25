DROP TABLE IF EXISTS poll;
DROP TABLE IF EXISTS user;


CREATE TABLE user (
    userid TEXT PRIMARY KEY
);

CREATE TABLE poll (
    pollid TEXT PRIMARY KEY,
    message TEXT,
    creator TEXT
);

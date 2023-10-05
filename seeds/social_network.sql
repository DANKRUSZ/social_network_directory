
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;

--Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email_address text,
    username text
);
INSERT INTO accounts (email_address, username) VALUES ('dan@email.com', 'dan');
INSERT INTO accounts (email_address, username) VALUES ('harry@email.com', 'harry');

DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    account_id int
);

--Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, content, views, account_id) VALUES ('My Title 1', 'Content 1', 0, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('My Title 2', 'Content 2', 0, 2);



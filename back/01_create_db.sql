CREATE SCHEMA SESSION;

CREATE TABLE SESSION.USERS (
    user_id SERIAL,
    user_email TEXT NOT NULL UNIQUE,
    user_name TEXT NOT NULL,
    -- user_birth_date TIMESTAMP NOT NULL,
    user_password TEXT,
    user_salt TEXT,
    user_ext_con_type TEXT,
    user_ext_con_id TEXT,
    PRIMARY KEY (user_id)
);
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role INTEGER,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS collections (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    name TEXT,
    visible INTEGER,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS badges (
    id SERIAL PRIMARY KEY,
    collection_id INTEGER REFERENCES collections,
    amount INTEGER,
    price numeric(7,4),
    name TEXT,
    designer TEXT,
    supplier TEXT,
    created_at TIMESTAMP
);
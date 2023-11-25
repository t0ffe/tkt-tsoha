CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role INTEGER,
    created_at TIMESTAMP,
    student_organization INTEGER,
    FOREIGN KEY (student_organization) REFERENCES student_organization(id)

);

CREATE TABLE IF NOT EXISTS student_organization (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS badges (
    id SERIAL PRIMARY KEY,
    amount INTEGER,
    price numeric(7,4),
    name TEXT,
    designer TEXT,
    supplier TEXT,
    created_at TIMESTAMP,
    student_organization INTEGER,
    FOREIGN KEY (student_organization) REFERENCES student_organization(id)
);
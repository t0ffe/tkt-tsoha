CREATE TABLE roles (
    role_id INTEGER PRIMARY KEY,
    role_name TEXT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (role) REFERENCES roles(role_id)
);

CREATE TABLE student_organization (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE user_organizations (
    user_id INTEGER,
    organization_id INTEGER,
    PRIMARY KEY (user_id, organization_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (organization_id) REFERENCES student_organization(id)
);

CREATE TABLE badge_designers (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE badge_supplier (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE badges (
    id SERIAL PRIMARY KEY,
    student_organization INTEGER,
    amount INTEGER,
    price numeric(7,4),
    name TEXT,
    designer_id INTEGER,
    supplier_id INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (student_organization) REFERENCES student_organization(id),
    FOREIGN KEY (designer_id) REFERENCES badge_designers(id),
    FOREIGN KEY (supplier_id) REFERENCES badge_supplier(id)
);

INSERT INTO roles (role_id, role_name) VALUES ('1' ,'Myyjä');
INSERT INTO roles (role_id, role_name) VALUES ('2' ,'Asiakas');
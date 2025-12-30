CREATE DATABASE IF NOT EXISTS dating_app;
USE dating_app;

CREATE TABLE users_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    last_login DATETIME NULL,
    is_superuser TINYINT(1) DEFAULT 0,
    username VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    gender VARCHAR(10),
    age INT,
    latitude DOUBLE,
    longitude DOUBLE,
    is_staff TINYINT(1) DEFAULT 0,
    is_active TINYINT(1) DEFAULT 1,
    date_joined DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chat_message (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_id INT,
    receiver_id INT,
    message TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES users_user(id),
    FOREIGN KEY (receiver_id) REFERENCES users_user(id)
);

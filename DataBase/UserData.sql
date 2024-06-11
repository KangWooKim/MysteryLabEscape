CREATE DATABASE mygame;
USE mygame;

CREATE TABLE players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    nickname VARCHAR(255),
    avatar_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE game_progress (
    player_id INT,
    current_floor INT,
    puzzle_state TEXT,
    items TEXT,
    quest_state TEXT,
    FOREIGN KEY (player_id) REFERENCES players(id)
);

CREATE TABLE player_stats (
    player_id INT,
    play_time INT,
    successes INT,
    failures INT,
    best_time INT,
    score INT,
    level INT,
    FOREIGN KEY (player_id) REFERENCES players(id)
);

CREATE TABLE social (
    player_id INT,
    friends_list TEXT,
    messages TEXT,
    team_history TEXT,
    FOREIGN KEY (player_id) REFERENCES players(id)
);

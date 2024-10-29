-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;

CREATE TABLE IF NOT EXISTS tv_shows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS tv_show_genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    show_id INT,
    genre_id INT,
    FOREIGN KEY (show_id) REFERENCES tv_shows(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

SELECT genres.name, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.id, genres.name
ORDER BY genres.name ASC;
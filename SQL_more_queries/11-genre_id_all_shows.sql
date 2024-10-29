-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;

CREATE TABLE IF NOT EXISTS tv_shows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS tv_show_genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    show_id INT,
    genre_id INT,
    FOREIGN KEY (show_id) REFERENCES tv_shows(id)
);

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_shows.title, tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
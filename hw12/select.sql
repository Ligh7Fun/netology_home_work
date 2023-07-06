-- Задание 2
-- Название и продолжительность самого длительного трека.
SELECT name, duration "max duration track"
FROM tracks
WHERE duration = (SELECT max(duration) FROM tracks);

-- Название треков, продолжительность которых не менее 3,5 минут.
SELECT name
FROM tracks
WHERE duration > 210;

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT name
FROM collections
WHERE release BETWEEN 2018 AND 2020;


-- Исполнители, чьё имя состоит из одного слова.
SELECT name
FROM artists
WHERE name NOT LIKE '% %';

-- Название треков, которые содержат слово «мой» или «my».
SELECT name
FROM tracks
WHERE LOWER(name) LIKE '%my%' OR LOWER(name) LIKE '%мой%';


-- Задание 3
-- Количество исполнителей в каждом жанре.
SELECT name, count(name)
FROM genres
JOIN genres_and_artists
ON genres.id = genres_and_artists.genre_id
GROUP BY name;

-- Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT count(*)
FROM tracks
JOIN albums
ON tracks.album_id = albums.id
WHERE albums.release BETWEEN 2019 AND 2020;

-- Средняя продолжительность треков по каждому альбому.
SELECT albums.name "album", AVG(tracks.duration) "avg duration"
FROM albums
JOIN tracks
ON tracks.album_id = albums.id
GROUP BY albums.name;

-- Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT artists.name
FROM artists
WHERE NOT EXISTS (
    SELECT *
    FROM albums_and_artists
    JOIN albums ON albums_and_artists.album_id = albums.id
    WHERE albums_and_artists.artist_id = artists.id AND albums.release = 2020
);

-- Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
SELECT collections.name
FROM collections
JOIN collections_and_tracks ON collections_and_tracks.collection_id = collections.id
JOIN tracks ON tracks.id = collections_and_tracks.track_id
JOIN albums ON albums.id = tracks.album_id
JOIN albums_and_artists ON albums_and_artists.album_id = albums.id
JOIN artists ON artists.id = albums_and_artists.artist_id
WHERE artists.name = 'Mike Johnson'
GROUP BY collections.name;
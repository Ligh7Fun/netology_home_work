CREATE TABLE genres (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(70) NOT NULL UNIQUE,
    description TEXT NOT NULL
);
CREATE TABLE collections (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(70) NOT NULL,
    release INTEGER NOT NULL CHECK
	(release > 1900 AND release < 2100)
);
CREATE TABLE artists (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(70) NOT NULL UNIQUE,
    biography TEXT NOT NULL
);
CREATE TABLE albums (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(70) NULL UNIQUE,
    description TEXT NOT NULL,
    release INTEGER NOT NULL CHECK
	(release > 1900 AND release < 2100)
);
CREATE TABLE tracks (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(70) NOT NULL UNIQUE,
    duration INTEGER NOT NULL,
    album_id INTEGER NULL REFERENCES albums(id)
);
CREATE TABLE genres_and_artists (
    id SERIAL NOT NULL PRIMARY KEY,
    artist_id INTEGER NOT NULL REFERENCES artists(id),
    genre_id INTEGER NOT NULL REFERENCES genres(id)
);
CREATE TABLE albums_and_artists (
    id SERIAL NOT NULL PRIMARY KEY,
    album_id INTEGER NOT NULL REFERENCES albums(id),
    artist_id INTEGER NOT NULL REFERENCES artists(id)
);
CREATE TABLE collections_and_tracks (
    id SERIAL NOT NULL PRIMARY KEY,
    track_id INTEGER NOT NULL REFERENCES tracks(id),
    collection_id INTEGER NOT NULL REFERENCES collections(id)
);
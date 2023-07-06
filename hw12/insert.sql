-- Жанры
INSERT INTO genres (name, description) VALUES
    ('Rock', 'Жанр рок-музыки, характеризующийся гитарными рифами и энергичными ритмами.'),
    ('Pop', 'Популярный музыкальный жанр с акцентом на мелодии и коммерческую привлекательность.'),
    ('Hip Hop', 'Музыкальный стиль, развившийся из афроамериканской культуры, основанный на речитативе и ритмичных рифмах.'),
    ('Electronic', 'Электронная музыка, создаваемая с использованием электронных инструментов и технологий.');

-- Сборники
INSERT INTO collections (name, release) VALUES
    ('Best of 2000s', 2009),
    ('Summer Hits', 2018),
    ('Oldies but Goldies', 1985),
    ('Top 40', 2022);

-- Исполнители
INSERT INTO artists (name, biography) VALUES
    ('John Doe', 'John Doe is a talented singer-songwriter known for his soulful voice and heartfelt lyrics.'),
    ('Jane Smith', 'Jane Smith is a versatile musician who excels in both singing and playing multiple instruments.'),
    ('Mike Johnson', 'Mike Johnson is a rock guitarist renowned for his electrifying solos and energetic stage presence.'),
    ('Emily', 'Emily Davis is a rising star in the pop music scene with her catchy tunes and captivating performances.');

-- Альбомы
INSERT INTO albums (name, description, release) VALUES
    ('Greatest Hits', 'A compilation of the artist''s most popular songs.', 2010),
    ('Revolution', 'The artist''s latest album showcasing their growth and experimentation.', 2021),
    ('In the Spotlight', 'An album that highlights the artist''s vocal range and emotional depth.', 2020),
    ('Journey Within', 'A collection of introspective songs inspired by the artist''s personal experiences.', 2018),
    ('Rock Anthems', 'Сборник лучших рок-песен всех времен.', 2019);

-- Треки
INSERT INTO tracks (name, duration, album_id) VALUES
    ('The One', 240, 1),
    ('Love Me Now', 320, 1),
    ('Freedom', 280, 2),
    ('Rise Up', 290, 2),
    ('Unbreakable', 260, 3),
    ('Shine On', 300, 3),
    ('Dreamer', 230, 4),
    ('Мой город', 270, 4),
    ('Midnight Groove', 210, 2),
    ('Livin'' on a Prayer', 280, 5),
    ('My Heart Will Go On', 250, 4);

-- Связи
INSERT INTO genres_and_artists (artist_id, genre_id) VALUES
    (1, 1),
    (2, 2),
    (3, 1),
    (3, 3),
    (4, 2);

INSERT INTO albums_and_artists (album_id, artist_id) VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (5, 4);

INSERT INTO collections_and_tracks (track_id, collection_id) VALUES
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 2),
    (5, 3),
    (6, 3),
    (7, 4),
    (8, 4),
    (9, 2),
    (10, 3);

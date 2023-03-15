CREATE TABLE IF NOT EXISTS Genres (
	id SERIAL PRIMARY KEY,
	genre_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Performers (
	id SERIAL PRIMARY KEY,
	alias VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Albums (
	id SERIAL PRIMARY KEY,
	album_title VARCHAR(60) UNIQUE NOT NULL,
	year TINYINT(4) NOT NULL
);

CREATE TABLE IF NOT EXISTS PerformersAllGenres (
	performer_id INTEGER REFERENCES Performers(id),
	genre_id INTEGER REFERENCES Genres(id),
	CONSTRAINT gp PRIMARY KEY (preformer_id, genre_id)
);

CREATE TABLE IF NOT EXISTS PerformersAllAlbums (
	performer_id INTEGER REFERENCES Performers(id),
	album_id INTEGER REFERENCES Albums(id),
	constraint pa PRIMARY KEY (performer_id, album_id)
);

CREATE TABLE IF NOT EXISTS Tracks (
	id SERIAL PRIMARY KEY,
	track_title VARCHAR(80) NOT NULL,
	duration TIME not NULL CHECK(duration > 0),
	album_id INTEGER REFERENCES Albums(album_id)
);

CREATE TABLE IF NOT EXISTS Collections (
	id SERIAL PRIMARY KEY,
	collection_title VARCHAR(80) NOT NULL,
	year TINYINT(4) NOT NULL
);

CREATE TABLE IF NOT EXISTS TracksInCollections (
	collection_id INTEGER REFERENCES Collections(id),
	track_id INTEGER REFERENCES Tracks(id),
	CONSTRAINT ct PRIMARY KEY (collection_id, track_id)
);

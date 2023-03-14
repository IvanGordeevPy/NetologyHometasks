CREATE TABLE IF NOT EXISTS Genres (
	id INTEGER PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS performer (
	performerID INTEGER PRIMARY KEY,
	alias VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS album (
	albumID INTEGER PRIMARY KEY,
	album_title VARCHAR(80) NOT NULL,
	release_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS genreperformer (
	genreID INTEGER REFERENCES genre(genreID),
	performerID INTEGER REFERENCES performer(performerID),
	CONSTRAINT pk_genreperformer PRIMARY KEY (genreID, performerID)
);

CREATE TABLE IF NOT EXISTS performeralbum (
	albumID INTEGER REFERENCES album(albumID),
	performerID INTEGER REFERENCES performer(performerID),
	constraint pk_performeralbum PRIMARY KEY (albumID, performerID)
);

CREATE TABLE IF NOT EXISTS track (
	trackID INTEGER PRIMARY KEY,
	albumID INTEGER REFERENCES album(albumID),
	track_title VARCHAR(80) not null,
	duration TIME not NULL
);

CREATE TABLE IF NOT EXISTS music_collection (
	collectionID INTEGER PRIMARY KEY,
	collection_title VARCHAR(80) not null,
	release_year INTEGER not null
);

CREATE TABLE IF NOT EXISTS trackcollection (
	trackID INTEGER REFERENCES track(trackID),
	collectionID INTEGER REFERENCES music_collection(collectionID),
	CONSTRAINT pk_trackcollection PRIMARY KEY (trackID, collectionID)
);

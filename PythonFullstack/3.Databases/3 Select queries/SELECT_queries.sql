SELECT album_title, year FROM Albums
WHERE year = 2018;

SELECT track_title, duration FROM Tracks
WHERE duration = MAX(duration)

SELECT track_title, duration FROM Tracks
WHERE duration >= 3.50;

SELECT collection_title FROM Collections
WHERE year >= 2018 AND year <= 2020;

SELECT alias FROM Performers
WHERE alias NOT LIKE '%% %%';

SELECT track_title FROM Tracks
WHERE track_title LIKE '%%my%%';

-- количество исполнителей в каждом жанре
SELECT g.name, count(pag.performer_id) FROM PerformersAllGenres pag
JOIN Genres g ON pag.genre_id = g.id 
GROUP BY g.name;

-- количество треков, вошедших в альбомы 2019-2020 годов
SELECT a.album_title, count(t.id) Amount FROM Tracks t
JOIN Albums a ON t.album_id = a.id
WHERE a.year = 2019 OR a.year = 2020
GROUP BY a.album_title;

-- средняя продолжительность треков по каждому альбому
SELECT a.album_title, AVG(t.duration) Average FROM Tracks t
JOIN Albums a ON t.album_id = a.id 
GROUP BY a.album_title;

-- все исполнители, которые не выпустили альбомы в 2020 году
SELECT p.alias, a.year FROM Performers p
JOIN PerformersAllAlbums paa ON p.id = paa.performer_id 
JOIN Albums a ON paa.album_id = a.id 
WHERE paa.performer_id NOT IN 
(SELECT paa.performer_id FROM PerformersAllAlbums
WHERE a.year = 2020);

-- названия сборников, в которых присутствует конкретный исполнитель:
SELECT c.collection_title, p.alias FROM Performers p
JOIN PerformersAllAlbums paa ON p.id = paa.performer_id 
JOIN Albums a ON paa.album_id = a.id 
JOIN Tracks t ON a.id = t.album_id 
JOIN TracksInCollections tic ON t.id = tic.track_id 
JOIN Collections c ON tic.collection_id = c.id 
WHERE p.alias = 'Kordhell';

-- название альбомов, в которых присутствуют исполнители более 1 жанра
SELECT a.album_title, p.alias FROM Performers p
JOIN PerformersAllAlbums paa ON p.id = paa.performer_id 
JOIN Albums a ON paa.album_id = a.id 
JOIN PerformersAllGenres pag ON p.id = pag.performer_id 
GROUP BY a.album_title, p.alias
HAVING COUNT(pag.genre_id) > 1;

-- наименование треков, которые не входят в сборники
SELECT track_title FROM Tracks t
LEFT JOIN TracksInCollections tic ON t.id = tic.track_id 
WHERE tic.track_id IS NULL;

-- исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
SELECT alias FROM Performers p
JOIN PerformersAllAlbums paa ON p.id = paa.performer_id 
JOIN Albums a ON paa.album_id = a.id 
JOIN Tracks t ON a.id = t.album_id 
WHERE t.duration = (SELECT MIN(duration) FROM Tracks);

-- название альбомов, содержащих наименьшее количество треков
SELECT a.album_title, COUNT(t.id) FROM Albums a
JOIN Tracks t ON a.id = t.album_id 
GROUP BY a.album_title
HAVING COUNT(t.id) IN (SELECT COUNT(t.id) FROM Albums a
JOIN Tracks t ON a.id = t.album_id 
GROUP BY a.album_title
ORDER BY COUNT(t.id)
LIMIT 1);

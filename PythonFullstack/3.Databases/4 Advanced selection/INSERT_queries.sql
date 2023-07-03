-- айди можно не писать, тк они заданы как серийные номера
-- в ограничениях, но для наглядности оставим:

INSERT INTO Performers
VALUES (1,'BONES'),
       (2,'Kordhell'),
       (3,'Rezz'),
       (4,'Hugeloud'),
       (5,'Pulsedriver'),
       (6,'Bad Smith'),
       (7,'Pastel Ghost'),
       (8,'Senkya'),
       (9,'Hiko');

INSERT INTO Genres
VALUES (1,'phonk'),
       (2,'dance music'),
       (3,'hip-hop'),
       (4,'trance'),
       (5,'electronic music'),
       (6,'pop');
       
INSERT INTO Albums
VALUES (1,'The Best', 2019),
     (2,'Split', 2022),
     (3,'Personalities', 2018),
     (4,'Freestyle', 2011),
     (5,'Moon',2021),
     (6,'Season 6', 2015),
     (7,'Wanna sleep', 2016),
     (8,'Idk', 2017),
     (9,'Slay',2022);
     
INSERT INTO Tracks
VALUES (1,'FIND', 2.21, 1),
      (2,'MYWAY', 3.59, 9),
      (3,'High', 1.5, 8),
      (4,'Circus', 4.18, 7),
      (5,'Hearts', 3.20, 6),
      (6,'Who we are', 1.01, 5),
      (7,'Tainted love', 3.21, 4),
      (8,'Matrix', 8.10, 3),
      (9,'Bombay', 4.15, 2),
      (10,'Need', 2.56, 1),
      (11,'Flash', 1.20, 5),
      (12,'Bad', 2.45, 9),
      (13,'Pharmacy', 5.00, 3),
      (14,'Sleepwell', 7.15, 7),
      (15,'The Sign', 5.04, 2);

INSERT INTO Collections 
VALUES (1,'Mood',2022),
       (2,'Vibe', 2021),
       (3,'atmosphere', 2019),
       (4,'reason why', 2020),
       (5,'backtoschool', 2022),
       (6,'nearest future', 2021),
       (7,'pumpKING', 2019),
       (8,'spoky season', 2022);

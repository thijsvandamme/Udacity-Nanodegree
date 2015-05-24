-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players (id serial PRIMARY KEY, name varchar(255));
CREATE TABLE matches (match_id serial PRIMARY KEY, p1 int REFERENCES players(id), p2 int REFERENCES players(id), winner int DEFAULT 0);


CREATE VIEW totalwins AS
	SELECT players.id,
    players.name,
    count(matches.winner) AS wins
   FROM (players
     LEFT JOIN matches ON ((players.id = matches.winner)))
  GROUP BY players.id
  ORDER BY count(matches.winner) DESC;

CREATE VIEW totalmatches AS
	SELECT players.id,
    players.name,
    count(matches.match_id) AS matches
   FROM (players
     LEFT JOIN matches ON (((players.id = matches.p1) OR (players.id = matches.p2))))
  GROUP BY players.id
  ORDER BY players.id;

CREATE VIEW tournamentstandings AS
 SELECT players.id,
    players.name,
    totalwins.wins,
    totalmatches.matches
   FROM ((players
     JOIN totalwins ON ((players.id = totalwins.id)))
     LEFT JOIN totalmatches ON ((players.id = totalmatches.id)))
  ORDER BY totalwins.wins DESC;


# EnFuego
version: 1.0.0

`server`: localhost:8000



## /pointtable
Returns the point table standings of all teams in order.
 Response:  array of objects.
 Properties of each objects:
 - team_id	(string)
 - gamesplayed	(int)
 - gameswon	(int)
 - gamesdraw	(int)
 - gameslost	(int)
 - goalsscored	(int)
 - goalsconceded	(int)
 - goaldifference	(int)
 - points	(int)
#### sample response
`
[{"team_id": "EEE", "gamesplayed": 3, "gameswon": 1, "gamesdraw": 1, "gameslost": 1, "goalsscored": 3, "goalsconceded": 3, "goaldifference": 0, "points": 4}, {"team_id": "MECH", "gamesplayed": 1, "gameswon": 1, "gamesdraw": 0, "gameslost": 0, "goalsscored": 7, "goalsconceded": 0, "goaldifference": 7, "points": 3}, {"team_id": "ECB", "gamesplayed": 1, "gameswon": 1, "gamesdraw": 0, "gameslost": 0, "goalsscored": 2, "goalsconceded": 0, "goaldifference": 2, "points": 3}, {"team_id": "CSB", "gamesplayed": 2, "gameswon": 1, "gamesdraw": 0, "gameslost": 1, "goalsscored": 2, "goalsconceded": 8, "goaldifference": -6, "points": 3}, {"team_id": "ECA", "gamesplayed": 1, "gameswon": 0, "gamesdraw": 1, "gameslost": 0, "goalsscored": 1, "goalsconceded": 1, "goaldifference": 0, "points": 1}, {"team_id": "EB", "gamesplayed": 1, "gameswon": 0, "gamesdraw": 0, "gameslost": 1, "goalsscored": 0, "goalsconceded": 1, "goaldifference": -1, "points": 0}, {"team_id": "CSA", "gamesplayed": 1, "gameswon": 0, "gamesdraw": 0, "gameslost": 1, "goalsscored": 0, "goalsconceded": 2, "goaldifference": -2, "points": 0}]
`


## /completefixtures
Returns all the fixtures ordered by match number.
 Response:  array of objects.
 Properties of each objects:
 - matchnumber	(int)
 - teama_id	(string)
 - teamb_id	(string)
 - scorea	(int)  // null if the match has not yet taken place
 - scoreb	(int)  // null if the match has not yet taken place
 - date	(string) // format is yyyy-mm-dd
 - finished	(boolean)   // true if match is over; false if match is not yet over.
#### sample response
 `
 [{"matchnumber": 1, "teama_id": "ECB", "teamb_id": "CSA", "scorea": 2, "scoreb": 0, "date": "2022-06-27", "finished": true}, {"matchnumber": 2, "teama_id": "EEE", "teamb_id": "ECA", "scorea": 1, "scoreb": 1, "date": "2022-06-28", "finished": true}, {"matchnumber": 3, "teama_id": "CSB", "teamb_id": "MECH", "scorea": 0, "scoreb": 7, "date": "2022-06-29", "finished": true}, {"matchnumber": 4, "teama_id": "EB", "teamb_id": "EEE", "scorea": 0, "scoreb": 1, "date": "2022-06-30", "finished": true}, {"matchnumber": 5, "teama_id": "MECH", "teamb_id": "ECB", "scorea": null, "scoreb": null, "date": "2022-07-01", "finished": false}, {"matchnumber": 10, "teama_id": "CSB", "teamb_id": "EEE", "scorea": 2, "scoreb": 1, "date": "2022-07-14", "finished": true}]
`

## /specificfixtures
Returns fixtures of a particular team ordered by match number.
Required Query parameter:
- team (string for among the list ["CSA", "CSB", "EB", "ECA", "ECB", "EEE", "MECH"] )
 Response:  array of objects.
 Properties of each objects:
 - matchnumber	(int)
 - teama_id	(string)
 - teamb_id	(string)
 - scorea	(int)  // null if the match has not yet taken place
 - scoreb	(int)  // null if the match has not yet taken place
 - date	(string) // format is yyyy-mm-dd
 - finished	(boolean)   // true if match is over; false if match is not yet over.

#### sample request
`http://localhost:8000/specificfixtures/?team=EEE`
#### sample response
`[{"matchnumber": 2, "teama_id": "EEE", "teamb_id": "ECA", "scorea": 1, "scoreb": 1, "date": "2022-06-28", "finished": true}, {"matchnumber": 4, "teama_id": "EB", "teamb_id": "EEE", "scorea": 0, "scoreb": 1, "date": "2022-06-30", "finished": true}, {"matchnumber": 10, "teama_id": "CSB", "teamb_id": "EEE", "scorea": 2, "scoreb": 1, "date": "2022-07-14", "finished": true}]`

## /goalscorers
Returns all the goal scorers.
 Response:  array of objects.
 Properties of each objects:
 - name (string)
 - team_id	(string)
 - goalsscored  (int)

#### sample response
`[{"name": "rakesh", "team_id": "ECA", "goalsscored": 6}, {"name": "sreejith", "team_id": "CSB", "goalsscored": 4}]`

## /guidelines
Returns all the rules and regulations.
 Response:  array of objects.
 Properties of each objects:
 - rule (string)

#### sample response
`[{"rule": "7 side tournament"}, {"rule": "boots are compulsory"}, {"rule": "each half is of 15 min"}]`

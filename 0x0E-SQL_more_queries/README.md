# 0x0E. SQL - More queries

This project expands on MySQL by introducing the following concepts:
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Requirements for SQL scripts
- All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- The length of your files will be tested using wc

---
File | Task
---|---
0-privileges.sql | A script that lists all privileges of the MySQL users ```user_0d_1``` and ```user_0d_2```
1-create_user.sql | A script that creates the MySQL server user ```user_0d_1```
2-create_read_user.sql | A script that creates the database ```hbtn_0d_2``` and the user ```user_0d_2```
3-force_name.sql | A script that creates the table ```force_name```
4-never_empty.sql | A script that creates the table ```id_not_null```
5-unique_id.sql | A script that creates the table ```unique_id```
6-states.sql | A script that creates the database ```hbtn_0d_usa``` and the table ```states```
7-cities.sql | A script that creates the database ```hbtn_0d_usa``` and the table ```cities```
8-cities_of_california_subquery.sql | A script that lists all the cities of California that can be found in the database ```hbtn_0d_usa```
9-cities_by_state_join.sql | A script that lists all cities contained in the database ```hbtn_0d_usa```
10-genre_id_by_show.sql | A script that lists all shows contained in ```hbtn_0d_tvshows``` that have at least one genre linked
11-genre_id_all_shows.sql | A script that lists all shows contained in the database ```hbtn_0d_tvshows```
12-no_genre.sql | A script that lists all shows contained in ```hbtn_0d_tvshows``` without a genre linked
13-count_shows_by_genre.sql | A script that lists all genres from ```hbtn_0d_tvshows``` and displays the number of shows linked to each
14-my_genres.sql | A script that uses the ```hbtn_0d_tvshows``` database to list all genres of the show ```Dexter```
15-comedy_only.sql | A script that lists all Comedy shows in the database ```hbtn_0d_tvshows```
16-shows_by_genre.sql | A script that lists all shows and all genres linked to that show from the database ```hbtn_0d_tvshows```

## Author
Francesca Cantor
### logs Analysis

-project of fullstack nanodegree


## About this project

This is the first project for the Udacity Full Stack Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

## Needed the program

Python3
Vagrant
Virtual box



## To Run

Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

The database includes three tables:
-how to join the table
-how to aggregate table

To execute the program, run `python newsdata.py` from the command line.

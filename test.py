import psycopg2

dbname ="news"
conn = psycopg2.connect(dbname="news")
cursor = conn.cursor()

query1 = "SELECT title FROM articles, (SELECT count(path), path FROM log GROUP BY path ORDER BY count DESC FETCH FIRST 4 ROWS ONLY) AS foo WHERE foo.path LIKE '%'||articles.slug||'%'"

cursor.execute(query1)
ret1 = cursor.fetchall()
print ret1

query2 = "SELECT name FROM (SELECT count(name), name FROM log, (SELECT articles.slug, authors.name FROM articles INNER JOIN authors ON (articles.author = authors.id)) as foo WHERE log.path LIKE '%'||foo.slug||'%'GROUP BY name) as ret  ORDER BY ret.count DESC LIMIT 1"

cursor.execute(query2)
ret2 = cursor.fetchall()
print ret2
query3 = " WITH t1 AS (SELECT count(*) AS n, time::timestamp::date as time1 FROM log GROUP BY time::timestamp::date), t2 AS (SELECT count(*) AS m, time::timestamp::date as time2 FROM log WHERE status LIKE '%404%' GROUP BY time::timestamp::date) SELECT t1.time1, n, m, (100.0 * m) / n as Pct  FROM t1, t2 where t1.time1 = t2.time2 ORDER BY pct DESC LIMIT 1"



cursor.execute(query3)
ret3 = cursor.fetchall()
print ret3


























#1.What are the most popular three articles of all time?
#              title               
#----------------------------------
# Bad things gone, say good people
# Bears love berries, alleges bear
# Candidate is jerk, alleges rival

#2.Who are the most popular article authors of all time?

#news=> SELECT name FROM (SELECT count(name), name FROM log, (SELECT articles.slug, authors.name FROM articles INNER JOIN authors ON (articles.author = authors.id)) as foo WHERE log.path LIKE '%'||foo.slug||'%'GROUP BY name) as ret  ORDER BY ret.count DESC LIMIT 1;
#      name       
#-----------------
# Ursula La Multa

#3. On which days did more than 1% of requests lead to errors?


#news=> WITH t1AS (SELECT count(*) AS n, time::timestamp::date as time1 FROM log GROUP BY time::timestamp::date), t2 AS (SELECT count(*) AS m, time::timestamp::date as time2 FROM log WHERE status LIKE '%404%' GROUP BY time::timestamp::date) SELECT t1.time1, n, m, (100.0 * m) / n as Pct  FROM t1, t2 where t1.time1 = t2.time2;



# to store results
# query_1_result = dict()
#query_1_result['title'] = "\n1. The 3 most popular articles of all time are:\n"

#query_2_result = dict()
#query_2_result['title'] = """\n2. The most popular article authors of
#all time are:\n"""

#query_3_result = dict()
#query_3_result['title'] = """\n3. Days with more than 1% of request that

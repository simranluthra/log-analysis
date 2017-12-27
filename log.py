#!/usr/bin/env python2
import psycopg2
DBNAME = "news"

# 'q-1 What are the most popular three articles of all time?'
query1 = "SELECT a.title,count(*) AS views FROM articles a inner join log l \
          ON a.slug = substr(l.path,10) \
          WHERE l.status = '200 OK' \
          GROUP BY a.title, l.path \
          ORDER BY views DESC LIMIT 3;"

# 'q-2 Who are the most popular authors of all time?'
query2 = "SELECT author.name, count(*) AS views FROM authors author inner JOIN \
          articles a ON author.id = a.author inner JOIN log l ON  \
          a.slug = substr(l.path,10)\
          GROUP BY author.name \
          ORDER BY views DESC LIMIT 5;"

# 'q-3 On which days did more than 1% of requests lead to errors?'
query3 = "SELECT Date, percentage_error \
          FROM bad_status\
          WHERE percentage_error > 1;"

# function to run all the queries.


def get_results(query, string):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    for i in results:
        print i[0],
        print ' - ',
        print i[1],
        print string
    db.close()
    return


# calling function for first query
print "\n\nWhat are the most popular three articles of all time?\n"
get_results(query1, 'views')

# calling function for second query
print "\n\nWho are the most popular authors of all time?\n"
get_results(query2, 'views')

# calling function for third query
print "\n\nOn which days did more than 1% of requests lead to errors?\n"
get_results(query3, '%')


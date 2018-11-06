#!/usr/bin/env python
import psycopg2 as psql


DB_NAME = 'news'


def top_articles():
    """List top three articles of all times by numbers of views"""

    query = """
    SELECT title,
       COUNT(title) AS Views
    FROM articles
    JOIN log ON PATH = concat('/article/', articles.slug)
    GROUP BY title
    ORDER BY Views DESC
    LIMIT 3;
    """
    articles = execute_query(query)
    print('\nMost popular three articles of all time:-')
    for article in articles:
        print(str(articles.index(article) + 1) + '- ' +
              article[0] + ' - ' + str(article[1]) + ' Views')


def top_authors():
    """List top three article authors of all time"""
    
    query = """
    SELECT name,
    COUNT(title) AS Views
    FROM articles
    JOIN authors ON authors.id = articles.author
    JOIN log ON PATH = concat('/article/', articles.slug)
    GROUP BY name
    ORDER BY Views DESC;
    """
    authors = execute_query(query)
    print('\nMost popular article authors of all time:-')
    for author in authors:
        print(str((authors.index(author) + 1)) + '- ' +
              author[0] + ' - ' + str(author[1]) + ' Views')


def err_day():
    """List days that more that 1% of requests lead to errors"""

    query = """
    WITH reqs AS(
            SELECT time::date as date,
            COUNT(*)
            FROM log
            GROUP BY date
            ORDER BY date
    ), errs AS(
            SELECT time::date as date,
            COUNT(*)
            FROM log
            WHERE status != '200 OK'
            GROUP BY date
            ORDER BY date
    ), err_rate AS(
            SELECT reqs.date,
            errs.count::float / reqs.count::float * 100
            AS err_pct
            FROM reqs, errs
            WHERE reqs.date = errs.date
     ) SELECT * FROM err_rate WHERE err_pct > 1;
    """
    requests = execute_query(query)
    print('\nDays which more than 1% of requests lead to errors:-')
    for request in requests:
        print(request[0].strftime('%B %d, %Y') + ' - ' +
              str(round(request[1], 2)) + '% errors \n')


def execute_query(query):
        """
        Helper funcation that takes an SQL query as a parameter, 
        executes the query and returns the results as a list of tuples.

        args:
        query - (string) an SQL query statement to be executed.

        returns:
        A list of tuples containing the results of the query.
        """
        try:
            db = psql.connect(database=DB_NAME)
            c = db.cursor()
            c.execute(query)
            results = c.fetchall()
            db.close()
            return results
        except (Exception, psql.DatabaseError) as err:
            print(err)


if __name__ == '__main__':
    top_articles()
    top_authors()
    err_day()

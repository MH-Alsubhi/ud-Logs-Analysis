# import python db api
import psycopg2 as psql

# create a var for db name
DB_NAME = 'news'

def top_articles():
    db = psql.connect(database=DB_NAME)
    c = db.cursor()
    q = """
    SELECT title,
       COUNT(title) AS Views
    FROM articles
    JOIN log ON PATH = concat('/article/', articles.slug)
    GROUP BY title
    ORDER BY Views DESC
    LIMIT 3;
    """
    c.execute(q)
    articles = c.fetchall()
    db.close()
    print('\nMost popular three articles of all time:-')
    for article in articles:
        print(str(articles.index(article) + 1) + '- ' +
              article[0] + ' - ' + str(article[1]) + ' Views')


def top_authors():
    db = psql.connect(database=DB_NAME)
    c = db.cursor()
    q = """
    SELECT name,
    COUNT(title) AS Views
    FROM articles
    JOIN authors ON authors.id = articles.author
    JOIN log ON PATH = concat('/article/', articles.slug)
    GROUP BY name
    ORDER BY Views DESC;
    """
    c.execute(q)
    authors = c.fetchall()
    db.close()
    print('\nMost popular article authors of all time:-')
    for author in authors:
        print(str((authors.index(author) + 1)) + '- ' +
              author[0] + ' - ' + str(author[1]) + ' Views')


def err_day():
    db = psql.connect(database=DB_NAME)
    c = db.cursor()
    q = """
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
    c.execute(q)
    requests = c.fetchall()
    db.close()
    print('\nDays which more than 1% of requests lead to errors:-')
    for request in requests:
        print(request[0].strftime('%B %d, %Y') + ' - ' +
              str(round(request[1], 2)) + '% errors \n')

if __name__ == '__main__':
    top_articles()
    top_authors()
    err_day()

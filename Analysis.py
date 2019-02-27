#!/usr/bin/env python3
import psycopg2

# Answer1
PopularArticles = """
SELECT articles.title,
count(*)
FROM log,articles
WHERE log.path = '/article/' || articles.slug
GROUP BY articles.title
ORDER BY count(*) DESC
LIMIT 3;
"""
# Answer2
PopularAuthors = """
SELECT authors.name,
count(*)
FROM log,articles,authors
WHERE log.path = '/article/' || articles.slug
GROUP BY authors.name
ORDER BY count(*) DESC;
"""

# Answer3
MoreThanOnePercent = """
WITH num_requests AS (
SELECT time::date AS day, count(*)
FROM log
GROUP BY time::date
ORDER BY time::date
), num_errors AS (
SELECT time::date AS day,count(*)
FROM log
WHERE status != '200 OK'
GROUP BY time::date
ORDER BY time::date
), error_rate AS (
SELECT num_requests.day ,
num_errors.count::float /num_requests.count::float *100
AS error_pc
FROM num_requests,num_errors
WHERE num_requests.day = num_errors.day
)
SELECT * FROM error_rate WHERE error_pc > 1;
"""


def f():
    c = psycopg2.connect("dbname=news")
    curr = c.cursor()
    # Answer1 execution
    curr.execute(PopularArticles)
    results = curr.fetchall()
    print("|       Most Popular Articles       |")
    for result in results:
        print(
            '"{title}"" - {count} views'.format(title=result[0], count=result[1])
            )
    print("#"*70)
    # Answer2 execution
    curr.execute(PopularAuthors)
    results = curr.fetchall()
    print("|       Most Popular Authors       |")
    for result in results:
        print('{author} - {count} views'.format(author=result[0], count=result[1]))
    print("#"*70)
    # Answer3 execution
    curr.execute(MoreThanOnePercent)
    results = curr.fetchall()
    print("|       Days in Which More Than One Percent Error        |")
    for result in results:
        print(
            '{date:%B %d, %Y}-{error_rate:.1f}% errors'.
            format(date=result[0], error_rate=result[1]))
    print("#"*70)
    curr.close()
    c.close()

if __name__ == '__main__':
    f()

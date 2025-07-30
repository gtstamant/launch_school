import psycopg2
from psycopg2 import extras

connection = psycopg2.connect(dbname='films')

try:
    with connection:
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute("""SELECT genre, count(id)
                                FROM films
                               WHERE duration < 110
                            GROUP BY genre;
                           """)
            genres = cursor.fetchall()

finally:
    connection.close()

for row, genre in genres:
    print(f'{row}: {genre}')
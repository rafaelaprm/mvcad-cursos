import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect("dbname=curso_mvcad user=postgres password=xxx host=localhost")

connection.autocommit = True

cursor = connection.cursor(cursor_factory=RealDictCursor)

#cursor.execute("""SELECT table_name FROM information_schema.tables
#       WHERE table_schema = 'public'""")

#for table in cursor.fetchall():
#    print(table)
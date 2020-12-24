import psycopg2
from psycopg2.extras import RealDictCursor

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = [
        """
        CREATE TABLE pessoa (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            cpf CHAR(11) NOT NULL,
            estado VARCHAR(50) NOT NULL, 
            turma INTEGER NOT NULL,
            periodo VARCHAR(10) NOT NULL,
            modulo VARCHAR(100) NOT NULL
        )
        """
        ]

    connection = None

    try:
        # connect to the PostgreSQL server
        connection = psycopg2.connect("dbname=curso_mvcad user=postgres password=xxx host=localhost")
        
        cursor = connection.cursor()
        # create table one by one
        for command in commands:
            cursor.execute(command)
        # close communication with the PostgreSQL database server
        cursor.close()
        # commit the changes
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    create_tables()
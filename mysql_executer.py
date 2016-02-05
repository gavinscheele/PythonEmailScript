import mysql.connector


def execute_query(query, hostname, user, password, db_name):
    cnx = mysql.connector.connect(host=hostname, user=user, password=password, database=db_name)
    cursor = cnx.cursor()
    for result in cursor.execute(query, multi=True):
        pass
    cnx.commit()
    cursor.close()
    cnx.close()


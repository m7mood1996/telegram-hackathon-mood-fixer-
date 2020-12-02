import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Bandi4434!!!",
    db="sql_testing",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

#function will be passed with different categoryid based on flow.
def get_question_by_categoryID_randomly(id):
    try:
         with connection.cursor() as cursor:
             query=""" SELECT question FROM questions where categoryid = %s ORDER BY RAND() LIMIT 1"""
             cursor.execute(query,(id, ))
             result=cursor.fetchone()
    except:
        result = "ERROR connecting to DATABASE"
    return result

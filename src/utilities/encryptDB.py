import MySQLdb


db = MySQLdb.connect(host="localhost",
            user="root",
            passwd="password",
            database="progettoCritto")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

role = 'ceo'
matricola = '11111'
query = "select matricola from " + role + " where matricola = " + matricola
cur.execute(query)
row = cur.fetchall()
if (len(row) == 0):
        #se non ci sono corrispondenze
    print ('false')
else:
    print('true')


db.close()

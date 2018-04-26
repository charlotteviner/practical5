import sqlite3

conn = sqlite3.connect('resultsdb.sqlite')
c = conn.cursor()
#c.execute("CREATE TABLE Results (address text, burglaries integer)")
c.execute("INSERT INTO Results VALUES ('Queen Vic', 2)")
conn.commit()
conn.close()
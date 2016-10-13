import sqlite3
conn = sqlite3.connect('carrier.db')

pre=raw_input("Enter first 3 Digits: ");
database = conn.execute("SELECT Carrier, Type from DetectCarrier WHERE Number=:prefix", {"prefix": '1-876-'+pre})        
for row in database:
   print "\nCarrier >>", row[0]
   print "Type >> ", row[1]
   
conn.close()

import ConfigParser
import twisted.internet


'''
Database Connection Settings
'''


'''
###############################################################################
Production Settings
'''
pdb = dbmodule.connect('mydb', 'username', 'password') 


# PostgreSQL PyPgSQL
#cp = adbapi.ConnectionPool("pyPgSQL.PgSQL", database="pdb")

# MySQL
cp = adbapi.ConnectionPool("MySQLdb", db="pdb")


#Network Event management (mongoDB)



#Specify production logfile location

#MongoDB

#Redis



'''
###############################################################################
Development/Testing Settings
'''
tdb = dbmodule.connect('mydb', 'username', 'password') 


# PostgreSQL PyPgSQL
#cp = adbapi.ConnectionPool("pyPgSQL.PgSQL", database="pdb")

# MySQL
#cp = adbapi.ConnectionPool("MySQLdb", db="pdb

#SQLite


#Network Event management (mongoDB / network log-file)



#specify testing logfile location

#testlog = "/etc/netman/test.log";





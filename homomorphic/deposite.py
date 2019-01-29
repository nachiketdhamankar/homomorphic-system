#!c:\python27\python.exe
print "Content-Type: text/html\n\n"
import cgitb
import cgi
import MySQLdb
from paillier.paillier import *

db = MySQLdb.connect(host="localhost",user="root",passwd="",db="homomorphic")
cur = db.cursor()
cur1 = db.cursor()
cur2 = db.cursor()

form = cgi.FieldStorage()

user=form.getvalue("user")

p=0
q=0
cur1.execute("select * from tblreg where username='%s'"%(user))
try:
	for row in cur1.fetchall():
	    #name = row[0]
	    p = row[8]
except:
	print "No Records Found"	
	
cur2.execute("select * from tblreg where username='%s'"%(user))
try:
	for row in cur2.fetchall():	   
	    q = row[9]		
except:
	print "No Records Found"	



#print p
#print q
priv, pub = generate_keypair(16,p,q)

#print (priv.l,priv.m)
#print (pub.n)

print "<html lang='en'><head><title>Bootstrap Example</title>  <meta charset='utf-8'>"
print "<meta name='viewport' content='width=device-width, initial-scale=1'>"
print "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'>"
print "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>"
print "<script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js'></script>"
print "<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js'></script>"
print "<script src='java.js'></script>"
#print "<link rel='stylesheet' href='style.css'>"
print "</head><body style='background-color:#5bc0de;'>"
print "<nav class='navbar navbar-expand-md navbar-dark bg-dark'> <div class='navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2'> <ul class='navbar-nav mr-auto'> <li class='nav-item active'> <a class='nav-link' href='home.php'>Home</a> </li> </ul> </div> <div class='mx-auto order-0'> <a class='navbar-brand mx-auto' href='#'>Deposit Amount</a> <button class='navbar-toggler' type='button' data-toggle='collapse' data-target='.dual-collapse2'> <span class='navbar-toggler-icon'></span> </button> </div> <div class='navbar-collapse collapse w-100 order-3 dual-collapse2'> <ul class='navbar-nav ml-auto'> <li class='nav-item'> <a class='nav-link logout' href='logout.php'>Logout</a> </li> </ul> </div></nav>"

acno=0
prevbal=0
fname = ""
cur1.execute("select * from tblreg where username='%s'"%(user))
try:
	for row in cur1.fetchall():	   
	    acno= row[6]		
except:
	print "No Records Found"
#print acno	
ac = decrypt(priv,pub,int(acno))


cur1.execute("select * from tblreg where username='%s'"%(user))
try:
	for row in cur1.fetchall():	   
	    prevbal= row[7]		
except:
	print "No Records Found"
#print acno	
prevbal = decrypt(priv,pub,int(prevbal))
	
fname = user;	
print "<br><br><table  align='center'>"
print "<form action='depoamt.py?user=%s' method='post'>"%(user)
#print "<tr><td><input type='hidden' class='form-control input-sm' value='%s' name='acno' readonly></td></tr>"%(user)
print "<h3 style='text-align:center'>Hello, " +fname +"</h3>"
print "<h3 style='text-align:center; margin-bottom:2%;'>Please enter the following details</h3>"
print "<tr><td><label><font color='black'>Account No:</font></td><td><input type='text' class='form-control input-sm' value='%s' name='acno' readonly></td></tr>"%(int(ac))
print "<tr><td><label><font color='black'>Current Balance:</font></td><td><input type='text' class='form-control input-sm' value='%s' name='balance' readonly></td></tr>"%(int(prevbal))
print "<tr><td><label><font color='black'>Amount to Deposit	 :</font> </td><td><input type='text' class='form-control input-sm' name='amt' placeholder='Enter Amount to Deposit'></td></tr>"
print "<br/><tr><td></td><td><input type='submit' class='btn btn-danger' value='Deposit'></td></tr>"
print "</form></table>"
		
		

	
db.commit()
db.close()
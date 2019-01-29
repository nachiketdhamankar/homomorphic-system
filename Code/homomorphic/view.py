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
cur3 = db.cursor()
cur4 = db.cursor()

form = cgi.FieldStorage()

user=form.getvalue("user")

print "<html lang='en'><head><title>Bootstrap Example</title>  <meta charset='utf-8'>"
print "<meta name='viewport' content='width=device-width, initial-scale=1'>"
print "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'>"
print "<link rel='stylesheet' href='style.css'>"
print "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>"
print "<script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js'></script>"
print "<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js'></script>"
print "</head><body>"
print "<nav class='navbar navbar-expand-md navbar-dark bg-dark'> <div class='navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2'> <ul class='navbar-nav mr-auto'> <li class='nav-item active'> <a class='nav-link' href='home.php'>Home</a> </li> </ul> </div> <div class='mx-auto order-0'> <a class='navbar-brand mx-auto' href='#'>Account Details</a> <button class='navbar-toggler' type='button' data-toggle='collapse' data-target='.dual-collapse2'> <span class='navbar-toggler-icon'></span> </button> </div> <div class='navbar-collapse collapse w-100 order-3 dual-collapse2'> <ul class='navbar-nav ml-auto'> <li class='nav-item'> <a class='nav-link logout' href='logout.php'>Logout</a> </li> </ul> </div></nav>"
#p = 0
#q = 0
acno = 0
cur1.execute("select * from tblreg where username='%s'"%(user))


data = cur1.fetchall()
for row in data:
	acno = row[6]
	bal = row[7]
	p = row[8]
	q = row[9]


priv, pub = generate_keypair(16,p,q)

account = decrypt(priv, pub, int(acno))
balance = decrypt(priv, pub, int(bal))



cur.execute("select * from tblreg where username='%s'"%(user))

prevbal=0

try:
	for row in cur.fetchall():
		user = row[0]
		fname = row[1]
		lname = row[2]
		email = row[4]
		gender = row[5]
except:
	print "No Records Found"
	
#prevbal = decrypt(priv,pub,int(prevbal))
#print int(prevbal)

print "<h3 style='/*text-align:center*/margin: 2%;'>Hello, " +fname +"</h3>"
print "<h4 style='margin: -1.1% 0 2% 2.5%'>Here is your account information, </h4>"

#prevbal= row[7]
#print "<h4>Account No: %s</h4>"%(int(account))
print "<table class='table table-stripped'>"
print "<tr class='table-warning'><th>Acc No</th><th>User Name</th><th>First Name</th><th>Last Name</th><th>Email</th><th>Gender</th><th>Balance</th></tr>"

print "<tr class='table-primary'><td>"+str(account)+"</td><td>"+user+"</td>"
print "<td>"+fname+"</td>"
print "<td>"+lname+"</td>"
#print "<td>"+row[3]+"</td>"
print "<td>"+email+"</td>"
print "<td>"+gender+"</td>"
print "<td>"+str(balance)+"</td></tr>"

db.commit()
db.close()
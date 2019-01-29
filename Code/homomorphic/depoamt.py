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

amount=0
user=form.getvalue("user")
acno=form.getvalue("acno")
prevbal=form.getvalue("balance")
amount=form.getvalue("amt")

total = 0
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

bal=0	
cur.execute("select * from tblreg where username='%s'"%(user))

try:
	for row in cur.fetchall():	   
	    bal = row[7]		
except:
	print "No Records Found"
	


priv, pub = generate_keypair(16,p,q)

amount = encrypt(pub,int(amount))
#bal = encrypt(pub,int(bal))

total = e_add(pub,int(amount),int(bal))

z = decrypt(priv, pub, total)

cur.execute("update tblreg set balance=%s where username=%s",(total,user))
#cur1.execute("update tbldec set balance=%s where username=%s",(total,user))
print "<script> alert('Amount Deposited Successfully'); window.location.href='home.php?user=%s'</script>"%(user)
db.commit()
db.close()
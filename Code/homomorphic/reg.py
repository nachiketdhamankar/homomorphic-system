#!c:\python27\python.exe
print "Content-Type: text/html\n\n"
import cgitb
import cgi
import MySQLdb
from paillier.paillier import *
from paillier.primes import *


db = MySQLdb.connect(host="localhost",user="root",passwd="",db="homomorphic")
cur = db.cursor()
cur1 = db.cursor()
cur2 = db.cursor()
cur3 = db.cursor()
cur4 = db.cursor()

form = cgi.FieldStorage()
bits = 16
p = primes.generate_prime(bits / 2)
q = primes.generate_prime(bits / 2)


#print p
#print "\n"
#print q
priv, pub = generate_keypair(128,p,q)

bal = 0
username=form.getvalue("userName")
fname=form.getvalue("firstName")
lname=form.getvalue("lastName")
password=form.getvalue("password")
email=form.getvalue("userEmail")
gender=form.getvalue("gender")
accno=form.getvalue("accNo")

a=int(accno)

cur2.execute("select acno from tblreg")
cur3.execute("select p from tblreg")
cur4.execute("select q from tblreg")

p_list = []
while True:
	p = cur3.fetchone()
	if p == None:
		break
	p_list.append(p[0])

q_list = []
while True:
	q = cur4.fetchone()
	if q == None:
		break
	q_list.append(q[0])	

acc_list_enc = []
while True:
	row_d = cur2.fetchone()
	if row_d == None:
		break
	acc_list_enc.append(row_d[0])

acc_list_dec = []
for i,item in enumerate(acc_list_enc):
	priv, pub = generate_keypair(16,int(p_list[i]),int(q_list[i]))
	dec = decrypt(priv, pub, int(item))
	acc_list_dec.append(dec)

for x in acc_list_dec:
	if a == x:
		print "<script> alert('Account No. already exits') </script>"
		print "<script>window.location.href='register.php' </script>"

acno=encrypt(pub,a)
#print acno
print "\n"
balance = encrypt(pub,int(bal))
#print balance
z = decrypt(priv, pub, acno)
print "\n"
#print z 
print "\n"
balcz = decrypt(priv, pub, balance)
#print balcz

#acn = encrypt(pub, a)


cur.execute("insert into tblreg values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(username,fname,lname,password,email,gender,acno,balance,p,q))
cur1.execute("insert into tbldec values(%s,%s,%s)",(username,z,balcz))
print "<script>window.location.href='index.php'</script>"
db.commit()
db.close()
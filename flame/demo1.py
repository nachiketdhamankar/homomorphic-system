#!c:\python27\python.exe
print "Content-Type: text/html\n\n"

from paillier.rsa import *

import cgitb
import cgi

form = cgi.FieldStorage()

x=form.getvalue("data")
y=form.getvalue("data1")
m=(int(x)*int(y))
print"<html><head><title>Homomorphic Encryption</title></html>"
print "<meta charset='utf-8'> <meta name='viewport' content='width=device-width, initial-scale=1'>"
print "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>"
print "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>"
print "<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script></head><body>"

print "<form name='FormName' method='post'>"
print "<div class='container'><h2 style='text-align:center'>RSA Cryptosystem</h2></div>"
print "<div class='container' style='text-align:center'><br>First Number:<code>",x
print "<br style='text-align:center'></code>Second Number:<code>",y
print "</code><br><h4 style='text-align:center'>Multiplication of two Numbers Before Homomorphic Encryption is:<code>",(int(x)*int(y))
print "</code></h4></div><br>"

keys = generate_keypair_R(64)


print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary' style='text-align:center'>Randomly generated values:</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>p = %s\nq = %s</textarea></div>"%(keys.p,keys.q)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary' style='text-align:center'>Private and Public keys</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>Public Key: %s\nPrivate Key: %s</textarea></div>"%(keys.d, keys.e)

x = int(x)
print "<div class='container-fluid'><p class='p-3 mb-2 bg-danger text-white' style='text-align:center'>Entered Value of x =",x
print "</p></div>"

cx = encrypt_R(keys.e, x, keys.n)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Encrypted Value of x, ie, enc(x):</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>%s</textarea></div>"%(cx)

y = int(y)
print "<div class='container-fluid'><p class='p-3 mb-2 bg-danger text-white' style='text-align:center'>Entered Value of y =",y
print "</p></div>"

cy = encrypt_R(keys.e, y, keys.n)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Homomorphic Encryption Value of Y(cy):</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>%s</textarea></div>"%(cy)

print "<br><div class='container-fluid'><p class='p-3 mb-2 bg-danger text-dark'><h4 style='text-align:center'><strong>Performing Computations</strong></h4></p></div>"

cz = e_mul_R(cx, cy, keys.n)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>RSA Multiplication of Encrypted Numbers:</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>%s</textarea></div>"%(cz)


z = decrypt_R(keys.d,cz,keys.n)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Decrypting Value of enc(x) * enc(y):</p></label></center><center><input type='text' class='form-control' id='value1'  value='%s' style='text-align:center'/></center></div>"%(z)
print "</form>"


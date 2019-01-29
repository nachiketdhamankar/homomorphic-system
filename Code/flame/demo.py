#!c:\python27\python.exe
print "Content-Type: text/html\n\n"

from paillier.paillier import *

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
print "<div class='container'><h2 style='text-align:center'>Paillier Cryptosystem</h2></div>"
print "<div class='container' style='text-align:center'><br>First Number:<code>",x
print "<br style='text-align:center'></code>Second Number:<code>",y
print "</code><br><h4 style='text-align:center'>Addition of two Numbers Before Homomorphic Encryption is:<code>",(int(x)+int(y))
print "</code></h4></div><br>"

priv_P, pub_P = generate_keypair_P(16)

print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Randomly generated values:</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>p = %s\nq = %s</textarea></div>"%(priv_P.p,priv_P.q)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Private and Public keys:</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>Private Key (lambda, mu): %s \nPublic Key (n, g): %s</textarea></div>"%(priv_P, pub_P)

x = int(x)
print "<div class='container-fluid'><p class='p-3 mb-2 bg-danger text-white' style='text-align:center'>Entered Value of x =",x
print "</p></div>"


cx,r1 = encrypt_P(pub_P, x)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Encrypted Value of x, ie, enc(x):</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>%s \n r = %s</textarea></div><br/>"%(cx,r1)


y = int(y)
print "<div class='container-fluid'><p class='p-3 mb-2 bg-danger text-white' style='text-align:center'>Entered Value of y =", y
print "</p></div>"

cy,r2 = encrypt_P(pub_P, y)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Encrypted Value of y, ie, enc(y):</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>%s \n r = %s</textarea></div>"%(cy,r2)


print "<br><div class='container-fluid'><p class='p-3 mb-2 bg-danger text-dark'><h4 style='text-align:center'><strong>Performing Computations</strong></h4></p></div>"
cz = e_add_P(pub_P, cx, cy)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Paillier Addition of Encrypted Numbers</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>%s</textarea></div>"%(cz)


print "<div class='container-fluid'><p class='p-3 mb-2 bg-success text-white'></p></div>"
z = decrypt_P(priv_P, pub_P, cz)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Decrypting Value of enc(x) + enc(y):</p></label></center><center><input type='text' class='form-control' id='value1' style='text-align:center'  value='%s'/></center></div>"%(z)
print "</form>"

print "<br><div class='container-fluid'><p class='p-3 mb-2 bg-danger text-dark' style='text-align:center'>----------</p></div>"
cz_mul_const_P = e_mul_const_P(pub_P, cx, 5)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Paillier Multiplication of encrypted value with constant</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>%s</textarea></div>"%(cz_mul_const_P)

print "<div class='container-fluid'><p class='p-3 mb-2 bg-success text-white'></p></div>"
z_mul_const_P = decrypt_P(priv_P, pub_P, cz_mul_const_P)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Decrypting Value of enc(x)*5:</p></label></center><center><input type='text' class='form-control' id='value1' style='text-align:center' value='%s'/></center></div>"%(z_mul_const_P)
print "</form>"


print "<br><div class='container-fluid'><p class='p-3 mb-2 bg-danger text-dark' style='text-align:center'>----------</p></div>"
cz_add_const_P = e_add_const_P(pub_P, cx, 7)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Paillier Addition of encrypted value with constant</p></label></center><textarea class='form-control' id='exampleFormControlTextarea1' style='text-align:center'>%s</textarea></div>"%(cz_add_const_P)

print "<div class='container-fluid'><p class='p-3 mb-2 bg-success text-white'></p></div>"
z_add_const_P = decrypt_P(priv_P, pub_P, cz_add_const_P)
print "<div class='form-group'><center><label for='exampleFormControlTextarea1'><p class='text-primary'>Decrypting Value of enc(x)+7:</p></label></center><center><input type='text' class='form-control' id='value1' style='text-align:center'  value='%s'/></center></div>"%(z_add_const_P)
print "</form>"


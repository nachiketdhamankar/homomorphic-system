<html>
<head>
<title>Login Page</title>
</head>
<body background="home.jpg" width="500" height="500">
<form name="loginForm" method="post" action="action1.php"><br><br><br><br><br><br><br><br><br><br>
<table width="20%" bgcolor="gold" align="center">

<tr>
<td colspan=2><center><font size=4><b>Login Page</b></font></center></td>
</tr>

<tr>
<td>Username:</td>
<td><input type="text" size=25 name="uname"></td>
</tr>

<tr>
<td>Password:</td>
<td><input type="Password" size=25 name="pass"></td>
</tr>

<tr>
<td ><input type="Reset"></td>
<td><input type="submit" onclick="return check(this.form)" value="Login"></td>
</tr>

</table>
</form>
<script language="javascript">
function check(form)
{

if(form.userid.value == "" && form.pwd.value == "")
{
	alert("Enter Username or Password")
}
else
{
	alert("Error Password or Username")
	return false;
}
}
</script>

</body>
</html>
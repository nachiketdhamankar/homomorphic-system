<?php

$con=mysql_connect("localhost","root","");
mysql_select_db("homomorphic",$con);	

$u=$_POST['uname'];
$p=$_POST['pass'];

$query="select * from tblreg where username='$u' and password='$p'";
$res=mysql_query($query);

if(mysql_num_rows($res)>0)
{

   $_SESSION['user']=$u;
	/*echo "<script>alert('Login Successfull');
			window.location='home.php'</script>";*/
			 header("location:login.php");
}
else{
	echo "<script>alert('Invalid Username Password');
			window.location='login.php'</script>";
}

?>
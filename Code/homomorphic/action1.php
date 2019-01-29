<?php
session_start();
$con=mysql_connect("localhost","root","");
mysql_select_db("homomorphic",$con);	

$u=$_POST['uname'];
$p=$_POST['pass'];

echo $u;
echo $p;

  $query="select * from tblreg where username='$u' and password='$p'";
        $res=mysql_query($query);

        if(mysql_num_rows($res)>0)
        { 

            $_SESSION['user']=$u;
            header("location:home.php");
        }
         else
             {
				 echo "<script> alert('Invalid Credentials');
								window.location.href='index.php' </script>";
                 //header("location:index.php?msg=Invalid Username/Password");
             }

?>
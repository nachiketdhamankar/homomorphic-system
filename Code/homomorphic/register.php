<html>
<head>
<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
  <script>
  $('#password, #confirm_password').on('keyup', function () {
  if ($('#password').val() == $('#confirm_password').val()) {
    $('#message').html('Matching').css('color', 'green');
  } else 
    $('#message').html('Not Matching').css('color', 'red');
});
  </script>
</head>
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="index.php">Simple Banking Demo</a>
    </div>
    <ul class="nav navbar-nav">
      <li ><a href="index.php">Login</a></li>
      <!--<li><a href="index.php">Login</a></li>-->
      <li class="active"><a href="register.php">Register</a></li>
    </ul>
  </div>
</nav>
<?php
  $conn=mysql_connect("localhost","root","");
  mysql_select_db("homomorphic",$conn);
  $q="select max(accno) as acc from tbldec";
  $r=mysql_query($q);
  $row=mysql_fetch_assoc($r);
  $ac=$row['acc'];
  if($ac<1){
	  $ac = 1;
  }
  
?>
<form name="frmRegistration" method="post" action="reg.py">
	<table border="0" width="400" align="center" class="demo-table">
		<?php if(!empty($success_message)) { ?>	
		<div class="success-message"><?php if(isset($success_message)) echo $success_message; ?></div>
		<?php } ?>
		<?php if(!empty($error_message)) { ?>	
		<div class="error-message"><?php if(isset($error_message)) echo $error_message; ?></div>
		<?php } ?>
		<tr>
			<td >User Name</td>
			<td><input type="text" class="demoInputBox" name="userName" value="" placeholder="Only lowercase letters" required pattern="[a-z]{1,15}"
        title="Username should only contain lowercase letters. e.g. john"></td>
		</tr>
		<tr>
			<td>First Name</td>
			<td><input type="text" class="demoInputBox" name="firstName" placeholder="First Name"  title="Only Character" required></td>
		</tr>
		<tr>
			<td>Last Name</td>
			<td><input type="text" class="demoInputBox" name="lastName" placeholder="Last Name"  title="Only Character" required></td>
		</tr>
		<tr>
			<td>Password</td>
			<td><input type="password" class="demoInputBox"  id="password" name="password" placeholder="Password" required></td>
		</tr>
		<tr>
			<td>Confirm Password</td>
			<td><input type="password" class="demoInputBox" id="confirm_password" name="confirm_password" placeholder="Confirm Password" required></td>
		</tr>
		<tr>
			<td>Email</td>
			<td><input type="Email" class="demoInputBox" name="userEmail" placeholder="Email" required></td>
		</tr>
		<tr>
			<td>Gender</td>
			<td><input type="radio" name="gender" value="Male" <?php if(isset($_POST['gender']) && $_POST['gender']=="Male") { ?>checked<?php  } ?>> Male
			<input type="radio" name="gender" value="Female" <?php if(isset($_POST['gender']) && $_POST['gender']=="Female") { ?>checked<?php  } ?>> Female
			</td>
		</tr>
		<tr>
			<td>Account No</td>
			<td><input type="text" class="demoInputBox" name="accNo" placeholder="Account No"  required></td>
		</tr>
		
		<tr>
			<td colspan=2>
			 <input type="submit" name="register-user" value="Register" class="btnRegister"></td>
		</tr>
	</table>
</form>
<style>
.error-message {
	padding: 7px 10px;
	background: #fff1f2;
	border: #ffd5da 1px solid;
	color: #d6001c;
	border-radius: 4px;
}
.success-message {
	padding: 7px 10px;
	background: #cae0c4;
	border: #c3d0b5 1px solid;
	color: #027506;
	border-radius: 4px;
}
.demo-table {
	background: #d9eeff;
	width: 100%;
	border-spacing: initial;
	margin-top: -5%;
	word-break: break-word;
	table-layout: auto;
	line-height: 1em;
	color: #333;
	border-radius: 4px;
	/*padding: 20px 40px;*/
	text-align:center;
}
.demo-table td {
	padding: 15px 0px;
}
.demoInputBox {
	padding: 10px 30px;
	border: #a9a9a9 1px solid;
	border-radius: 4px;
}
.btnRegister {
	padding: 10px 30px;
	background-color: #3367b2;
	border: 0;
	color: #FFF;
	cursor: pointer;
	border-radius: 4px;
	margin-left: -15%;
}
</style>
</html>
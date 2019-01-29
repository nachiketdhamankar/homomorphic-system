<!DOCTYPE html>
<html lang="en">
<head>
  <title>Homomorphic</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
  <style>
	#welcome
	{
		text-align: center;
		font-size: 200%;
		padding: 2%
	}
	#toDo
	{
		text-align: center;
		font-size: 120%;
		text-decoration:none;
		margin: 1.5%;
	}
	.btn-xl {
    padding: 10px 20px;
    font-size: 20px;
    border-radius: 10px;
    width:35%;    //Specify your width here
	}
	.logout
	{
		font-weight:bold;
	}
</style>
</head>
<body>
<?php

$conn=mysql_connect("localhost","root","");
session_start();
if($_SESSION['user']=="")
{
    header("location:index.php");
}
$u=$_SESSION['user'];

?>

<nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <a class="nav-link" href="#">Home</a>
            </li>
        </ul>
    </div>
    <div class="mx-auto order-0">
        <a class="navbar-brand mx-auto" href="#">Homomorphic Encryption</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".dual-collapse2">
            <span class="navbar-toggler-icon"></span>
        </button>
    </div>
    <div class="navbar-collapse collapse w-100 order-3 dual-collapse2">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link logout" href="logout.php">Logout</a>
            </li>
        </ul>
    </div>
</nav>

<?php
  echo "<div id=\"welcome\">Welcome, $u</div>";
?>
<div id="welcome">
	What would you like to do today?
</div>

<br/>

	<div id="toDo">
		<a href="view.py?user=<?php echo $u ?>">
			<button type="button" class="btn btn-success btn-xl">View Account Details</button>
		</a>
	</div>
	<div  id="toDo">
		<a href="deposite.py?user=<?php echo $u ?>">
			<button type="button" class="btn btn-primary btn-xl">Deposit</button>
		</a>
	</div>
</body>
</html>

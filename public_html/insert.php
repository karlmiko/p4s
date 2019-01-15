<?php
    
$to = "parkflowco@gmail.com";
$subject = "New student registration";
$txt = filter_input(INPUT_POST, 'firstname');
$headers = "From: Parking4Students.com";
mail($to,$subject,$txt,$headers);


mysql_connect("www.parkflow.space","main","password");
mysql_select_db("test");



if (mysql_connect_error()) {

	die('Connect error');
}
else {

	sql = "INSERT INTO tbName (firstName) VALUES ('$txt')";

	if ($con->query($sql)) {
		header('Location: success_student.html');
		exit;
	}
	$con->close()
}

?>
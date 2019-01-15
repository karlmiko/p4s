<?php

$connection = mysqli_connect ('localhost','main','password', 'test');

if (mysqli_connect_error()) {
    
    die("There was an error connecting to the database.")
};
else {echo ("connection successful")};

$name = $_POST ['firstname'];
$email = $_POST ['email'];

$query = "INSERT INTO users('name', 'email')

VALUES

('$name','$email')";

mysqli_query($connection, $query);
    
Echo "Database Saved"; 
mysql_close($connection);

?>
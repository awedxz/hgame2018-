<?php
error_reporting(0);

$db_host = 'localhost';
$db_name = 'users';
$db_user = 'root';
$db_pwd = '';

$conn = mysqli_connect($db_host, $db_user, $db_pwd, $db_name);

if(!$conn){
    die(mysqli_connect_error());
}

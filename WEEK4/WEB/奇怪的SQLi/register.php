<?php
error_reporting(0);

include('config.php');

$username = addslashes($_POST['username']);
$password = addslashes($_POST['password']);

if ($username == NULL || $password == NULL) {
    die("");
} else {
    $sql = "insert into user values(NULL, '{$username}', '{$password}')";
    $re = mysqli_query($conn, $sql);
    if ($re) {
        echo 'success';
        header('Location: login.html');
    }
}





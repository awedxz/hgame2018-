<?php
error_reporting(0);

session_start();

$_SESSION['login'] = 0;

include('config.php');

$username = addslashes($_POST['username']);
$password = addslashes($_POST['password']);

if ($username == NULL || $password == NULL) {
    die("");
} else {
    $sql = "select * from user where username = '{$username}'";
    $re = mysqli_query($conn, $sql);
    $rs = mysqli_fetch_array($re);
    if ($rs['password'] === $password) {
        $_SESSION['login'] = 1;
        echo 'success';
        header('Location: index.html');
    } else {
        echo 'error';
    }
}


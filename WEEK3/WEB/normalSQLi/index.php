<?php
error_reporting(0);

$db_host = 'mysql';
$db_name = 'users';
$db_user = 'hgame';
$db_pwd = '';

$conn = mysqli_connect($db_host, $db_user, $db_pwd, $db_name);

if(!$conn){
    die(mysqli_connect_error());
}

setcookie("name", base64_encode('guest'));

$username = base64_decode($_COOKIE['name']);

if (strstr($_SERVER['HTTP_USER_AGENT'], 'sqlmap')) {
    die("something error");
}

$sql = "select * from user where username = '{$username}'";
$re = mysqli_query($conn, $sql);
$rs = mysqli_fetch_array($re);

// echo $rs['flag'];
echo "hello" . $username . '<br/>';
echo "因为出题人太懒了，所以现在没有任何功能";

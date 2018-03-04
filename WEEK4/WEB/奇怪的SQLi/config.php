<?php
error_reporting(0);
// 题目是线上改的 下面是凭印象复原的
$db_host = 'mysql';
$db_name = 'users';
$db_user = 'week4';
$db_pwd = '';

$conn = mysqli_connect($db_host, $db_user, $db_pwd, $db_name);

if(!$conn){
    die(mysqli_connect_error());
}

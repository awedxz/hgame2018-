<?php
error_reporting(0);

session_start();

if ($_SESSION['login'] != 1) {
    die("you need login\n");
}

if ($_POST['url']) {
    $url = $_POST['url'];

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HEADER, 0);

    curl_exec($ch);

    curl_close($ch);
}
?>
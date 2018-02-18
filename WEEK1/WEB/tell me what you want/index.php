<form action="index.php" method="get">
    tell me what you want : <input name="want" type="text">
    <input type="submit" value="submit">
</from>
<?php
error_reporting(0);
echo "<br/>";
setcookie("isadmin", 0);
// var_dump($_SERVER);
if (isset($_GET['want']) || isset($_POST['want'])) {
    if (!isset($_POST['want'])) {
        die("request method is error.I think POST is better");
    } 

    if ($_SERVER['HTTP_X_FORWARDED_FOR'] != '127.0.0.1') {
        echo "https://www.wikiwand.com/en/X-Forwarded-For<br/>";
        die("only localhost can get flag");
    }
    
    // Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
    if (!strpos($_SERVER['HTTP_USER_AGENT'], 'Icefox/57.0')) {
        echo "https://www.wikiwand.com/en/User_agent<br/>";
        die("please use Icefox/57.0");
    }
    
    if ($_SERVER['HTTP_REFERER'] != 'www.google.com') {
        echo "https://www.wikiwand.com/en/HTTP_referer<br/>";
        die("the requests should referer from www.google.com");
    }

    if (isset($_SERVER['HTTP_COOKIE']) && $_SERVER['HTTP_COOKIE'] == "isadmin=0") {
        echo "https://www.wikiwand.com/en/HTTP_cookie<br/>";
        die("you are not admin");
    }
    
    echo "hgame{For9e_hTTp_iS_N0T_HArd}";
}


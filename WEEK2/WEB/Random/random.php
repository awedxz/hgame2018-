<?php
error_reporting(0);
include ('flag.php');

class emmm
{
    var $public;
    var $secret;
}

if ($_GET['emmm']) {
    $emmm = unserialize($_GET['emmm']);
    var_dump($emmm);
    var_dump(is_object($emmm));
    if (!is_object($emmm)) {
        die("error");
    }
    $emmm->public = random_int(0, 100000000);
    $emmm->secret = random_int(0, 100000000);
    if ($emmm->public == $emmm->secret) {
        echo $flag;
    }
}

highlight_file(__FILE__);



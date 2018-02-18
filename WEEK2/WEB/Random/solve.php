<?php
class emmm
{
    var $public;
    var $secret;

    public function __construct() {
        $this->public =& $this->secret;
    }
}

$a = new emmm;
echo serialize($a);
// O:4:"emmm":2:{s:6:"public";N;s:6:"secret";R:2;}

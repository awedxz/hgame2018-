<form action="index.php" method="get">
    give me your token : <input name="token" type="text">
    <input type="submit" value="submit">
</from>
<br/>
<?php
error_reporting(0);

define("key", "1qazxsw23edcvfr4");
define("method", "aes-128-cbc");
$flag = 'hgame{Oh_bad_paDDing#@!}';

function getRandomStr($length)
{
	$iv = '';
	for ($i = 0; $i < $length; $i++)
	{
		$iv .= chr(rand(1, 255));
	}
	return $iv;
}

function enc($plaintext)
{
	$iv = getRandomStr(16); 
	$c = openssl_encrypt((string)$plaintext, method, key, OPENSSL_RAW_DATA, $iv);
	return bin2hex($iv . $c);
}

function dec($ciphertext)
{
	$ciphertext = hex2bin($ciphertext);
	if ($iv = substr($ciphertext, 0, 16))
	{
		if ($c = substr($ciphertext, 16))
		{
			if ($plaintext = openssl_decrypt((string)$c, method, key, OPENSSL_RAW_DATA, $iv))
			{
				return $plaintext;
			}
			else
			{
				return "dec error";
			}
		}
	}
}

echo 'your token is: ' . enc(getRandomStr(16)) . '<br/>';
if ($_GET['token']) 
{
    if (dec($_GET['token']) === 'admin') {
        echo $flag;
    } else if (dec($_GET['token']) == 'dec error') {
		echo "decrypt error";
	} else {
		echo 'you are not admin, you cant get flag';
	}
}


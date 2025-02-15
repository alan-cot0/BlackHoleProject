<!DOCTYPE html>
<html>
<head>
<title>Python Scripts</title>
<?PHP
echo shell_exec("python test.py 'parameter1'");
?>
</head>
<body>
	<h3>[Temporary] Click to run Python scripts: </h3>
	<p>Script 1: <?php 
	$script1 = escapeshellcmd('test.py');
	$output = shell_exec($script1);
	echo $output;
?>
</body>
</html>
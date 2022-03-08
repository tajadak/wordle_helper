<?php
$formdata = array(
    // 'Included'=> $_POST['Included'],
    'Excluded'=> $_POST['Excluded'],
    '1'=> $_POST['1'],
    '2'=> $_POST['2'],
    '3'=> $_POST['3'],
    '4'=> $_POST['4'],
    '5'=> $_POST['5'],
    'a'=> $_POST['a'],
    'b'=> $_POST['b'],
    'c'=> $_POST['c'],
    'd'=> $_POST['d'],
    'e'=> $_POST['e']
);
$jsondata = json_encode($formdata, JSON_PRETTY_PRINT);

file_put_contents("assets/conditions.json", $jsondata);
$command = escapeshellcmd('./wordle.py');

$output = shell_exec($command);
echo '<span style="font-size:2.00em;color:blue;">'.$output.'</span>';

?>


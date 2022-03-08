
<html>
<head>
<title>Wordle Helper</title>
<style type="text/css">
textarea {
width: 150px;
height: 5em;
}
input, select, textarea {
font-size: 150%;
width: 200px;
}
</style>
</head>
<body>
<h1 style="font-size:25">
<form target="_blank" action="wordle_results.php" method="post">
 <!-- Included: <input type="text" name="Included" id="Included" /><br /> -->
 Excluded Letters: <input type="text" name="Excluded" id="Excluded" /><br />
 Correct Letter Pos 1: <input type="text" name="1" id="1" /><br />
 Correct Letter Pos 2: <input type="text" name="2" id="2" /><br />
 Correct Letter Pos 3: <input type="text" name="3" id="3" /><br />
 Correct Letter Pos 4: <input type="text" name="4" id="4" /><br />
 Correct Letter Pos 5: <input type="text" name="5" id="5" /><br />
 Included Letters Not in Pos 1: <input type="text" name="a" id="a" /><br />
 Included Letters Not in Pos 2: <input type="text" name="b" id="b" /><br />
 Included Letters Not in Pos 3: <input type="text" name="c" id="c" /><br />
 Included Letters Not in Pos 4: <input type="text" name="d" id="d" /><br />
 Included Letters Not in Pos 5: <input type="text" name="e" id="e" /><br />
 <input type="submit" id="submit" value="Get Words" />
</h1>
</form>
</body>
</html>
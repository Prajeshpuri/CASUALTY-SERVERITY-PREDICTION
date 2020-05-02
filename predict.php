<?php
$vehicle = $_GET["vehicle"];
$surface = $_GET["surface"];
$light = $_GET["light"];
$weather = $_GET["weather"];
$victim = $_GET["victim"];
$sex = $_GET["sex"];
$age = $_GET["age"];
$type = $_GET["type"];

// Execute the model
system("/usr/anaconda/bin/python3 casualty_severity_prediction_model.py ".$vehicle." ".$surface." ".$light." ".$weather." ".$victim." ".$sex." ".$age." ".$type." 2>&1");    
?>

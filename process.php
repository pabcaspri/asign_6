<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $numbers = $_POST['numbers'];
    $threshold = $_POST['threshold'];

    $command = escapeshellcmd("python3 bitwise_operations.py '" . json_encode(['numbers' => $numbers, 'threshold' => $threshold]) . "'");
    $output = shell_exec($command);

    echo "<pre>Result: $output</pre>";
}
?>

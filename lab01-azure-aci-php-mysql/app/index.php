<!DOCTYPE html>
<html>
<head>
<style>
table, th, td { border: 1px solid black; }
</style>
</head>
<body>
<?php
ini_set('display_errors', 1); ini_set('display_startup_errors', 1); error_reporting(E_ALL);
$servername = "mysql512.b0hqc5cue7bfapbf.canadaeast.azurecontainer.io";
$username = "root";
$password = "mysql-secret-pwd";
$dbname = "ecommerce";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}
$sql = "SELECT client_id, client_fname, client_lname, client_email FROM ecommerce.clients";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
echo "<table><tr><th>ID Client</th><th>First name and Last name</th><th>Email Address</th></tr>";
// output data of each row
while($row = $result->fetch_assoc()) {
echo "<tr><td>" . $row["client_id"]. "</td><td>" . $row["client_fname"]. " " . $row["client_lname"]. "</td><td>" . $row["client_email"]. "</td></tr>";
}
echo "</table>";
} else {
echo "0 results";
}
$conn->close();
?>
</body>
</html>

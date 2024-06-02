<?php
$servername = "localhost";
$username = "er1xyz_recone";
$password = "RT%;_#jyYqfK";
$dbname = "er1xyz_recone";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Error" . $conn->connect_error);
}

$link = "";
if (isset($_GET['link'])) {
    $link = htmlspecialchars(mysqli_real_escape_string($conn, $_GET['link']));
}

$port = "";
if (isset($_GET['port'])) {
    $port = htmlspecialchars(mysqli_real_escape_string($conn, $_GET['port']));
}

$title = "";
if (isset($_GET['title'])) {
    $title = htmlspecialchars(mysqli_real_escape_string($conn, $_GET['title']));
}

$status = "";
if (isset($_GET['status'])) {
    $status = htmlspecialchars(mysqli_real_escape_string($conn, $_GET['status']));
}

$subdomain = "";
if (isset($_GET['subdomain'])) {
    $subdomain = htmlspecialchars(mysqli_real_escape_string($conn, $_GET['subdomain']));
}

$wapplayzer = "";
if (isset($_GET['wapplayzer'])) {
    $wapplayzer = htmlspecialchars(mysqli_real_escape_string($conn, $_GET['wapplayzer']));
}

$whois = "";
if (isset($_GET['whois'])) {
    $whois = htmlspecialchars(mysqli_real_escape_string($conn, $_GET['whois']));
}

$regex = "";
if (isset($_GET['regex'])) {
    $regex = htmlspecialchars(mysqli_real_escape_string($conn, $_GET['regex']));
}

$query = "INSERT INTO user (link, port, title, status, subdomain, wapplayzer, whois, regex) VALUES ('$link', '$port', '$title', '$status', '$subdomain', '$wapplayzer', '$whois', '$regex')";

if ($conn->query($query) === TRUE) {
    echo json_encode(["result" => "ok"]);
} else {
    echo json_encode(["result" => "Error","Error" => "$conn->error"]);
}

$conn->close();
?>

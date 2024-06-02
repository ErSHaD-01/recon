<?php
$servername = "localhost";
$username = "er1xyz_recone";
$password = "RT%;_#jyYqfK";
$dbname = "er1xyz_recone";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Error" . $conn->connect_error);
}

$sql = "SELECT id, link, port, title, status, subdomain, wapplayzer, whois, regex FROM user";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<style>
    body {
        background-color: #212121;
        color: #fff;
    }

    table {
    width: 50%;
    border-collapse: collapse;
    margin: 50px 0;
    font-size: 18px;
    text-align: left;
}

table, th, td {
    border: 1px solid #acacac;
}

th, td {
    padding: 12px;
}

th {
    background-color: #565656;
}

td {
    background-color: #333;
}

button {
    padding: 8px 16px;
    margin: 5px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

</style>
<body>

<center><h2>Recon</h2>

<table>
    <tr>
        <th>ID</th>
        <th>Link</th>
        <th>Port</th>
        <th>Title</th>
        <th>status</th>
        <th>subdomain</th>
        <th>wapplazer</th>
        <th>whois</th>
        <th>regex</th>
    </tr>
    <?php
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "<tr>
                    <td>" . $row["id"]. "</td>
                    <td>" . $row["link"]. "</td>
                    <td>" . $row["port"]. "</td>
                    <td>" . $row["title"]. "</td>
                    <td>" . $row["status"]. "</td>
                    <td>" . $row["subdomain"]. "</td>
                    <td>" . $row["wapplayzer"]. "</td>
                    <td>" . $row["whois"]. "</td>
                    <td>" . $row["regex"]. "</td>
                  </tr>";
        }
    } else {
        echo "<tr><td colspan='3'>هیچ داده‌ای یافت نشد</td></tr>";
    }
    $conn->close();
    ?>
</table>
</center>
</body>
</html>

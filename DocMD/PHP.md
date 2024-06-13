# PHP

## Conceitos

## Conectar a um banco de dados MySQL local (Mysqli)

```php
    $serverName = "localhost:3306";
    $userName = "caio";
    $password = "";
    $db = "gerbd";

    $connect = new mysqli($serverName, $userName, $password, $db);

    if ($connect->connect_error) {
        echo "Connection Failed";
        die("Connection Failed: " . $connect->connect_error);
    }

    $sql = "SELECT cod_barra FROM produtos";
    $res = mysqli_query($connect, $sql); # $res é um array
```

## Requisição de API com curl

```php
$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "https://api.gestaoclick.com/clientes");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($ch, CURLOPT_HEADER, FALSE);

// Header:
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "Content-Type: application/json",
    "access-token: c30c81e9b3b337ab6fe8ecdb9e3e9bfda0b8a193",
    "secret-access-token: bd2ae4e231cdd80b049987c1fb0e87f91da364d2"
));

$response = curl_exec($ch);
// Checa retorno de erro:
if(curl_errno($ch)) {
    echo 'curl error: ' . curl_error($ch);
} else {
    echo $response;
}

curl_close($ch);

var_dump($response);
```

## Abrindo DB usando PDO

```php
$db = new PDO('mysql:host=localhost:3306;dbname=gerbd', $userName, $password);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Utilização do DB

$db = null; // Fecha a conexão com o banco de dados
```

## Fetch em DB usando PDO

```php
$sql = "SELECT * FROM Table";
$stmt = $db->prepare($sql);
$stmt->execute();
$result = $stmt->setFetchMode(PDO::FETCH_NUM);
$response = $stmt->fetchAll();
```

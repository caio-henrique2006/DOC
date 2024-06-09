# PHP

## Conceitos

## Conectar a um banco de dados MySQL local

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

##

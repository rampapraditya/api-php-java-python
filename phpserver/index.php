<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = json_decode(file_get_contents("php://input"), true);
    $a = $input["a"] ?? 0;
    $b = $input["b"] ?? 0;
    $sum = $a + $b;

    echo json_encode(["result" => $sum]);
} else {
    http_response_code(405);
    echo json_encode(["error" => "Only POST method is allowed"]);
}

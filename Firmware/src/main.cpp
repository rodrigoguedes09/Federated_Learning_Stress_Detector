#include <Arduino.h>
#include "NeuralNetwork.h"
#include "model_data.h"

#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <rBase64.h>

NeuralNetwork* nn;

const char* ssid = "custodma_2G";
const char* password = "berserknd";
const char* serverUrl = "http://192.168.0.119:5001";
DynamicJsonDocument doc(2*converted_model_tflite_len);
String response;
HTTPClient http;
const char* modelb64 = NULL;
char* model = NULL;

uint8_t count = 10;

void setup()
{
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop()
{
  if (count == 10) {
    Serial.println("Atualizando Modelo");
    http.begin(String(serverUrl) + "/model");
    int httpResponseCode = http.GET();
    
    if (httpResponseCode == HTTP_CODE_OK) {
      response = http.getString();
      deserializeJson(doc, String(response));
      modelb64 = doc["model_encoded"];
      rbase64.decode(modelb64);
      model = rbase64.result();
      delete[] nn;
      nn = NULL;
      nn = new NeuralNetwork(model);
    } else {
      Serial.print("Error sending data. HTTP response code: ");
      Serial.println(httpResponseCode);
    }
    count = 0;
  }
  

  float number1 = random(100) / 100.0;
  float number2 = random(100) / 100.0;

  nn->getInputBuffer()[0] = number1;
  nn->getInputBuffer()[1] = number2;

  float result = nn->predict();

  const char *expected = number2 > number1 ? "True" : "False";

  const char *predicted = result > 0.5 ? "True" : "False";

  Serial.printf("%.2f %.2f - result %.2f - Expected %s, Predicted %s\n", number1, number2, result, expected, predicted);

  http.begin(String(serverUrl) + "/data");
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(String("{\"number1\": " + String(number1) + ", \"number2\": " + String(number2) + ", \"result\": " + String(result) + "}"));
  if (httpResponseCode == HTTP_CODE_OK) {
    response = http.getString();
    Serial.println(response);
  } else {
    Serial.print("Error sending data. HTTP response code: ");
    Serial.println(httpResponseCode);
  }

  delay(10000);
  count++;
}
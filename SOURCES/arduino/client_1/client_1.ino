#include <ESP8266WiFi.h>
#include <PubSubClient.h>
//http://arduino.esp8266.com/stable/package_esp8266com_index.json
// Change the credentials below, so your ESP8266 connects to your router
const char* ssid          = "IZZI-9146";      // RED DE INTERNET
const char* password      = "F82DC0169146";   // CONTRASEÑA
const char* mqtt_server   = "192.168.0.11";    // IP adress Raspberry Pi

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg1[50];
char msg2[50];
char msg3[50];
char msg4[50];

int value = 0;


char message[100];
 
void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}
 
void setup_wifi() {
 
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
 
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
 
  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }
 
}
 
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("mesa1");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
 double randomDouble(double minf, double maxf)
{
  return minf + random(1UL << 31) * (maxf - minf) / (1UL << 31);  // use 1ULL<<63 for max double values)
}
void loop() {
 
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
 
  long now = millis();
  if (now - lastMsg > 1000) {
    lastMsg = now;

  float temp1 = randomDouble(35.00, 39.00);
    float temp2 = randomDouble(35.00, 39.00);
      float temp3 = randomDouble(35.00, 39.00);
         int temp4 = 0 ;
    snprintf (msg1, 100," %4.2f",temp1);
    snprintf (msg2, 100," %4.2f",temp2);
    snprintf (msg3, 100," %4.2f",temp3);
    snprintf (msg4, 100," %d",temp4);
    Serial.println("Publish message: ");
    Serial.println(msg1);
    Serial.println(msg2);
    Serial.println(msg3);
    Serial.println(msg4);
    Serial.println(" ");

    
    client.publish("esp32/temperature", msg1);
    client.publish("esp32/humedad", msg2);
    client.publish("esp32/corriente", msg3);
    client.publish("esp32/motor", msg4);
  }
}

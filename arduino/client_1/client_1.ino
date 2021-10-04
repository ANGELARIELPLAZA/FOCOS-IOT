#include <ESP8266WiFi.h>
#include <PubSubClient.h>
/* 
CODIGO PARA VERIFICAR PINES DE ESP8266 Y D1 MINI
D0=16  D1=5  D2=4  D3=0  D4=2  
D5=14  D6=12 D7=13 D8=15 
*/

//LED Connections
const int bluepin  = 2; // D4
const int redpin   = 4; // D2
const int greenpin = 0; // D3


// Change the credentials below, so your ESP8266 connects to your router
const char* ssid          = "IZZI-9146";      // RED DE INTERNET
const char* password      = "F82DC0169146";   // CONTRASEÑA
const char* mqtt_server   = "192.168.0.13";    // IP adress Raspberry Pi

WiFiClient espClient;
PubSubClient client(espClient);

unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("ESTABLECIENDO RED ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WIFI CONECTADO");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Mensaje recibido [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  //  if ((char)payload[0] == '1') {
  //    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
  //    // but actually the LED is on; this is because
  //    // it is active low on the ESP-01)
  //  } else {
  //    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  //  }

  //SI EL DATO DE ENTRADA ES 1 EJECUTA LO DE SU INTERIOR
  if ((char)payload[0] == '1' )
  {
    RGB_color(255, 0, 0); // Red
    Serial.println("rojo");
    Serial.println("-----------------------");
  }
 
  //SI EL DATO DE ENTRADA ES 2 EJECUTA LO DE SU INTERIOR
  if ((char)payload[0] == '2' )
  {
    RGB_color(0, 255, 0); // Green
    Serial.println("verde");
    Serial.println("-----------------------");
  }

  //SI EL DATO DE ENTRADA ES 3 EJECUTA LO DE SU INTERIOR
  if ((char)payload[0] == '3' )
  {
    RGB_color(0, 0, 255); // Blue
    Serial.println("azul");
    Serial.println("-----------------------");
  }

  //SI EL DATO DE ENTRADA ES 4 EJECUTA LO DE SU INTERIOR
  if ((char)payload[0] == '4' )
  {
    RGB_color(255, 0, 255); // Magenta
    Serial.println("magenta");
    Serial.println("-----------------------");
  }

  //SI EL DATO DE ENTRADA ES 5 EJECUTA LO DE SU INTERIOR
  if ((char)payload[0] == '5' )
  {
    RGB_color(255, 20, 0); // Yellow
    Serial.println("amarillo");
    Serial.println("-----------------------");
  }

  //SI EL DATO DE ENTRADA ES 6 EJECUTA LO DE SU INTERIOR
  if ((char)payload[0] == '6' )
  {
    RGB_color(255, 255, 255); // white
    Serial.println("blanco");
    Serial.println("-----------------------");
  }

  //SI EL DATO DE ENTRADA ES 0 EJECUTA LO DE SU INTERIOR
  if ((char)payload[0] == '0' )
  {
    RGB_color(0, 0, 0); // apagado
    Serial.println("apagar");
    Serial.println("-----------------------");
  }


}

void reconnect() {
  // BUCLE DE RECONECCION
  while (!client.connected()) {
    Serial.print("CONECTANDO CON MQTT ...");
    // Create a random client ID
    String clientId = "ESP8266Client";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("mesa1");                    //IDENTIFICADOR DE PLACA (TOPIC)
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" REINTENTANDO EN 5 SEGUNDOS");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
{
  analogWrite(redpin, red_light_value);
  analogWrite(greenpin, green_light_value);
  analogWrite(bluepin, blue_light_value);
}
void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  pinMode (redpin, OUTPUT);
  pinMode (bluepin, OUTPUT);
  pinMode (greenpin, OUTPUT);
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

    unsigned long now = millis();
    if (now - lastMsg > 2000) {
      lastMsg = now;
      ++value;
      snprintf (msg, MSG_BUFFER_SIZE, "hello world #%ld", value);
      Serial.print("Publish message: ");
      Serial.println(msg);
      client.publish("outTopic", msg);
    }
}

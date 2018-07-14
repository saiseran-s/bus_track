#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>
#include <Wiegand.h>
//MAC ID
byte mac[]    = {  0xDE, 0xED, 0xBA, 0xFE, 0xFE, 0xED };
IPAddress ip(192,168,2,28);
const char* server = "iot.eclipse.org";
EthernetClient ethClient;
PubSubClient client(ethClient);
// These are the pins connected to the Wiegand D0 and D1 signals.
#define PIN_D0 2
#define PIN_D1 3
// The object that handles the wiegand protocol
Wiegand wiegand;

// Initialize Wiegand reader
void setup() {
  Serial.begin(9600);

  //Install listeners and initialize Wiegand reader
  wiegand.onReceive(receivedData, "Card read: ");
  wiegand.onStateChange(stateChanged, "State changed: ");
  wiegand.begin(WIEGAND_LENGTH_AUTO);
  

  //initialize pins as INPUT
  pinMode(PIN_D0, INPUT);
  pinMode(PIN_D1, INPUT);
  Ethernet.begin(mac,ip);
  delay(1500);
  client.setServer(server,1883);
  
}

// Continuously checks for pending messages and polls updates from the wiegand inputs
void loop() {
  // Checks for pending messages 
  wiegand.flush();
  
  // Check for changes on the the wiegand input pins
  wiegand.setPin0State(digitalRead(PIN_D0));
  wiegand.setPin1State(digitalRead(PIN_D1));
  
}

// Notifies when a reader has been connected or disconnected.
// Instead of a message, the seconds parameter can be anything you want -- Whatever you specify on `wiegand.onStateChange()`
void stateChanged(bool plugged, const char* message) {
    Serial.print(message);
    Serial.println(plugged ? "CONNECTED" : "DISCONNECTED");
}

// Notifies when a card was read.
// Instead of a message, the seconds parameter can be anything you want -- Whatever you specify on `wiegand.onReceive()`
void receivedData(uint8_t* data, uint8_t bits, const char* message) {
    Serial.print(message);    

    String cardNo;

    char mesg[20];

    //Print value in HEX
    uint8_t bytes = (bits+7)/8;
    for (int i=0; i<bytes; i++) 
    {
//        Serial.print(data[i] >> 4, 16);/
        cardNo+= String(data[i] >> 4, 16);
//        Serial.print(data[i] & 0xF, 16);/
        cardNo+= String(data[i] & 0xF, 16);
        
    }
    Serial.println(cardNo);
    Serial.println();

    cardNo.toCharArray(mesg,20);
    client.publish("bT-card-req",mesg);  
    
    
    
}
  
  
  


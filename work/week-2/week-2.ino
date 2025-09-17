#define LED_BUILTIN 2
void setup() {

  Serial.begin(9600);
  
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  Serial.print("สวัสดี นวนนท์ กุสลานนท์\n");

  digitalWrite(LED_BUILTIN, 1);
  Serial.print("light ... "); 
  delay(1000);

  digitalWrite(LED_BUILTIN, 0);
  Serial.print("no light ... "); 
  delay(1000);
}
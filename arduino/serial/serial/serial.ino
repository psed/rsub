String consoleCommand;

void setup() 
{
  pinMode(13, OUTPUT);
  Serial.begin(115200); // use the same baud-rate as the python side
}

void loop() 
{
}

void serialEvent()
{
    while (Serial.available()) {
      char c = Serial.read();
      delay(10);
      consoleCommand += c;
      if (consoleCommand.endsWith(";"))
      {
        digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(10);              // wait for a second
        digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
        consoleCommand = "";
      }
   } 
  Serial.println("Hello world from Ardunio!"); // write a string
}

#define bp_a 8
#define bp_b 9
#define bp_c 10

#define VRX_PIN  A1 // Arduino pin connected to VRX pin
#define VRY_PIN  A0 // Arduino pin connected to VRY pin

int xValue = 0; // To store value of the X axis
int yValue = 0; // To store value of the Y axis

int bs_a = 0;
int bs_b = 0;
int bs_c = 0;
 

void setup() {
  pinMode(bp_a, INPUT_PULLUP);
  pinMode(bp_b, INPUT_PULLUP);
  pinMode(bp_c, INPUT_PULLUP);
  
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  xValue = analogRead(VRX_PIN);
  yValue = analogRead(VRY_PIN);

  int x = map(xValue, 0, 1023, 0, 9);
  int y = map(yValue, 0, 1023, 0, 9);
  
  Serial.print(x);
  Serial.print(y);
  Serial.print('\n');
  
  bs_a = digitalRead(bp_a);
  bs_b = digitalRead(bp_b);
  bs_c = digitalRead(bp_c);
  
  if (bs_a == 0){
    Serial.print('a');
  }
  if (bs_b == 0){
    Serial.print('b');
  }
  if (bs_c == 0){
    Serial.print('c');
  }
  delay(40);
}

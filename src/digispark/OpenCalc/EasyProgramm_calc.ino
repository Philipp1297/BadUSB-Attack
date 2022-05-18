#include "DigiKeyboardDe.h" 
  
void setup() {
  DigiKeyboardDe.delay(3000);
  DigiKeyboardDe.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboardDe.delay(200);
  DigiKeyboardDe.println("calc");
}

void loop() {
}

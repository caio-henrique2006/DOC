# Arduino


## Códigos:

### Uso geral
```cpp
// Incluir biblioteca
#include <Ultrasonic.h>
// Declarar variável
#define name A0 // Pino
int valor = 10;
// PinMode
pinMode(name, OUTPUT);
pinMode(name, INPUT);
// Serial
Serial.begin(9600);
Serial.print("Value:");
Serial.println(value);
// Delay
delay(1000) // Microsegundos. 1000 ms = 1 segundo
// Digital and Analog
digitalWrite(pin, value); // Value = 1 ou 0
analogWrite(pin, value); // Value = 0 até 1023
digitalRead(pin);
analogRead(pin);
```

### Buzzer
```cpp
tone(pin, value);
noTone(pin);
```
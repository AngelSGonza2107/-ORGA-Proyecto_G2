#include <Servo.h>  // incluye libreria de Servo
int posx1 = 2;
int posx2 = 3;
int posy1 = 4;
int posy2 = 5;
int forma1 = 6;
int forma2 = 7;

int INA1 = 8;   // pin digital 7 de Arduino a IN1 de modulo controlador
int INA2 = 9;   // pin digital 8 de Arduino a IN2 de modulo controlador
int INA3 = 10;  // pin digital 9 de Arduino a IN3 de modulo controlador    PINES STEPPER 1
int INA4 = 11;  // pin digital 10 de Arduino a IN4 de modulo controlador

int INB1 = 12;  // pin digital 7 de Arduino a IN1 de modulo controlador
int INB2 = 13;  // pin digital 8 de Arduino a IN2 de modulo controlador
int INB3 = 14;  // pin digital 9 de Arduino a IN3 de modulo controlador    PINES STEPPER 1
int INB4 = 15;  // pin digital 10 de Arduino a IN4 de modulo controlador



//int registro = 16;
//int pulsoRegistro = 17;
int ciclosCoordenadas = 16;

int pinServo = A5;
int PULSOMIN = 1000;  // pulso minimo en microsegundos
int PULSOMAX = 2000;  // pulso maximo en microsegundos

int seleccionColor1 = 0;
int seleccionColor2 = 0;

int seleccionPosx1 = 0;
int seleccionPosx2 = 0;

int seleccionPosy1 = 0;
int seleccionPosy2 = 0;

int seleccionForma1 = 0;
int seleccionForma2 = 0;

int ciclosPorCoordenada = 512;
int margen = ciclosPorCoordenada / 10;


int demora = 3;  // demora entre pasos, no debe ser menor a 10 ms.
// paso completo con maximo torque
int paso[4][4] =  // matriz (array bidimensional) con la secuencia de pasos
  {
    { 1, 1, 0, 0 },
    { 0, 1, 1, 0 },
    { 0, 0, 1, 1 },
    { 1, 0, 0, 1 }
  };

int pasoInv[4][4] =  // matriz (array bidimensional) con la secuencia de pasos, pero en orden inverso
  {
    { 1, 0, 0, 1 },
    { 0, 0, 1, 1 },
    { 0, 1, 1, 0 },
    { 1, 1, 0, 0 }
  };


Servo servo1;  // crea objeto
void setup() {
  pinMode(posx1, INPUT);
  pinMode(posx2, INPUT);
  pinMode(posy1, INPUT);
  pinMode(posy2, INPUT);
  pinMode(forma1, INPUT);
  pinMode(forma2, INPUT);
  // put your setup code here, to run once:
  pinMode(INA1, OUTPUT);    // todos los pines del stepper como salida pin 8
  pinMode(INA2, OUTPUT);    // pin 9
  pinMode(INA3, OUTPUT);    // pin 10
  pinMode(INA4, OUTPUT);    // pin 11
  digitalWrite(INA1, LOW);  // detiene
  digitalWrite(INA2, LOW);
  digitalWrite(INA3, LOW);
  digitalWrite(INA4, LOW);

  pinMode(INB1, OUTPUT);    // todos los pines del stepper como salida pin 12
  pinMode(INB2, OUTPUT);    // pin 13
  pinMode(INB3, OUTPUT);    // pin 14
  pinMode(INB4, OUTPUT);    // pin 15
  digitalWrite(INB1, LOW);  // detiene
  digitalWrite(INB2, LOW);
  digitalWrite(INB3, LOW);
  digitalWrite(INB4, LOW);

  pinMode(ciclosCoordenadas, OUTPUT);  // pin16

  servo1.attach(pinServo, PULSOMIN, PULSOMAX);  // inicializacion de servo PIN 18
  Serial.begin(9600);
}

void loop() {
  servo1.write(0);
 


  //SE MUEVE EN POSICION X

  digitalWrite(ciclosCoordenadas, HIGH);
  delay(20);
  digitalWrite(ciclosCoordenadas, LOW);
  if (seleccionPosx1 == LOW && seleccionPosx2 == HIGH) {
    for (int i = 0; i < ciclosPorCoordenada; i++)  // 512*4 = 2048 pasos
    {
      for (int j = 0; j < 4; j++)        // bucle recorre la matriz de a una fila por vez
      {                                  // para obtener los valores logicos a aplicar
        digitalWrite(INA1, paso[j][0]);  // a IN1, IN2, IN3 e IN4
        digitalWrite(INA2, paso[j][1]);
        digitalWrite(INA3, paso[j][2]);
        digitalWrite(INA4, paso[j][3]);
        delay(demora);
      }
    }
    digitalWrite(INA1, LOW);  // detiene
    digitalWrite(INA2, LOW);
    digitalWrite(INA3, LOW);
    digitalWrite(INA4, LOW);
  }

  if (seleccionPosx1 == HIGH) {
    for (int i = 0; i < ciclosPorCoordenada * 2; i++)  // 512*4 = 2048 pasos
    {
      for (int j = 0; j < 4; j++)        // bucle recorre la matriz de a una fila por vez
      {                                  // para obtener los valores logicos a aplicar
        digitalWrite(INA1, paso[j][0]);  // a IN1, IN2, IN3 e IN4
        digitalWrite(INA2, paso[j][1]);
        digitalWrite(INA3, paso[j][2]);
        digitalWrite(INA4, paso[j][3]);
        delay(demora);
      }
    }
    digitalWrite(INA1, LOW);  // detiene
    digitalWrite(INA2, LOW);
    digitalWrite(INA3, LOW);
    digitalWrite(INA4, LOW);
  }


  seleccionPosy1 = digitalRead(posy1);
  seleccionPosy2 = digitalRead(posy2);

  //SE MUEVE EN POSICION Y

  digitalWrite(ciclosCoordenadas, HIGH);
  delay(20);
  digitalWrite(ciclosCoordenadas, LOW);
  if (seleccionPosy1 == LOW && seleccionPosy2 == HIGH) {
    for (int i = 0; i < ciclosPorCoordenada; i++)  // 512*4 = 2048 pasos
    {
      for (int j = 0; j < 4; j++)        // bucle recorre la matriz de a una fila por vez
      {                                  // para obtener los valores logicos a aplicar
        digitalWrite(INB1, paso[j][0]);  // a IN1, IN2, IN3 e IN4
        digitalWrite(INB2, paso[j][1]);
        digitalWrite(INB3, paso[j][2]);
        digitalWrite(INB4, paso[j][3]);
        delay(demora);
      }
    }
    digitalWrite(INB1, LOW);  // detiene
    digitalWrite(INB2, LOW);
    digitalWrite(INB3, LOW);
    digitalWrite(INB4, LOW);
  }

  if (seleccionPosy1 == HIGH) {
    for (int i = 0; i < ciclosPorCoordenada * 2; i++)  // 512*4 = 2048 pasos
    {
      for (int j = 0; j < 4; j++)        // bucle recorre la matriz de a una fila por vez
      {                                  // para obtener los valores logicos a aplicar
        digitalWrite(INB1, paso[j][0]);  // a IN1, IN2, IN3 e IN4
        digitalWrite(INB2, paso[j][1]);
        digitalWrite(INB3, paso[j][2]);
        digitalWrite(INB4, paso[j][3]);
        delay(demora);
      }
    }
    digitalWrite(INB1, LOW);  // detiene
    digitalWrite(INB2, LOW);
    digitalWrite(INB3, LOW);
    digitalWrite(INB4, LOW);
  }

  // -------------------DIBUJO DE FORMAS------------------------------------------

  seleccionForma1 = digitalRead(forma1);  // lectura de estado de señal de forma 1
  seleccionForma2 = digitalRead(forma2);  // lectura de estado de señal de forma 2

  // put your main code here, to run repeatedly:
  //PULSO DIBUJO TERMINADO
  servo1.write(0);
  digitalWrite(ciclosCoordenadas, HIGH);
  delay(20);
  digitalWrite(ciclosCoordenadas, LOW);
  //REGRESA EN POSICION X

  if (seleccionPosx1 == LOW && seleccionPosx2 == HIGH) {
    moverIzq(ciclosPorCoordenada);
  }

  if (seleccionPosx1 == HIGH) {
    moverIzq(ciclosPorCoordenada * 2);
  }

  //REGRESA EN POSICION Y

  if (seleccionPosy1 == LOW && seleccionPosy2 == HIGH) {
    moverArriba(ciclosPorCoordenada);
  }

  if (seleccionPosy1 == HIGH) {
    moverArriba(ciclosPorCoordenada * 2);
  }
  digitalWrite(ciclosCoordenadas, HIGH);
  delay(20);
  digitalWrite(ciclosCoordenadas, LOW);
}
void moverDer(int distancia) {
  for (int i = 0; i < distancia; i++)  // 512*4 = 2048 pasos
  {
    for (int j = 0; j < 4; j++)        // bucle recorre la matriz de a una fila por vez
    {                                  // para obtener los valores logicos a aplicar
      digitalWrite(INA1, paso[j][0]);  // a IN1, IN2, IN3 e IN4
      digitalWrite(INA2, paso[j][1]);
      digitalWrite(INA3, paso[j][2]);
      digitalWrite(INA4, paso[j][3]);
      delay(demora);
    }
  }
  digitalWrite(INA1, LOW);  // detiene
  digitalWrite(INA2, LOW);
  digitalWrite(INA3, LOW);
  digitalWrite(INA4, LOW);
}

void moverIzq(int distancia) {
  for (int i = 0; i < distancia; i++)  // 512*4 = 2048 pasos
  {
    for (int j = 0; j < 4; j++)           // bucle recorre la matriz de a una fila por vez
    {                                     // para obtener los valores logicos a aplicar
      digitalWrite(INA1, pasoInv[j][0]);  // a IN1, IN2, IN3 e IN4
      digitalWrite(INA2, pasoInv[j][1]);
      digitalWrite(INA3, pasoInv[j][2]);
      digitalWrite(INA4, pasoInv[j][3]);
      delay(demora);
    }
  }
  digitalWrite(INA1, LOW);  // detiene
  digitalWrite(INA2, LOW);
  digitalWrite(INA3, LOW);
  digitalWrite(INA4, LOW);
}

void moverAbajo(int distancia) {
  for (int i = 0; i < distancia; i++)  // 512*4 = 2048 pasos
  {
    for (int j = 0; j < 4; j++)        // bucle recorre la matriz de a una fila por vez
    {                                  // para obtener los valores logicos a aplicar
      digitalWrite(INB1, paso[j][0]);  // a IN1, IN2, IN3 e IN4
      digitalWrite(INB2, paso[j][1]);
      digitalWrite(INB3, paso[j][2]);
      digitalWrite(INB4, paso[j][3]);
      delay(demora);
    }
  }
  digitalWrite(INB1, LOW);  // detiene
  digitalWrite(INB2, LOW);
  digitalWrite(INB3, LOW);
  digitalWrite(INB4, LOW);
}

void moverArriba(int distancia) {
  for (int i = 0; i < distancia; i++)  // 512*4 = 2048 pasos
  {
    for (int j = 0; j < 4; j++)           // bucle recorre la matriz de a una fila por vez
    {                                     // para obtener los valores logicos a aplicar
      digitalWrite(INB1, pasoInv[j][0]);  // a IN1, IN2, IN3 e IN4
      digitalWrite(INB2, pasoInv[j][1]);
      digitalWrite(INB3, pasoInv[j][2]);
      digitalWrite(INB4, pasoInv[j][3]);
      delay(demora);
    }
  }
  digitalWrite(INB1, LOW);  // detiene
  digitalWrite(INB2, LOW);
  digitalWrite(INB3, LOW);
  digitalWrite(INB4, LOW);
}
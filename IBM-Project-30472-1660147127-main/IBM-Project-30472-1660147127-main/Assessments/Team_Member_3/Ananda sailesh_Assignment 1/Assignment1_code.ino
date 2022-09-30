//Assignment1
void setup()
{
  pinMode(12, OUTPUT);
  pinMode(2,OUTPUT);
}

void loop()
{
  int m=digitalRead(8);
  double a=analogRead(A1);
  double v=a/1024;
  double tvolt=v*5;
  double o=tvolt-0.5;
  double t=o*100;
  if(t>50)
  { 
  
   digitalWrite(2, HIGH);
  }
  else
  {
  
  digitalWrite(2, LOW);
  }
  if(m==1)
  {
  digitalWrite(12, HIGH);
  }
  else
  {
  digitalWrite(12, LOW);
  }
}

#include <cs50.h>
#include <stdio.h>

float add(float a, float b, char operador);

int main (void)
{
    
    float x = get_float ("Insira o valor de x:\n");
    char z = get_char ("Insira a Operação: (+,-,/,*)\n");
    float y = get_float ("Insira o valor de y\n"); 
    float c = add(x,y,z);
    printf ("Resultado : %.2f\n",c);
}
    float add(float a, float b,char operador){
     
     if (operador == '+') {    
        return a + b ;
     
    }
    else if (operador == '-') {
        return a - b;
       
    }
    else if (operador =='/') { 
        return a / b;
     
    }
    else if (operador =='*'){
        return a * b;
    }
    else {
            printf ("Operação Invalida!");
    }
  
    }

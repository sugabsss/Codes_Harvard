#include <cs50.h>
#include <stdio.h>

float lengths(float a,float b,float c);
int main (void){
    float x = get_float("valor de x:");
    float y = get_float("valor de y:");
    float z = get_float("valor de z:");
        float valid_triangle = lengths(x,y,z);
}
    float lengths(float a,float b,float c){
    if (a,b,c <= 0){
        printf("Número inválido!\n");        
    }
    else if (a + c < b){
        printf ("Valor Invalido\n");
    
    }
    }
    

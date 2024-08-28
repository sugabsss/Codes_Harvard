#include <cs50.h>
#include <stdio.h>

int main (void){
    int n = get_int("Quantos numeros quer mutiplicar?\n");
    number[n];
    number[0] = 1;
    if (n <= 0) {
        printf("Insira um valor maior que 0\n");
    }
    for (int i = 1; i < n; i++){
        number[i] = number[i - 1]* 2;       
    }
    for (int i = 0; i < n; i++) {
        printf("Valores: %i\n", number[i]);
        
    }

    return 0;
}
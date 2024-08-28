#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main (void){
    int numero = get_int("Selecione um Número:\n"); //Pergunta ao usuario o numero a ser selecionado
    if (numero < 1 || numero > 26){ // restrinção de letras
        printf("Apenas numero entre 1 - 26\n");
            return 1;
    }
    printf("\n");
    {
    char letra = 'a' + numero - 1;
    printf("Letra correspondente ao número %d: %c\n", numero, letra);// Transformando numeros em letras
}
    printf("\n");
    char letras[26];
        for (int i = 0; i < numero;i++){
            letras[i] = 'a' + i;
                printf("%c \n",letras[i]); // array de letras
        }
        printf("\n");
    int numeros[26];
        for (int i = 0; i < numero; i++){
            numeros[i] = '1' + i;
                    printf("%c \n",numeros[i]); // array de numeros
        }
           return 0;
}

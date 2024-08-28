#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main (void){

    string phrase = get_string("Enter with a phrase:");
    int tamanho = strlen(phrase);
    
    for (int i = 0; i < tamanho;i++ ){
        printf("Numero de letras:%c\n",phrase[i]);
}
}
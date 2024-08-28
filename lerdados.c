#include <stdio.h>
#include <stdlib.h>

int main (void){
    FILE *f;
    char str[100];
    f = fopen("./valor1.txt","w+");
    if (!f){
        printf("error file 404\n");
        return 1;   
    }
        
    fscanf(f,"%s\n",str);
    printf("Conteudo do arquivo%s\n",str);
    fclose(f);
        return 0; 
}
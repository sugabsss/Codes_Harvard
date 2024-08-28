#include <stdio.h>
#include <stdlib.h>

int main (void){
    FILE *f;
    f = fopen("./valor1.txt","w+");
    if (!f){
        printf("error file 404\n");
        return 1;   
    }
    
    fprintf(f,"texto feito em %d\n",2024);
    fclose(f);
        return 0; 
}
#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int height = get_int("Qual Altura?\n");
    int weight = get_int("Qual Largura?\n");    
    while (true){
    for (int i = 0;i < height;i++){  
     for (int j = 0;j < weight;j++){
            printf("#");         
}
            printf("\n");
}
}
}
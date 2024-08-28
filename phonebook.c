#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main (void)
{
    string names[] = {"Carter","Gabriel","Miguel"};
    string number[] = {"+55-97143-2343","+55-95163-8534","+55-95321-3213"};

    string name = get_string("Pesquise um nome:\n");
    for (int i = 0; i < 3;i++){
        if(strcmp (names[i],name)== 0){
            printf("Nome Encontrado:%s\n",names[i]);
                 printf("numero:%s\n",number[i]);
            return 0;

        }
    }
   printf("Nome Não encontrado\n");
   return 1;
}   
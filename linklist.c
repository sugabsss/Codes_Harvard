#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
    int number;
    struct node *next; //Um pointer para o proximo node da minha lista,criando uma lista encadeada;
}
node; //declarando o nome da minha struct;

int main (int argc, int argv[]){ //contagem de argumentos passados e um array de string para linhas de comando;
    
    //Memoria dos numeros;
    node *list = NULL; //Declara que a lista está vazia no começo;

    // Para cada linha de comando;
    for (int i = 1;i < argc; i++){ //começa no 1 visto que o 0 já e o nome do proprio programa argv [0];

        // Convertendo os argumentos de char para inteiro;
        int number = atoi(argv[1]);

        //Alocando memoria para um node novo;
        node *n = malloc(sizeof(node)); 

        //verifica se a alocação de memoria acabou caso retorna 1 (falha);
        if (n == NULL){ 
            return 1;
        }
        n->number = number; //atribuindo o valor da int number no campo number do node;
        n->next = NULL; //atribui o valor NULL indicando que o ultimo campo 'next' estara vazio;
        
        //caso a lista esteja vazia;
        if (list ==NULL){

        //um novo node se torna a lista inteira (cabeça da lista);
           list = n;
        }

        //Caso a lista já tenha numeros;
        else
        {
            //Percorrer os nodes começando do node (list) até o final da lista lembrando que tem que ser diferente de NULL;
            for(node *ptr = list; ptr != NULL; ptr-> next){

                //Declarando que chegou no final da lista;
                if (ptr->next == NULL){

                    //Anexando um novo node no final dessa lista;
                    ptr->next = n;
                    break; //quebrando o looping após o processo estiver completo;
                }
            }
        }
    }
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>

//Criando uma Lista encadeada;

typedef struct node{ //Lembrando que o typedef é  para que não seja necessario escrever todo o nome e apenas node;
    string frase;
    struct node *next;
}node;

#define LIST_SIZE 3

bool unload(node *list);
void visualizer(node *list);

int main (void){
    node *list = NULL; //Declarando que dentro de minha struct node tem uma lista com valor NULL;


    //Adicionando intens na lista;
    for(int i = 0;i < LIST_SIZE;i++){
        //Pedindo para o usuario adicionar uma frase na entrada;
        string frase = get_string("Drop your phase here:"); 

        node *n = malloc(sizeof(node));
        
        if (n == NULL){
            return 1;
        }
        n->frase = frase;
        n->next = NULL;
        
        n->next = list;
        list = n;
        //Visualizando a lista após a entrada de dados do usuario;
        visualizer(list);
    }
    //liberando a memoria que havia sido alocada;
    if (!unload(list)){
        printf("Erro ao liberar a lista.\n"); //Usado para definir que chegou ao final da lista
        return 1;
    }
    printf("liberando a lista");
    return 0;
}
bool unload(node *list){

    node *ptr = list;
    while (ptr != NULL){
        ptr = list->next;
        free(list);
        list = ptr;
    }
    return true;
}
void visualizer(node *list){
    printf("\n+-- Visualizador de Lista --+\n\n");
    for(node *ptr = list;ptr !=NULL;ptr = ptr->next)
    {
            printf("Frase:%s\nNext:-->%p\n",ptr->frase,(void*)ptr->next);
        }
}
    

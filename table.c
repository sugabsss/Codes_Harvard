#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>

//Criando uma Lista encadeada;

typedef struct node{ //Lembrando que o typedef é  para que não seja necessario escrever todo o nome e apenas node;
    string frase;
    struct node *next;
}node;

node *table[26];

int hash(string frase);
bool unload(node *list);
void visualizer(node *list);

int main(void){
    for(int i = 0;i < 3;i++){
        string frase = get_string("Insira uma nova frase:\n");
    if(frase[0] < 'A' || frase[26] > 'Z'){
        printf("Nome invalido!\n");
        return 1;
    }
    int bucket = hash(frase);
    printf("%s hashes para %i\n",frase,bucket);
}
}
int hash (string frase){
    return toupper(frase[0]) - 'A';
    //Deixando claro que as letras sejam em ordem alfabetica para que não tenha disordem;
}

bool unload(node *list){
    node *ptr = list;
    while(ptr != NULL){
        ptr = list->next;
        free(list);
        list = ptr;

    }
    return true;
}

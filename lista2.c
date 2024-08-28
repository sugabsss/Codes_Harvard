#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>

//Criando uma Lista encadeada;

typedef struct node{ //Lembrando que o typedef é  para que não seja necessario escrever todo o nome e apenas node;
    int number;
    struct node *next;
}node;

int main(void){
    node *head = malloc(sizeof(node));
    head->number = 1;
    head->next = NULL;

    node *second = malloc(sizeof(node));
    second->number = 2;
    second->next = NULL;

    head->next = second;

    for(node *ptr = head;ptr != NULL;ptr = ptr ->next){
        printf("%d\n",ptr->number);
    }
    free(second);
    free(head);
    return 0;
}
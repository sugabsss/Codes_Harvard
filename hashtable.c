#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int hash(char *word){
    return toupper(word[0]) - 'A';
}

int main (void){
    char *letter = get_char("") 
}
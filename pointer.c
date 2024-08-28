#include <stdio.h>
#include <cs50.h>

// Pointer are nothing more than a ADDRESS

int main(void){
int k = 5;  
int* pk;
*pk = 35;
pk = &k;
printf("%d\n",*pk);
}
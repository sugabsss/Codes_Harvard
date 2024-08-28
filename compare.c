#include <cs50.h>
#include <stdio.h>

int main (void)
{
    int x = get_int ("What's x?\n");
    int y = get_int ("What's y? \n");

if (x > y){
    printf ("x greater than y");
}
else if (x < y)
{
    printf ("x less than y");
}
else {
    printf ("x equal y");
}
}

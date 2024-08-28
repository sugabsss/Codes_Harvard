    #include <cs50.h>
    #include <stdio.h>

    int answer;

    int main (void)
    {
    answer = get_int("Quantos vezes o gato irá miar?\n");
        
        if (answer <= 0)
        {
            printf ("Numero Invalido\n");
        }
        else if (answer > 99)
        {
            printf ("Apenas numeros menores que 99 e maiores que 0\n");
        while (answer <= 0 || answer > 99)
        {
        answer = get_int("Pergunte outro numero!\n");
        }
        }
        else
        {
            printf("O gato irá miar:%d\n",answer);
            for (int i = 0; i  < answer; i++)
        {   
                printf ("meow\n");
        }
        }
    }

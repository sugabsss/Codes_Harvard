#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct{ 
    string nome;
    int votos;
}candidato;         //struct de criação dos meus candidatos;


bool selecao(char letra ,char inicio,char final){        //função para  restrição de letras;
    return (letra < inicio || letra > final);
}

int escrever_valor(candidato candidatos[], int num_candidatos, const char *filename){           //Função para escrever novos votos;
    FILE *f;                  //Criando um file para armazenar os dados da eleição;
    f = fopen(filename,"w");

    if (!f){
        printf("error file 404\n");
            return 1;   
    }
    fprintf(f,"Dados das eleições de : %d\n",2024);
     for (int i = 0; i < num_candidatos; i++){
        fprintf(f, "\nQuantidade de votos candidato Paulo:%d\n\n", candidatos[i].votos);
    }
    fclose(f);
}

    int ler_valor(candidato candidatos[], int num_candidatos, const char *filename){        //Função para leitura de votos;
    FILE *f;                 //Criando um file para armazenar os dados da eleição;
    f = fopen(filename,"r");
    if (!f){
    printf("Error 404 FILE NOT FOUND\n");
        return 1;
    }
    for (int i = 0; i < num_candidatos; i++){
        fscanf(
            f, "%d", &candidatos[i].votos);
    }
    fclose(f);
}
    
int main (void){
        const char *filename = "valor.txt";

        const int num_candidatos = 3;              //Criando nossos 3 candidatos;
    candidato candidatos[num_candidatos];
    
    candidatos[0].nome = "Paulo";
    candidatos[0].votos = 0;
    
    candidatos[1].nome = "Carlos";
    candidatos[1].votos = 0;

    candidatos[2].nome = "Maria";
    candidatos[2].votos = 0; 

    ler_valor(candidatos,num_candidatos,filename);

    printf("Escolhe a letra de acordo com seu candidato:\n");
    char letra = get_char("a --> Paulo\n b --> Carlos\n c --> Maria\n");                //Perguntando ao eleitor qual candidato será votado;

    char inicio = 'a';
    char final = 'c';

    if (selecao(letra,inicio,final)) {                              //criação e chamada da função de restrição de letras;
        printf("Candidato Invalido, Por favor tente novamente.\n");
        return 1;
    }
    else {
        printf("%c - Candidato selecionado com sucesso.\n",letra);                 //Fim da restrição de possiveis erros de votos;
    }                //Termino de criação dos 3 candidatos;

    if (letra == 'a'){                      //Adicionando votos ao candidato selecionado;
        candidatos[0].votos++;
    }
    else if (letra == 'b'){
        candidatos[1].votos++;
    }
    else{
        candidatos[2].votos++;
    } 
                                        //Fim da adição de votos do candidato selecionado;
    escrever_valor(candidatos,num_candidatos,filename);
    
    int max_votos = 0;                  //Encontrando o candidato com a maior quantidade de votos;
    for(int i = 0; i < num_candidatos;i++){
        if (candidatos[i].votos > max_votos){
            max_votos = candidatos[i].votos;}
        } 
        printf("Quantidade de votos do candidato eleito:%i\n",max_votos); 
    for(int i = 0; i < num_candidatos;i++){
    if (candidatos[i].votos == max_votos){
        printf("O candidato eleito foi:%s\n",candidatos[i].nome); //Candidato com mais votos encontrado e citado;
    }
    }   
        return 0;
}

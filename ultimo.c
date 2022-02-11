/*
 ============================================================================
 Name        : Arquivos.c
 Author      : ALlan Rodrigo e João Vitor Silva Gomes
 Version     : 0.1
 Copyright   : Your copyright notice
 Description : Implemente o utilitário Line.c que mostre o conteúdo de um 
 arquivo recebido na line de comando, mostrando cada line o número 
 respectivo.
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>


int main(void) {
	FILE *arq;
	char line[100];
	char *result;
	int i;
  
	arq = fopen("palavras.txt", "rt");
	if (arq == NULL) {
     printf("Problemas na abertura do arquivo\n");
     return;
  }
  	i = 1;
  	while (!feof(arq)) {
    	result = fgets(line, 100, arq);  
    	if (result) {
			printf("%d: %s",i,line);
    		i++;
	  }
  }
  fclose(arq);
}
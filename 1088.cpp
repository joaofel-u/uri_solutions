#include <iostream>

using namespace std;

int merge(int *saida, int *auxiliar, int inicio, int meio, int fim){
    int i, j, k;
    i = inicio;
    j = meio + 1;
    k = inicio;
    while(i <= meio && j <= fim){
        if(auxiliar[i] < auxiliar[j]){
            saida[k] = auxiliar[i];
            i++;
        }
        else{
            saida[k] = auxiliar[j];
            j++;
        }
        k++;
    }

    while(i <= meio){
        saida[k] = auxiliar[i];
        i++;
        k++;
    }

    while(j <= fim){
        saida[k] = auxiliar[j];
        j++;
        k++;
    }
    //Copia os elementos que foram ordenados para o auxiliar
    for(int p = inicio; p <= fim; p++)
        auxiliar[p] = saida[p];
}



int mergeSort(int *saida, int *auxiliar, int inicio, int fim){
    if(inicio < fim){
        int swaps = 0;
        int meio = (inicio + fim) / 2;
        swaps += mergeSort(saida, auxiliar, inicio, meio);
        swaps += mergeSort(saida, auxiliar, meio + 1, fim);
        merge(saida, auxiliar, inicio, meio, fim);
        return swaps;
    }
}


int main(int argc, char const *argv[]) {
  int n;

  while (cin >> n, n != 0) {
    int vetor[n];
    for (int i = 0; i < n; i++)
      cin >> vetor[i];

    int saida[n];
    int aux[n];

    swaps = mergeSort(saida, aux, 0, n-1);

  }

  return 0;
}

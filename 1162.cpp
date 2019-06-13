#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;


// swap p2 to p1, element by element, and return the counting of swaps
int swap(int* list, int p1, int p2) {
    int swaps = 0;
    int aux_i = p2-1;
    int aux_f = p2;
    while (aux_i >= p1) {
        int aux = list[aux_i];

        list[aux_i] = list[aux_f];
        list[aux_f] = aux;
        aux_i--;
        aux_f--;
        swaps++;
    }


    return swaps;
}


int main(int argc, char const *argv[]) {
    int testes;
    cin >> testes;

    for (int t = 0; t < testes; t++) {
        int n;
        cin >> n;

        int entrada[n];
        for (int i = 0; i < n; i++)
            cin >> entrada[i];


        // processamento
        int swaps = 0;
        int element = 1;
        for (int i = 0; i < n; i++) {
            while (element <= n) {
                for (int j = element-1; j < n; j++) {
                    if (entrada[j] == element) {
                        swaps += swap(entrada, element-1, j);
                        break;
                    }
                }

                element++;
            }
        }

        cout << "Optimal train swapping takes " << swaps << " swaps." << endl;
    }


    return 0;
}

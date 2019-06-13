#include <iostream>
#include <list>

using namespace std;


list< int* >* working;

// metodo para insercao em uma fila de prioridade
void priority_queue_insertion(int* value) {
    bool inserted = false;

    for (auto it = working->begin(); it != working->end(); it++) {
        if (((*it)[1] > value[1]) || ((*it)[1] == value[1] && (*it)[0] > value[0])) {
            working->insert(it, value);
            inserted = true;
            break;
        }
    }

    if (!inserted)
        working->push_back(value);
}


int main(int argc, char const *argv[]) {
    int n, m;
    cin >> n >> m;

    // leitura dos tempos que cada funcionario toma para processar um produto
    int tempos[n];
    for (int i = 0; i < n; i++)
        cin >> tempos[i];


    // leitura das quantidades de itens que cada cliente tem em sua cesta
    int clientes[m];
    for (int i = 0; i < m; i++)
        cin >> clientes[i];


    // processamento
    working = new list<int*>();

    // primeira distribuicao de trabalho
    for (int i = 0; i < n; i++) {
        int work_time = tempos[i] * clientes[i];
        int* aux = new int[2];
        aux[0] = i;
        aux[1] = work_time;
        priority_queue_insertion(aux);
    }

    // reposicao de trabalho
    for (int i = n; i < m; i++) {
        int* aux = working->front();
        int work_time = aux[1] + clientes[i] * tempos[aux[0]];
        working->pop_front();

        int* in_aux = new int[2];
        in_aux[0] = aux[0];
        in_aux[1] = work_time;
        priority_queue_insertion(in_aux);
    }


    // saida
    cout << working->back()[1] << endl;

    return 0;
}

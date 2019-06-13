#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef struct {
    int horas, valor;
} element;

bool order(element x, element y) {
    if (x.valor > y.valor)
        return true;
    else
        if (x.valor == y.valor) return x.horas < y.horas;
        else return false;
}


int solve(int tarefas[], int n_tarefas, int hora_atual) {
    int dp[n_pacotes+1][hora_atual+1];

    for (int i = 0; i <= n_tarefas; i++) {
        for (int j = 0; j <= hora_atual; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else {
                dp[i][j] = dp[i-1][j];
                if (j - pesos[i-1] >= 0) {
                    dp[i][j] = max(dp[i][j], dp[i-1][j-pesos[i-1]]+enfeites[i-1]);
                }
            }
        }
    }

    return dp[n_pacotes][peso];
}


int main(int argc, char const *argv[]) {

    int n_tarefas, horas_disponiveis;

    while (cin >> n_tarefas >> horas_disponiveis) {
        element tarefas[1004];

        for (int i = 0; i < n_tarefas; i++)
            scanf("%d %d", &tarefas[i].valor, &tarefas[i].horas);

        vector<element> vetor (tarefas, tarefas+n_tarefas);

        sort(vetor.begin(), vetor.end(), order);

        long perdido = 0;
        for (int hora_atual = 0; hora_atual < horas_disponiveis; hora_atual++) {
            if (n_tarefas > (horas_disponiveis-hora_atual)) {
                while
            }
        }


    }

    return 0;
}

#include <cstdio>
#include <algorithm>

using namespace std;


int solve(int enfeites[], int pesos[], int n_pacotes, int peso) {
    int dp[n_pacotes+1][peso+1];

    for (int i = 0; i <= n_pacotes; i++) {
        for (int j = 0; j <= peso; j++) {
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

    int galhos, cont;
    scanf("%d", &galhos);
    cont = 0;

    while (cont < galhos) {
        int n_pacotes, peso;
        int pesos[104], enfeites[104];

        scanf("%d", &n_pacotes);
        scanf("%d", &peso);

        for (int i = 0; i < n_pacotes; i++)
            scanf("%d %d", &enfeites[i], &pesos[i]);

        printf("Galho %d:\n", ++cont);
        printf("Numero total de enfeites: %d\n\n", solve(enfeites, pesos, n_pacotes, peso));

    }

    return 0;
}

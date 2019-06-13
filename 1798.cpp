#include <cstdio>
#include <list>

using namespace std;

int tamanhos_pesos[1001];
int dp[1001];

int cut(int tam) {
    if(dp[tam] == -1) {
        return max()
    }
}


int main(int argc, char const *argv[]) {

    int cortes, t;
    scanf("%d %d", &cortes, &t);



    for (int i = 0; i < 1001; i++) {
        tamanhos_pesos[i] = -1;
    }

    for (int i = 0; i < cortes; i++) {
        int* item = new int[2];
        scanf("%d %d", &item[0], &item[1]);
        tamanhos_pesos[item[0]] = item[1];
    }


    long dp = new long[t];
    dp[0] = 0;


    // CUT ROD
    for (int tam = 1; tam < t; tam++) {
        dp[tam] = 0;

        for (auto it = options->begin(); it != options->end(); it++) {
            int cut_size = (*it)[0];
            int value = (*it)[1];

            if (tam >= cut_size) {
                long total_value = value + dp[tam-cut_size];
                if (total_value > dp[tam]) dp[tam] = total_value;
            } else {
                if (dp[tam] == 0)
                    dp[tam] = options->front()[1];
                break;
            }
        }
    }

    printf("%ld\n", dp[t-1]);

    return 0;
}

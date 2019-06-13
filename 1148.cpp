#include <cstdio>
#include <algorithm>

using namespace std;

#define LIM 502
#define INF 2000


long distancia[LIM][LIM];

void floyd_warshall(int size) {
    // relaxamento
    long val;
	for (int k = 0; k <= size; ++k) {
		for (int i = 0; i <= size; ++i) {
			for (int j = 0; j <= size; ++j) {
				val = min(distancia[i][j], (distancia[i][k] + distancia[k][j]));
				distancia[i][j] = val;
			}
		}
	}
}


int main() {

    int n, e, x, y, h, k;
    long ans;
    while (true) {
        scanf("%d %d", &n, &e);
        if (n == 0 && e == 0) break;

        // reinicializacao
        for (int i = 0; i <= n; ++i)
            for (int j = 0; j <= n; ++j)
                distancia[i][j] = INF;

        // construcao do grafo
        for (int i = 0; i < e; ++i) {
            scanf("%d %d %d", &x, &y, &h);

            if (distancia[y][x] != INF) {
                distancia[x][y] = 0;
                distancia[y][x] = 0;
            } else {
                distancia[x][y] = h;
            }
        }

        // calculo das distancias de todos para todos usando floyd_warshall
        floyd_warshall(n);

        // tratamento das consultas
        scanf("%d", &k);

        for (int i = 0; i < k; ++i) {
            scanf("%d %d", &x, &y);

            ans = distancia[x][y];

            if (ans == INF)
                printf("Nao e possivel entregar a carta\n");
            else
                printf("%ld\n", ans);
        }

        printf("\n");
    }


	return 0;
}

#include <cstdio>
#include <cmath>

using namespace std;

#define LIM 102
#define INF 2000.0

typedef struct {
	int x, y, r;
} antena;

antena antenas[LIM];

double distancia[LIM][LIM];

void floyd_warshall(int size) {
    // relaxamento
    double val;
	for (int k = 0; k <= size; ++k) {
		for (int i = 1; i <= size; ++i) {
			for (int j = 1; j <= size; ++j) {
				val = min(distancia[i][j], (distancia[i][k] + distancia[k][j]));
				distancia[i][j] = val;
			}
		}
	}
}


int main() {

	int n, x, y, r, c, a1, a2, ans;
	double dist;

	while (true) {
		scanf("%d", &n);
		if (n == 0) break;

		for (int i = 0; i <= n; ++i)
			for (int j = 0; j <= n; ++j)
				distancia[i][j] = INF;

		// leitura da entrada
		for (int i = 1; i <= n; ++i) {
			scanf("%d %d %d", &x, &y, &r);
			antena a;
			a.x = x;
			a.y = y;
			a.r = r;
			antenas[i] = a;
		}

		// montagem do grafo
		for (int i = 1; i <= n; ++i) {
			x = antenas[i].x;
			y = antenas[i].y;
			r = antenas[i].r;

			for (int j = 1; j <= n; ++j) {
				if (i == j)
					distancia[i][j] = 0;
				else {
					dist = sqrt(pow(x-antenas[j].x ,2) + pow(y-antenas[j].y ,2));
					if (dist <= r)
					distancia[i][j] = dist;
				}
			}
		}

		// calculo da distancia de todos para todos usando floyd_warshall
		floyd_warshall(n);

		// processamento das consultas
		scanf("%d", &c);
		for (int i = 0; i < c; ++i) {
			scanf("%d %d", &a1, &a2);
			ans = distancia[a1][a2];
			if (ans == INF)
				printf("-1\n");
			else
				printf("%d\n", ans);
		}

	}

	return 0;
}

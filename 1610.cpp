#include <cstdio>

using namespace std;

#define BRANCO -1
#define CINZA 0
#define PRETO 1


// estruturas grafo
int grau[10002];
int adj[10002][10002];

int c[10002];


// funcao auxiliar ordenacao topologica
int dfs(int s) {
	int u;

	for (int i = 0; i < grau[s]; ++i) {
		u = adj[s][i];
		if (c[u] == PRETO) continue;
		if (c[u] == CINZA) return 1;
		c[u] = CINZA;
		if (dfs(u) == 1) return 1;
	}

   c[s] = PRETO;

   return 0;
}


int main(int argc, char const *argv[]) {

	int t, n, m, a, b;
	bool has_cicle;
	scanf("%d", &t);

	while (t--) {
		scanf("%d %d", &n, &m);

		// reinicializacao
		for (int i = 0; i <= n; ++i)
			grau[i] = 0;

		// leitura do grafo
		for (int i = 0; i < m; ++i) {
			scanf("%d %d", &a, &b);
			adj[b][grau[b]++] = a;
		}

		// inicializacao lista de busca
		for (int i = 0; i <= n; ++i)
			c[i] = BRANCO;

		has_cicle = false;
		for (int i = 1; i <= n; ++i) {
			if (c[i] == PRETO) continue;
			c[i] = CINZA;
			if (dfs(i) == 1) {
				has_cicle = true;
				break;
			}
		}

		if (has_cicle) printf("SIM\n");
		else printf("NAO\n");

	}

	return 0;
}

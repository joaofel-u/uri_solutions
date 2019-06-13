#include <cstdio>
#include <queue>

#define LIM 1010

using namespace std;

int adj[LIM][LIM];
int grau[LIM];


// funcao auxiliar ordenacao topologica
int bfs(int s) {
	int u, v;
	bool c[LIM];
	for (int i = 0; i < LIM; ++i)
		c[i] = false;

	c[s] = true;
	queue<int>* q = new queue<int>();
	q->push(s);

	while (!q->empty()) {
		u = q->front();
		q->pop();

		for (int i = 0; i < grau[u]; ++i) {
			v = adj[u][i];
			if (!c[v]) {
				c[v] = true;
				q->push(v);
			}
		}
	}

	int cont = 0;
	for (int i = 0; i < LIM; ++i)
		if (c[i])
			cont++;

   return cont;
}


int main(int argc, char const *argv[]) {

	int n, m, a, b, s, ans;

	while (scanf("%d %d", &n, &m) != EOF) {

		for (int i = 0; i <= n; ++i)
			grau[i] = 0;

		for (int i = 0; i < m; ++i) {
			scanf("%d %d", &a, &b);

			adj[a][grau[a]++] = b;
			adj[b][grau[b]++] = a;
		}

		scanf("%d", &s);

		ans = bfs(s);

		printf("%d\n", ans);

	}

	return 0;
}

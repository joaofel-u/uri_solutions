#include <cstdio>
#include <vector>
#include <list>
#include <climits>
#include <queue>

using namespace std;

#define LIM 200002
#define INF INT_MAX

typedef pair<int, int> arco;

vector< list<arco> > grafo;
int m, n;
int distancia[LIM];
bool c[LIM];

// use prim algorithm to get the min generation cost tree
int prim() {
    int u;
    for (int i = 1; i < m; ++i) {
        distancia[i] = INF;
        c[i] = false;
    }

    distancia[0] = 0;
    c[0] = true;

    priority_queue<arco, vector<arco>, greater<arco> > pq;
    pq.push(arco(distancia[0], 0));

    while (!pq.empty()) {
        u = pq.top().second;
        pq.pop();


        c[u] = true;

        int dist, v;
        for (auto it = grafo[u].begin(); it != grafo[u].end(); ++it) {
            dist = (*it).first;
            v = (*it).second;

            if (distancia[v] > dist && !c[v]) {
                distancia[v] = dist;
                pq.push(arco(distancia[v], v));
            }
        }
    }

    long custo_minimo = 0;
    for (int i = 0; i < m; ++i)
        custo_minimo += distancia[i];

    return custo_minimo;
}


int main() {
    int x, y, z;
    long total, custo_minimo;

    while (true) {
        scanf("%d %d", &m, &n);
        if (m == 0 && n == 0) break;

        grafo.clear();
        grafo.resize(m);

        total = 0;

        // leitura do grafo
        for (int i = 0; i < n; ++i) {
            scanf("%d %d %d", &x, &y, &z);
            grafo[x].push_back(arco(z, y));
            grafo[y].push_back(arco(z, x));

            total += z;
        }

        // calculo da arvore de custo minimo
        custo_minimo = prim();


        printf("%ld\n", total-custo_minimo);
    }

    return 0;
}

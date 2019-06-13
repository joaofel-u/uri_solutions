#include <cstdio>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int grau[1002];
int adj[1002][1002];

int dist[1002];

typedef pair<int, int> myPair;

void dijkstra(int s, int exclude) {
    for (int i = 0; i < 1002; ++i)
        dist[i] = 1000000;

    // Step 1: initialize graph
    priority_queue<myPair, vector<myPair>, greater<myPair>> pq;

    pq.push(make_pair(0, s));
    dist[s] = 0;            // The distance from the source to itself is, of course, zero

    int u, v, peso;
    while (!pq.empty()) {
        u = pq.top().second;
        pq.pop();

        for (int i = 0; i < grau[u]; ++i) {
            v = adj[u][i];
            if (v != exclude && u != exclude) {
                if (dist[v] > dist[u]+1) {
                    dist[v] = dist[u]+1;
                    pq.push(make_pair(dist[v], v));
                }
            }
        }
    }
}


int main(int argc, char const *argv[]) {

    int n, m, u, v;
    int c, r, e;

    while (scanf("%d %d", &n, &m) != EOF) {
        for (int i = 0; i <= n; ++i)
            grau[i] = 0;

        // leitura do grafo
        for (int i = 0; i < m; ++i) {
            scanf("%d %d", &u, &v);
            adj[u][grau[u]++] = v;
            adj[v][grau[v]++] = u;
        }

        scanf("%d %d %d", &c, &r, &e);

        // execucao
        dijkstra(c, e);

        printf("%d\n", dist[r]);
    }

    return 0;
}

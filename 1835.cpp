#include <cstdio>
#include <string>
#include <queue>

using namespace std;

bool visited[101];

int grau[101];
int adj[101][101];


void bfs (int s) {
    queue<int> f;

    visited[s] = true;
    f.push(s);

    while (!f.empty()) {
        int u = f.front();
        f.pop();

        for (int i = 0; i < grau[u]; ++i) {
            int aux = adj[u][i];
            if (!visited[aux]) {
                visited[aux] = true;
                f.push(aux);
            }
        }
    }
}


int main(int argc, char const *argv[]) {

    int testes;
    int cont = 1;
    scanf("%d", &testes);

    while (cont <= testes) {
        int n, m;
        scanf("%d", &n);
        scanf("%d", &m);

        for (int i = 0; i < 101; ++i)
            grau[i] = 0;

        int u, v;
        for (int i = 0; i < m; ++i) {
            scanf("%d %d", &u, &v);
            adj[u][grau[u]++] = v;
            adj[v][grau[v]++] = u;
        }

        // verificacao
        int faltam = 0;

        for (int i=0; i < 101; i++)
            visited[i] = false;

        bfs(1);
        for (int i=1; i <= n; i++) {
            if (visited[i] == false) {
                bfs(i);
                faltam++;
            }
        }


        // saida
        if (faltam)
            printf("Caso #%d: ainda falta(m) %d estrada(s)\n", cont++, faltam);
        else
            printf("Caso #%d: a promessa foi cumprida\n", cont++);
    }

    return 0;
}

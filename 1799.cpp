#include <cstdio>
#include <unordered_map>
#include <string>
#include <iostream>

using namespace std;

int grau[4002];
int adj[4002][4002];

int distancia[4002];

int c[4002];


void bellmanFord(int s, int size) {
    // Step 1: initialize graph
    for (int i = 0; i <= size; ++i) {
        distancia[i] = 100000;
    }
                  // Initialize the distancia to all vertices to infinity

    distancia[s] = 0;            // The distancia from the source to itself is, of course, zero

    // Step 2: relax edges repeatedly
    int u;
    for (int j = 1; j < size; ++j) {
        for (int v = 0; v < size; ++v) {
            for (int i = 0; i < grau[v]; ++i) {
                u = adj[v][i];
                if (distancia[u] + 1 < distancia[v])
                    distancia[v] = distancia[u]+1;
            }
        }
    }
}


int main(int argc, char const *argv[]) {

    int pontos, ligacoes, u, v;
    string c1, c2;
    unordered_map<string, int> map;
    scanf("%d %d", &pontos, &ligacoes);

    for (int i = 0; i < pontos; ++i)
        grau[i] = 0;

    // leitura do grafo
    for (int i = 0; i < ligacoes; ++i) {
        cin >> c1 >> c2;
        if (map.size() < pontos) {
            map.emplace(c1, map.size());
            map.emplace(c2, map.size());
        }

        u = map[c1];
        v = map[c2];

        adj[u][grau[u]++] = v;
        adj[v][grau[v]++] = u;
    }


    // execucao
    int s = map["Entrada"];
    int queijo = map["*"];
    int t = map["Saida"];
    bellmanFord(s, pontos);
    int first = distancia[queijo];
    bellmanFord(queijo, pontos);
    int last = distancia[t];

    printf("%d\n", first+last);


    // executar dijkstra de s ate queijo
    // executar dijkstra de queijo ate saida
    return 0;
}

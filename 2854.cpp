#include <cstdio>
#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

int grau[302];
int adj[302][302];


void dfsRcc(int *cc, int v, int id) {
   cc[v] = id;
   for (int i = 0; i < grau[v]; ++i) {
       int u = adj[v][i];
       if (cc[u] == -1)
        dfsRcc(cc, u, id);
   }
}

int UGRAPHcc(int *cc, int m)
{
   int id = 0;
   for (int v = 0; v < m; ++v)
      cc[v] = -1;
   for (int v = 0; v < m; ++v)
      if (cc[v] == -1)
         dfsRcc(cc, v, id++);
   return id;
}


int main(int argc, char const *argv[]) {

  int m, n, u, v;
  string n1, rel, n2;
  unordered_map<string, int> map;

  scanf("%d %d", &m, &n);
  // leitura do grafo
  for (int i = 0; i < n; ++i) {
      cin >> n1 >> rel >> n2;
      if (map.size() < m) {
          map.emplace(n1, map.size());
          map.emplace(n2, map.size());
      }

      u = map[n1];
      v = map[n2];

      adj[u][grau[u]++] = v;
      adj[v][grau[v]++] = u;
  }

  // solucao
  int* cc = new int[m];
  int ans = UGRAPHcc(cc, m);

  printf("%d\n", ans);

  return 0;
}

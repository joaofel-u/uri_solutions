#include <cstdio>
#include <algorithm>

using namespace std;

int moedas[1004];

int solve(int v, int m){
    if (v < 0) return false;
    if (v == 0) return true;
    if (m == 0) return false;
    return solve(v-moedas[m], m-1) || solve(v, m-1);
}

int main(int argc, char const *argv[]) {

    int v, m;

    scanf("%d %d", &v, &m);

    for (int i = 1; i <= m-1; i++) {
        scanf("%d ", &moedas[i]);
    }
    scanf("%d", &moedas[m]);

    if (solve(v, m))
        printf("S\n");
    else
        printf("N\n");

    return 0;
}

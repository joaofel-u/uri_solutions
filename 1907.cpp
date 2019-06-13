#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

#define LIM 1030


char mapa[LIM][LIM];
int dx[] = {1, 0, -1, 0};
int dy[] = {0, -1, 0, 1};
int m, n;


bool valid(int x, int y) {
	if (x < 0 || x >= n || y < 0 || y >= m)
		return false;

	return mapa[x][y] == '.';
}


void dfs(int x, int y) {
	mapa[x][y] = 'o';

	for (int i = 0; i < 4; ++i) {
		if (valid(x+dx[i], y+dy[i]))
			dfs(x+dx[i], y+dy[i]);
	}
}


int main(int argc, char const *argv[]) {

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; ++i)
		scanf("%s", mapa[i]);


	int ans = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (mapa[i][j] == '.') {
				ans++;
				dfs(i, j);
			}
		}
	}

	printf("%d\n", ans);

	return 0;
}

// direita e baixo apenas

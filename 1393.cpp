#include <cstdio>

using namespace std;


int main(int argc, char const *argv[]) {

	int n;
	while (scanf("%d", &n), n != 0) {
		int in = 0;
		int f = 1;
        int ans = 0;

        for(int i = 1; i <= n; ++i) {
            ans = in + f;
            in = f;
            f = ans;
        }

		printf("%d\n", ans);
	}

	return 0;
}

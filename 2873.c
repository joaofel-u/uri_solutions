#include <stdio.h>

int main(int argc, char const *argv[]) {

	int a, b, c, d;
	while (scanf("%d %d %d %d", &a, &b, &c, &d), a != 0 || b != 0 || c != 0 || d != 0) {

	    float sp = (a/2.0) + b;
	    float ans = (sp/d) * c;

	    printf("%.5f\n", ans);
	}

	return 0;
}

#include <cstdio>
#include <cmath>

using namespace std;


double gambler (int ev1, int ev2, int at) {
	if (at == 3) {
		return (double)ev1 / (double)(ev1+ev2);
	} else {
		double q = 1.0 - (6-at)/6.0;
		double dado = (1.0-q)/(q);

		return (1.0 - pow(dado, ev1)) / (1.0 - pow(dado, ev1+ev2));
	}

}


int main(int argc, char const *argv[]) {

	int ev1, ev2, at, d, aux;
	double ans;
	while (scanf("%d %d %d %d", &ev1, &ev2, &at, &d), ev1 != 0 && ev2 != 0 && at != 0 && d != 0) {

		aux = ev1;
		ev1 = 0;
		while (aux > 0) {
			aux -= d;
			ev1++;
		}

		aux = ev2;
		ev2 = 0;
		while (aux > 0) {
			aux -= d;
			ev2++;
		}

		ans = gambler(ev1, ev2, at);

		printf("%.1lf\n", ans*100);
	}

	return 0;
}

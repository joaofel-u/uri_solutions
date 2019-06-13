#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;


int main(int argc, char const *argv[]) {

	int r, la, lo;

	while(cin >> r >> la >> lo) {
		double x = cos(lo) * r * sin(la);
		double y = sin(lo) * r * sin(la);
		double z = r * cos(la);

		printf("%.2f %.2f %.2f\n", x, y, z);

	}

	return 0;
}

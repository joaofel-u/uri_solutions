#include <iostream>
#include <cmath>
#include <bitset>

using namespace std;


#define M 64

int main(int argc, char const *argv[]) {

	unsigned long long int x, y;
	while (cin >> x >> y, x != 0 || y != 0) {

		bitset<M> bsetx(x);
		bitset<M> bsety(y);

		int hamming = 0;
		for (int i = 0; i < M; ++i) {
			if (bsetx[i] != bsety[i])
				hamming++;
		}

		cout << hamming << endl;

	}

	return 0;
}

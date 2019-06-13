#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>

using namespace std;


int main(int argc, char const *argv[]) {

	string palavra;
	int num_palavras = 0;
	char compare = 'b';

	while (cin >> palavra) {
		num_palavras++;

		int length = palavra.size()-1;
		long double result = 0;
		for (int i = 0; i < palavra.size(); ++i) {
			char c = palavra[length-i];

			if (c == compare)
				result += powl(2, i);
		}

		printf("Palavra %d\n%.0Lf\n\n", num_palavras, result);

	}

	return 0;
}

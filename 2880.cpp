#include <string>
#include <iostream>

using namespace std;


int main(int argc, char const *argv[]) {

	string mensagem, crib;
	cin >> mensagem;
	cin >> crib;

	int crib_size = crib.size();
	int possibilidades = mensagem.size() - crib_size + 1;

	for (int i = possibilidades-1; i >= 0; --i) {
		for (int j = 0; j < crib_size; ++j) {
			if (mensagem[i+j] == crib[j]) {
				possibilidades--;
				break;
			}
		}
	}

	cout << possibilidades << endl;

	return 0;
}

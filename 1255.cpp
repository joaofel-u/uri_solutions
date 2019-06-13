#include <iostream>
#include <string>
#include <algorithm>
#include <locale>

typedef struct {
	char letra;
	int cont;
} registro;

using namespace std;

// compara dois registros e retorna se o primeiro eh menor que o segundo
bool compare_registers(registro r1, registro r2) {
	if (r1.cont != r2.cont)
		return r1.cont > r2.cont;
	else
		return r1.letra < r2.letra;
}


int main(int argc, char const *argv[]) {

	int n;
	cin >> n;
	string aux;
	getline(cin, aux);

	while(n--) {
		string entrada;
		getline(cin, entrada);

		// inicializacao
		locale loc;
		registro registers[26];
		for (int i = 0; i < 26; ++i) {
			registers[i].letra = 97+i;
			registers[i].cont = 0;
		}

		// contagem
		for (char c : entrada) {
			char aux = tolower(c, loc);
			if (97 <= aux && aux <= 122)
				registers[aux-97].cont++;
		}

		// ordenacao e saida
		sort(registers, registers+26, compare_registers);

		int greatest = registers[0].cont;
		int i = 0;
		while (registers[i].cont == greatest)
			printf("%c", registers[i++].letra);

		printf("\n");


	}

	return 0;
}

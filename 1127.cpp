#include <iostream>
#include <unordered_map>

using namespace std;


int main(int argc, char const *argv[]) {

	// initialization
	unordered_map<string, int> escala_musical;
	escala_musical["A"] = 0;
	escala_musical["A#"] = 1;
	escala_musical["Bb"] = 1;
	escala_musical["B"] = 2;
	escala_musical["Cb"] = 2;
	escala_musical["B#"] = 3;
	escala_musical["C"] = 3;
	escala_musical["Db"] = 4;
	escala_musical["C#"] = 4;
	escala_musical["D"] = 5;
	escala_musical["Eb"] = 6;
	escala_musical["D#"] = 6;
	escala_musical["E"] = 7;
	escala_musical["Fb"] = 7;
	escala_musical["F"] = 8;
	escala_musical["E#"] = 8;
	escala_musical["F#"] = 9;
	escala_musical["Gb"] = 9;
	escala_musical["G"] = 10;
	escala_musical["Ab"] = 11;
	escala_musical["G#"] = 11;

	// input
	int m, t;
	while (cin >> m >> t, m != 0 || t != 0) {
		string nota, last;

		// leitura da melodia
		int melodia[100004];
		cin >> last;
		int last_v = escala_musical[last];
		int actual_v = 0;
		int val = 0;
		for (int i = 0; i < m-1; ++i) {
			cin >> nota;
			actual_v = escala_musical[nota];

			if (last_v > actual_v)
				val = 12 - last_v + actual_v;
			else
				val = actual_v - last_v;

			melodia[i] = val;

			last = nota;
			last_v = actual_v;
		}


		// leitura do trecho
		int trecho[10004];
		cin >> last;
		last_v = escala_musical[last];
		for (int i = 0; i < t-1; ++i) {
			cin >> nota;
			actual_v = escala_musical[nota];

			if (last_v > actual_v)
				val = 12 - last_v + actual_v;
			else
				val = actual_v - last_v;

			trecho[i] = val;

			last = nota;
			last_v = actual_v;
		}

		// checking
		int possibilidades = m-t + 1;
		bool plagio = false;
		for (int i = 0; i < possibilidades; ++i) {
			if (melodia[i] == trecho[0]) {
				bool teste = true;
				for (int j = 1; j < t-1; ++j) {
					if (melodia[i+j] != trecho[j]) {
						teste = false;
						break;
					}
				}

				if (teste) {
					plagio = true;
					break;
				}
			}
		}

		if (plagio)
			cout << "S" << endl;
		else
			cout << "N" << endl;
	}

	return 0;
}

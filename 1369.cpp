#include <string>
#include <iostream>
#include <cstring>

using namespace std;

// classe que define um nodo de uma lista encadeada basica
class Elemento {
private:
	string arquivo;
	long tamanho;
	Elemento* next;

public:
	// Construtor para elementos livres
	Elemento(long tam, Elemento* proximo) {
		arquivo = "";
		tamanho = tam;
		next = proximo;
	}

	// construtor para elementos ocupados por arquivo
	Elemento(string file, long tam, Elemento* proximo) {
		arquivo = file;
		tamanho = tam;
		next = proximo;
	}

	long get_tamanho() {
		return tamanho;
	}

	void set_tamanho(long tam) {
		tamanho = tam;
	}

	void set_arquivo(string file) {
		arquivo = file;
	}

	void set_next(Elemento* proximo) {
		next = proximo;
	}

	Elemento* get_next() {
		return next;
	}

	string get_arquivo() {
		return arquivo;
	}

	bool livre() {
		return arquivo == "";
	}
};

// classe que define uma lista encadeada simples
class LinkedList {
private:
	Elemento* head;
	long total_size;
	long free_space;

public:
	// Cria a lista encadeada com apenas um elemento livre de tamanho total
	LinkedList(long tam_total) {
		head = new Elemento(tam_total, NULL);
		total_size = tam_total;
		free_space = tam_total;
	}

	// funcao que insere um elemento no armazenamento
	bool insert(string arquivo, long tamanho, bool otimizado) {
		if (tamanho > free_space)
			return false;
		else {
			Elemento* aux = head;
			Elemento* candidato = NULL;
			while (aux != NULL) {
				// encontrou um espaco passivel de ser utilizado
				if (aux->livre() and aux->get_tamanho() >= tamanho) {
					if (candidato == NULL or candidato->get_tamanho() > aux->get_tamanho())
						candidato = aux;
				}

				aux = aux->get_next();
			}

			// Nao encontrou um bloco para inserir o elemento (tenta otimizar se ainda nao foi, caso contrario retorna false)
			if (candidato == NULL) {
				if (otimizado)
					return false;
				else {
					this->otimiza();
					return this->insert(arquivo, tamanho, true);
				}
			}
			// encontrou o melhor bloco para inserir o arquivo
			else {
				if (candidato->get_tamanho() == tamanho)
					candidato->set_arquivo(arquivo);
				else {
					long diferenca = candidato->get_tamanho() - tamanho;
					candidato->set_arquivo(arquivo);
					candidato->set_tamanho(tamanho);
					candidato->set_next(new Elemento(diferenca, candidato->get_next()));
				}

				free_space -= tamanho;
				return true;
			}
		}
	}

	// otimiza o armazenamento, nao deixando espacos vazios entre os elementos
	void otimiza() {
		Elemento* last = NULL;
		Elemento* aux = head;
		while (aux != NULL) {
			if (aux->livre()) {
				if (aux == head)
					head = aux->get_next();
				else {
					last->set_next(aux->get_next());
				}

				last = aux;
				aux = aux->get_next();

				if (aux == NULL) {
					last->set_tamanho(free_space);
				}
			}
		}
	}

	// remove um arquivo logicamente do armazenamento
	void remove(string arquivo) {
		Elemento* aux = head;
		Elemento* last = NULL;

		while(aux != NULL and aux->get_arquivo() != arquivo) {
			last = aux;
			aux = aux->get_next();
		}

		if (aux != NULL) {
			aux->set_arquivo("");
			free_space += aux->get_tamanho();

			if (aux->get_next() != NULL) {
				Elemento* temp = aux->get_next();
				if (temp->livre())
					aux->set_tamanho(aux->get_tamanho() + temp->get_tamanho());
					aux->set_next(temp->get_next());
					delete temp;
			}
		}
		// lembrar de unir espacos vazios
	}

	float get_pct_livre() {
		float pct = free_space / total_size;
		return pct;
	}
};


// converte um tamanho de entrada para kilobytes
long to_kb(char* entrada) {
	int length = strlen(entrada);
	char tamanho[length-1];
	char unidade = entrada[length-2];
	strncpy(tamanho, entrada, length-2);
	long value = stol(tamanho);

	if (unidade == 'M')
		value = value * 1024;
	else if (unidade == 'G')
		value = value * 1024 * 1024;
	return value;
}


// fluxo principal do programa
int main() {
	int operacoes;
	char tamanho_total[7];
	LinkedList* storage;

	while (true) {
		// capturar entrada
		int operacoes;
		scanf("%d", &operacoes);

		// condicao de parada
		if (operacoes == 0)
			break;

		scanf("%s", tamanho_total);

		long tam_tot = to_kb(tamanho_total);

		storage = new LinkedList(tam_tot);

		for (int i = 0; i < operacoes; i++) {

			char op[8], arquivo[11], tamanho[7];
			char entrada[3][11];
			int j = 0;
			while (scanf("%s", entrada[j]) == 1) {
				j++;
			}
			printf("%s", op);
			if (op == "insere") {
				scanf("%s %s", arquivo, tamanho);
				printf("passou");
				long tam_kb = to_kb(tamanho);

				if (!(storage->insert(arquivo, tam_kb, false)))
					printf("ERRO: disco cheio");
			} else if (op == "remove") {
				scanf("%s", arquivo);

				storage->remove(arquivo);
			} else {  // op == otimiza
				storage->otimiza();
			}
		}
	}

	// processamento
	return 0;
}

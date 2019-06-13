#include <iostream>
#include <list>

using namespace std;


void insert_sorted(list<int*>* list, int* item) {
    auto it = list->begin();
    bool inserted = false;
    for (; it != list->end(); it++) {
         if ((*it)[2] == item[2]) {
            if ((*it)[1] == item[1]) {
                if((*it)[0] < item[0]) {
                    list->insert(it, item);
                    inserted = true;
                    break;
                }
            } else if ((*it)[1] < item[1]) {
                list->insert(it, item);
                inserted = true;
                break;
            }
         } else if ((*it)[2] < item[2]) {
             list->insert(it, item);
             inserted = true;
             break;
         }
    }

    if(!inserted)
        list->push_back(item);
}


int main(int argc, char const *argv[]) {

    int n, c;
    int caso = 0;

    while (cin >> n >> c, n != 0 || c != 0) {
        caso++;

        list<int*>* itens = new list<int*>();

        // entrada
        for (int i = 0; i < n; i++) {
            int* item = new int[3];
            cin >> item[0] >> item[1];
            item[2] = item[1]/item[0];
            insert_sorted(itens, item);
        }

        long interesse = 0;

        while (c > 0 && !itens->empty()) {
            int* item = itens->front();
            itens->pop_front();

            if (item[0] <= c) {
                c -= item[0];
                interesse += item[1];
            }
        }

        cout << "Caso " << caso << ": " << interesse << endl;
    }

    return 0;
}

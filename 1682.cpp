#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>

using namespace std;

// retorna 1 caso um genoma seja valido
int valid_genom(string genom) {
  int size = genom.size();

  if (size == 1)
    return 1;

  int max_sub_len = size/2;
  int len = 1;

  while (len <= max_sub_len) {
    string substring = genom.substr(size-len, len);
    string aux = genom.substr(size-len-len, len);
    if (substring == aux) {
        return 0;
    }

    len++;
  }

  return 1;
}



int main(int argc, char const *argv[]) {
  while (1) {
    int n, i;
    scanf("%d", &n);

    string genom = "";
    i = 0;
    while (i < n) {
      genom.append("N");
      if (!(valid_genom(genom))) {
        genom.erase(i);
        genom.append("O");
        if (!(valid_genom(genom))) {
          genom.erase(i);
          genom.append("P");
          if (!(valid_genom(genom))) {
            genom.erase(i);
            i--;
            if (i < 0)
              break;
          }
        }
      }
      i++;
    }

    cout << genom << endl;
  }

  return 0;
}

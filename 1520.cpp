#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[]) {
  while (1) {
          int n;
          if (scanf("%d ", &n) == EOF)
              break;

          int racks[10005];

          array<int> empty;
          swap( racks, empty );
          int racks_size = 10005;

          int end_pos = 0;

          for (int i = 0; i < n; i++) {
              int ini, fim;
              scanf("%d %d", &ini, &fim);

              for (int j = ini; j < fim+1; j++) {
                  racks[end_pos] = j;
                  end_pos += 1;
              }
          }

          sort(racks, racks + racks_size);

          int value;
          scanf("%d", &value);
          int fst = 0, lst = 0;
          int found = 0;

          for (int i = 0; i < racks_size; i++) {
              int v = racks[i];
              if (v == 0)
                  break;

              if (found == 1) {
                  if (v == value)
                      lst += 1;
                  else
                      break;
              } else {
                  if (v == value) {
                      fst = i;
                      lst = fst;
                      found = 1;
                  }
              }
          }

          if (found == 1)
              printf("%d found from %d to %d",value, fst, lst);
          else
              printf("%d not found", value);
  }

  return 0;
}

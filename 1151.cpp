#include <cstdio>

using namespace std;


int main(int argc, char const *argv[]) {

    int n;
    scanf("%d", &n);


    int* fib = new int[n];
    fib[0] = 0;
    fib[1] = 1;

    for (int i = 2; i < n; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }

    for (int i = 0; i < n-1; i++) {
        printf("%d ", fib[i]);
    }
    printf("%d\n", fib[n-1]);

    return 0;
}

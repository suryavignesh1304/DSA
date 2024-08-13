#include <stdio.h>
#include <stdlib.h>

int rpg(int n, int initial, int poweri[], int bonusi[]) {
    int c = 0;
    int current = initial;
    for (int i = 0; i < n; i++) {
        if (poweri[i] <= current) {
            c += 1;
            current += bonusi[i];
        } else {
            break;
        }
    }

    return c;
}

int main() {
    int n = 2;
    int initial = 123;
    int poweri[] = {78, 130};
    int bonusi[] = {10, 0};

    int result = rpg(n, initial, poweri, bonusi);
    printf("%d\n", result);
    return 0;
}

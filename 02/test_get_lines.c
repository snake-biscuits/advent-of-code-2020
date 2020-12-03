#include <stdio.h>
#include "get_lines.h"


int main() {
    char lines[256][1024];
    int len_lines = get_lines("passwords.txt", lines);

    printf("line 1: %s\n", lines[0]);
    printf("line 2: %s\n", lines[1]);
    printf("line 3: %s\n", lines[2]);
    printf("line 4: %s\n", lines[3]);

    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../common/get_lines.h"


int main(void) {
    char* lines[1024];
    int len_lines = get_lines("passwords.txt", lines);
    if (len_lines == -1) {
        return 1;  // file not found
    }

    int invalid_passwords = 0;

    int min_char, max_char;
    char test_char[2];
    char password[64];

    int i, j, k;
    int char_count;
    char token[64];
    for (i=0; i<len_lines; i++) {
        strcpy(token, "");
        k = 0;
        for (j=0; j<128; j++) {  // assuming no line is longer than 128 chars
            // lots of repetition for each case, could refine
            if (lines[i][j] == "-"[0]) {
                min_char = atoi(token);
                j++;
                strcpy(token, "");
                k = 0;
            }
            else if (lines[i][j] == " "[0]) {
                max_char = atoi(token);
                j++;
                strcpy(token, "");
                k = 0;
            }
            else if (lines[i][j] == ":"[0]) {
                printf("%s\n", token);
                strcpy(test_char, token);
                j += 2;
                strcpy(token, "");
                k = 0;
            }
            token[k] = lines[i][j];
            k++;
        }
        strcpy(password, token);
        printf("%d-%d %s: %s\n", min_char, max_char, test_char, password);
        /* ^ recreate the string */
        return 0;

        char_count = 0;
        for (i=0; i<64; i++) {
            if (password[i] == test_char[0]) {
                char_count++;
            }
        }
        if (!(min_char <= char_count || char_count <= max_char)) {
            invalid_passwords++;
        }
    }

    printf("Found %i invalid_passwords", invalid_passwords);

    return 0;
}

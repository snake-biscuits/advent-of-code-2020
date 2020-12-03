#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void) {
    FILE *file;
    file = fopen("passwords.txt", "r");
    if (file == NULL) {
    	printf("Couldn't open %s\n", "passwords.txt");
		return -1;
    }

	int invalid_passwords = 0;
	
	int min_char, max_char;
	char test_char[2];
	char password[64];
	
	int i, j;
	int char_count;
    char line[128];
	char token[64];
    while (fgets(line, 128, file) != NULL) {  // get each password & policy
		strcpy(token, "");
		j = 0;
	    for (i=0; i<128; i++) {
			// lots of repetition for each case, could refine
			if (line[i] == "-"[0]) {
				min_char = atoi(token);
				i++;
				strcpy(token, "");
				j = 0;
			}
			else if (line[1] == " "[0]) {
				max_char = atoi(token);
				i++;
				strcpy(token, "");
				j = 0;
			}
			else if (line[1] == ":"[0]) {
				printf("%s\n", token);
				strcpy(test_char, token);
				i += 2;
				strcpy(token, "");
				j = 0;
			}
			token[j] = line[i];
			j++;
		}
		strcpy(password, token);
		printf("%d-%d %s: %s\n", min_char, max_char, test_char, password);
		return 0;
		
		char_count = 0;
		for (i=0; i<64; i++) {
			if (password[i] == test_char[0]) {
				char_count++;
			}
		}
		if (!(min_char <= char_count <= max_char)) {
			invalid_passwords++;
		}
		
    }
    fclose(file);
	
	printf("Found %i invalid_passwords", invalid_passwords);

	return 0;
}
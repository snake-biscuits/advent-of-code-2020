#include <stdio.h>
#include <stdlib.h>


int get_numbers(char* filename, int* output) {
    /* reads numbers from filename,
     * saves them in output,
     * returns the number of lines read */
    FILE *file;

    file = fopen(filename, "r");
    if (file == NULL) {
    	printf("Couldn't open %s\n", filename);
	return -1;
    }

    char buffer[8];
    int lines_read = 0;
    while (fgets(buffer, 8, file) != NULL) {
	    output[lines_read] = atoi(buffer);
	    lines_read++;
    }
    fclose(file);
    return lines_read;
}

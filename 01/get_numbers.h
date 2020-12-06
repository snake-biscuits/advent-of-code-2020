#include <stdio.h>  /* printf, fopen, fclose, fgets */
#include <stdlib.h>  /* atoi */


int get_numbers(char* filename, int* output) {
    /* reads numbers from filename,
     * saves them to output,
     * returns the number of lines read */
    FILE *file;

    file = fopen(filename, "r");
    if (file == NULL) {
    	printf("Couldn't open %s\n", filename);
	return -1;
    }

    char buffer[8];  // 8 char limit to line length
    int lines_read = 0;
    while (fgets(buffer, 8, file) != NULL) {
	    output[lines_read] = atoi(buffer);
	    lines_read++;
    }
    fclose(file);
    return lines_read;
}

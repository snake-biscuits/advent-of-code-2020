#include <stdio.h>  /* printf, fopen, fclose, fgets */
#include <stdlib.h>  /* malloc */
#include <string.h>  /* strcpy */

#define MAX_LINE_LENGTH 1024


int get_lines(char *filename, char **output) {
	/* reads lines from filename,
     * saves them to output,
     * returns the number of lines read */
    FILE *file;
    file = fopen(filename, "r");
    if (file == NULL) {
    	printf("Couldn't open %s\n", filename);
	return -1;
    }

    char buffer[MAX_LINE_LENGTH];
    int lines_read = 0;
    while (fgets(buffer, MAX_LINE_LENGTH, file) != NULL) {
        /* !!! INITIALISE THE STRING POINTER WITH: malloc() !!! */
        output[lines_read] = malloc(MAX_LINE_LENGTH);
	    strcpy(output[lines_read], buffer);
	    lines_read++;
    }
    fclose(file);

    strcpy(output[lines_read + 1], "\0");

    return lines_read;
}

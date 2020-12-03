#include <stdio.h>
#include <stdlib.h>


int get_lines(char* filename, char** output) {  // note: char (*output[LINE_MAX])[STRING_MAX];
	/* reads lines from filename,
     * saves them to output,
     * returns the number of lines read */
    FILE *file;
    file = fopen(filename, "r");
    if (file == NULL) {
    	printf("Couldn't open %s\n", filename);
	return -1;
    }

    char buffer[1024]; // if line is longer than 1024 chars, it will be split
    int lines_read = 0;
    while (fgets(buffer, 1024, file) != NULL) {
	    strcpy(output[lines_read], buffer);
	    lines_read++;
    }
    fclose(file);

    return lines_read;
}
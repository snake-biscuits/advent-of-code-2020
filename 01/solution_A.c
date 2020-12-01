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
    int count = 0;  // lines read
    while (fgets(buffer, 8, file) != NULL) {
	    output[count] = atoi(buffer);
	    count++;
    }
    fclose(file);
    return count;
}


int main(void) {
    int numbers[256];
    int len_numbers = get_numbers("numbers.txt", numbers);
    if (len_numbers == -1) {
    	return 1;  // file not found
    }

    int i, x;
    int j, y;
    for (i=0; i<len_numbers; i++) {
    	x = numbers[i];
	for (j=i+1; j<len_numbers; j++) {
	    y = numbers[j];
	    if (x + y == 2020) {
    		printf("%i * %i = %i\n", x, y, x * y);
		return 0;
	    }
	}
    }
    return 2;  // answer not found
}

#include <stdio.h>
#include <stdlib.h>


int get_numbers(char* filename, int* output) {
    /* reads newline separated numbers from filename,
     * places them into output_list,
     * returns the number of lines read */
    FILE *file;

    file = fopen(filename, "r");
    if (file == NULL) {
    	printf("Couldn't open %s\n", filename);
	return -1;
    }

    char buffer[1];
    int count = 0;  // the number of lines read
    int i = 0;
    char number[4] = "    ";
    while (fgets(buffer, 1, file) != NULL) {
    	if (buffer == "\n") {
	    output[count] = atoi(number);
	    number[0] = " ";  // pointers
	    number[1] = " ";  // make
	    number[2] = " ";  // me
	    number[3] = " ";  // hurt
	    count += 1;
	    i = 0;
    	}
	else {
	    number[i] = buffer;  // google C string operations (or get a segfault again)
	    i += 1;
	}
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

#include <stdio.h>  /* printf */
#include "get_numbers.h"

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

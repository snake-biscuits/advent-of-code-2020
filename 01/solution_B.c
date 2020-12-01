#include <stdio.h>
#include "get_numbers.h"

int main(void) {
    int numbers[256];
    int len_numbers = get_numbers("numbers.txt", numbers);
    if (len_numbers == -1) {
    	return 1;  // file not found
    }

    int i, x;
    int j, y;
	int k, z;
    for (i=0; i<len_numbers; i++) {
    	x = numbers[i];
		for (j=i+1; j<len_numbers; j++) {
			y = numbers[j];
			for (k=j+1; k<len_numbers; k++) {
                z = numbers[k];
				if (x + y + z == 2020) {
					printf("%i * %i * %i = %i\n", x, y, z, x * y * z);
				    return 0;
				}
			}
		}
    }
    return 2;  // answer not found
}

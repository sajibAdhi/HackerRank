#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    
    if(n >= 10000 && n <= 99999) {
        int digit, temp, sum = 0;
        temp = n;
        while(temp > 0)
        {
            digit = temp % 10;
            sum = sum + digit;
            temp = temp / 10;
        }    
          printf("%d\n",sum);
    }

    return 0;
}
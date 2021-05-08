#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#define p printf

int power(int base, int exponent){
    int result = 1;
    for (int i =exponent; i>0; i--)
    {
        result = result * base;
    }    
    return result;
}


int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
  	// Complete the code.
    
    if(1 <= a && a <= b && b <= power(10, 6)){
        
        for(a; a <= b; a++) {
            if(1 <= a && a <= 9){
        
                if (a == 1) {
                    p("one\n");    
                }else if (a == 2) {
                    p("two\n");    
                }else if (a == 3) {
                    p("three\n");    
                }else if (a == 4) {
                    p("four\n");    
                }else if (a == 5) {
                    p("five\n");    
                }else if (a == 6) {
                    p("six\n");    
                }else if (a == 7) {
                    p("seven\n");    
                }else if (a == 8) {
                    p("eight\n");    
                }else if (a == 9) {
                    p("nine\n");    
                }
        
            }else if (a > 9) {
                if(a%2 != 0){
                    p("odd\n");
                }else{
                    p("even\n");
                }
            }
        }    
    }
    
    return 0;
}
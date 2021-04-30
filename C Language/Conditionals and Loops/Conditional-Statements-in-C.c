#include <stdio.h>
#define p printf

int main(){
    int number;
    scanf("%d",&number);
    
    if(1 <= number && number <= 9){
        
        if (number == 1) {
            p("one\n");    
        }else if (number == 2) {
            p("two\n");    
        }else if (number == 3) {
            p("three\n");    
        }else if (number == 4) {
            p("four\n");    
        }else if (number == 5) {
            p("five\n");    
        }else if (number == 6) {
            p("six\n");    
        }else if (number == 7) {
            p("seven\n");    
        }else if (number == 8) {
            p("eight\n");    
        }else if (number == 9) {
            p("nine\n");    
        }
        
    }else if (number > 9) {
        p("Greater than 9 \n");
    }
}
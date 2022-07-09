#include <stdio.h>

int main() 
{
    int maxLength = 100;
    char ch,s[100],sen[100];
    
    scanf("%c",&ch);
    scanf("%s",s);
    scanf("\n");
    scanf("%[^\n]%*c",sen);
    
    printf("%c\n",ch);
    printf("%s\n",s);
    printf("%s\n",sen);
   
    return 0;
}
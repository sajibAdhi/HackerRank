#include<stdio.h>
int main()
{
    char str[100];
    scanf("%[^\n]%*c",str);

    printf("\nHello World!\n");
    printf("%s",str);
}

#include <stdio.h>

int main()
{
	int a,b;
    float c,d;
    
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%f",&c);
    scanf("%f",&d);
    
    printf("%d ", a+b);
    printf("%d\n", a-b);
    printf("%.1f ", c+d);
    printf("%.1f\n", c-d);
    
    return 0;
}
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int l,n;
    
    cin>>n>>l;
    
    for(n; n< l+1; n++){
        if(n == 1) cout<<"one\n";
        else if(n==2) cout<<"two\n";
        else if(n==3) cout<<"three\n";
        else if(n==4) cout<<"four\n";
        else if(n==5) cout<<"five\n";
        else if(n==6) cout<<"six\n";
        else if(n==7) cout<<"seven\n";
        else if(n==8) cout<<"eight\n";
        else if(n==9) cout<<"nine\n";
        else if(n >9){
            if(n%2 != 0) cout<<"odd\n";
            else cout<<"even\n";
        }
    }
    return 0;
}
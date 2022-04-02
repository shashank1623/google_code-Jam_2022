#include<iostream>
#include<vector>
using namespace std;

void pattern(int r , int c)
{
for(int i=0; i<(r*2 +1); i++){
			bool flag = true;
			for(int j=0; j<(c*2+1); j++){
				if(i%2 != 0){
					if(i<2 && j<2){
						cout<<(".");
					}else{
						if(flag){
							cout<<("|");
							flag = false;
						}else{
							cout<<(".");
							flag = true;
						}
					}
				}else{
					if(i<2 && j<2){
						cout<<(".");
					}else{
						if(flag){
							cout<<("+");
							flag = false;
						}else{
							cout<<("-");
							flag = true;
						}
					}
				}
			}
		    cout<<("")<<endl;
		}   

}

int main()
{
    int t;
    cin>>t;
    int tc=1;
    while(tc<=t)
    {
        
        int row;
        cin>>row;
        int col;
        cin>>col;
        
        
        cout<<"Case #"<<tc<<": "<<endl;
        pattern(row , col);
        tc++;
    }
}

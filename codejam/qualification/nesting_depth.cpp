#include <bits/stdc++.h>

 using namespace std;

 void solve(){
     int n;
     char c[100];
     cin>>c;
     int len=strlen(c);
     for(int i=0;i<len;i++){
         int howmany;
         if(i==0){
             howmany=c[i]-'0';
             for(int j=0;j<howmany;j++){
                 cout<<'(';
             }
         }
         else{
             if(c[i]>c[i-1]){
                 howmany=c[i]-c[i-1];
                 for(int j=0;j<howmany;j++){
                     cout<<'(';
                 }
             }
             else if(c[i-1]>c[i]){
                 howmany=c[i-1]-c[i];
                 for(int j=0;j<howmany;j++){
                     cout<<')';
                 }
             }
         }
         cout<<c[i];
         if(i==len-1){
             howmany=c[i]-'0';
             for(int j=0;j<howmany;j++){
                 cout<<')';
             }
         }
     }
     cout<<endl;
 }
 int main()
 {
     int t, i=1;
     cin>>t;
     while(t--){
         cout<<"Case #"<<i<<": ";
         solve();
         i++;
     }
     return 0;
 }

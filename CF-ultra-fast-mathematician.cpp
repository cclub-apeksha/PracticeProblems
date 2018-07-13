#include<iostream>
#include<string.h>
using namespace std;
int main()
{
  char input1[128],input2[128];
  cin>>input1;
  cin>>input2;
  for(int i=0;i < strlen(input1) ;i++)
  {
    if(input1[i] != input2[i])
      cout<<"1";
    else
      cout<<"0";
  }
  return 0;
}

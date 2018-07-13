#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
  set<int> s;
  int i,n,a,b;
  cin>>n;
  cin>>a;
  for(i=0;i<a;i++)
  {
      cin>>b;
      s.insert(b);
  }
  cin>>b;
  for(i=0;i<b;i++)
  {
    cin>>a;
    s.insert(a);
  }
  if(s.size()==n)
    cout<<"I become the guy.";
  else
    cout<<"Oh, my keyboard!";
  return 0;
}

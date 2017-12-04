#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

int main(){
  cout << time(0) << endl;
  srand(time(0));
  /*  for (int i=0 ; i<20; --i){
    cout << rand()%10 << endl;
  }
  */
  string s = "Hello World";
  string s2;

  cout << s << endl;
  s2 = s + " " + s;
  cout << s2 << endl;
  cout << s2[3] << endl;
  string s3;
  s3 = s2.substr(3,5);
  cout << s3 << endl;
  
  return 0;
}

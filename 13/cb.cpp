#include <iostream>
#include <set>
#include <numeric>
using namespace std;

int lone_sum(int a, int b, int c){
  int ints[] = {a,b,c};
  int sum=0;
  set<int> newList (ints,ints+sizeof(ints)/sizeof(int));
  for(set<int>::iterator i=newList.begin(); i!=newList.end();++i)
    sum+=*i;
  return sum;
}

int caught_speeding(int speed, bool is_birthday){
  int x = 0;
  if(is_birthday) x+=5;
  if(speed < 61 + x) return 0;
  else if(speed > 80+x) return 2;
  return 1;
}

bool cigar_party(int cigars, bool is_weekend){
  return (is_weekend && cigars >= 40) || (cigars >= 40 && cigars <= 60);
}

int main(){
  cout << "Lone Sum:\n";
  cout << "The sum of 11, 10, and 11 is " << lone_sum(11,10,11) << "\n";
  cout << "The sum of 25, 3, and 31 is " << lone_sum(25,3,31) << "\n\n";

  cout << "Cigar Party:\n";
  cout << "cigar_party(50,false): " << boolalpha << cigar_party(50,false) << "\n";
  cout << "cigar_party(74,false): " << boolalpha << cigar_party(74,false) << "\n";
  cout << "cigar_party(57,true): " << boolalpha << cigar_party(57,true) << "\n\n";

  cout << "Caught Speeding:\n";
  cout << "caught_speeding(60, false):"<< caught_speeding(60,false) << "\n";
  cout << "caught_speeding(65, false):" << caught_speeding(65,false) << "\n";
  cout << "caught_speeding(86, true):" << caught_speeding(86,true) << "\n";
  cout << "caught_speeding(85, true):" << caught_speeding(85,true) << "\n\n";
}

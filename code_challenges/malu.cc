// Given an array of integers with duplicate values like
// [3, 3, 5, 2, 1, 2], write a function to remove the
// duplicates while preserving the orginal order. 
// Try to make the function time optimal and extra space
// can used if needed Using C/C++ - You can use the data
// structures the language offers
// malu@cisco.com

#include <vector>
#include <map>
#include <iostream>

using namespace std;

using ExistenceMap = map<int, bool>;
using IntVec = vector<int>;

void print_vec(const IntVec vec) {

  for (auto& elem:vec) {
    cout << elem << ' ';
  }

  cout << endl;
}

void dedup(const IntVec inp, IntVec& out) {

  ExistenceMap emap;
    
  for (auto& elem:inp) {
    if (emap.find(elem) == emap.end()){
      // If elem not in emap i.e. not a dup, add
      // to out vector; add to emap.
      out.push_back(elem);
      emap[elem] = true;
      //print_vec(out);
    } 
  }
}

IntVec test_input[] = {
		       {3, 3, 5, 2, 1, 2},
		       {2, 3, 4, 3, 3, 6, 7, 5, 6}
};
IntVec test_output[] = {
			{3, 5, 2, 1},
			{2, 3, 4, 6, 7, 5}
};

int main(int argc, char *argv[]) {
  IntVec out;

  int idx=0;
  
  for (auto ti:test_input){
    dedup(ti, out);
    assert (out == test_output[idx]);
    out.clear();
    idx++;
  }
}

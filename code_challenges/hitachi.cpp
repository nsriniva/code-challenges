#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <map>

///////////////////////////
// 1. 
///////////////////////////

using namespace std;
// input:   "ABCDEF"
// output:  "FEDCBA"

void reverse(char *p)
{
  int lp, lp2;
  
  lp = strlen(p);
  lp2 = lp/2;
  
  
  for (int i=0; i < lp2; i++){
  	char tmp;
    
  	tmp = p[i];
    p[i] = p[lp-1-i];
    p[lp-1-i] = tmp;
  }
}


///////////////////////////
// 2. 
///////////////////////////

// input:    "test", "test2", "tset"
// output:   "test2" or "tset", "test"

// explanation: remove excess words that are anagrams of other words (contain all the same letters)
void normalize(set<string> &sset)
{
  map<string, bool> str_map;
  
  for (auto str : sset) {
    sort(str.begin(), str.end());
    if (str_map.find(str) == str_map.end()) { 
      str_map[str] = true;
    } else {
      sset.erase(str);
    }
  }


}


using vec_str = vector<string>;

vec_str split(const string& data, char c, vec_str &out);

///////////////////////////
// 3. 
///////////////////////////

// "HEADER1   HEADER2   HEADER3   HEADER4\ndata1     data2     data 3    data4"

// Visualization: 
// HEADER1   HEADER2   HEADER3   HEADER4
// data1     data2     d  at a 3    data4

void parse_entries(const std::string &dataIn, std::vector<std::string> &headersOut, std::vector<std::string> &dataOut)
{
  vec_str vec ;
  
  split(dataIn, '\n', vec);
  
  split(vec[0],' ', headersOut);
  
  split(vec[1], ' ', dataOut);
  
  auto str2 = new string;
  *str2 = dataOut[2];
  
  for (int i = 3; i<= dataOut.size()-2;){
    *str2 += ' '+dataOut[i];
    dataOut.erase(dataOut.begin()+i);
  }
  dataOut[2] = *str2;
	
  return;
}


#include <string>
#include <iostream>
#include <sstream>
#include <stdint.h>
#include <cassert>
#include <vector>
#include <stdio.h>

using namespace std;

uint32_t kill_kth_bit(uint32_t n, uint8_t k){

  return n & ((-1) ^ (1<<(k-1)));
}

using bytevec = vector<uint8_t>;

uint32_t pack_bytes(bytevec a) {

  auto a_len = a.size();

  uint32_t ret = a[0];

  int shift = 8;
  
  for (int i=1;i<a_len;i++){
    ret += a[i] << shift;
    shift += 8;
  }
  return ret;
}

using int3a = int[3];

int3a kill_k_tvs[] = {
	      {37, 3, 33},
	      {37, 4, 37}
};

using bytevec = vector<uint8_t>;
struct pack_bytes_tv_t {
  bytevec bv;
  uint32_t n;
};

using pack_bytes_tvs_t = vector<pack_bytes_tv_t>;

pack_bytes_tvs_t pack_bytes_tvs = {
				   {
				    {24, 85, 0},21784
				   },
};

int main(int argc, char *argv[], char*envp[]) {

  for (auto& kill_k_tv:kill_k_tvs) {
    auto n = kill_k_tv[0];
    auto k = kill_k_tv[1];
    auto v = kill_k_tv[2];
    
    cout << n << " after killing bit "<< k << " is " << kill_kth_bit(n,k)<< ":" << v << endl;
    assert (v == kill_kth_bit(n,k));
  }

  for (auto& pack_bytes_tv:pack_bytes_tvs) {
    auto bv = pack_bytes_tv.bv;
    auto n = pack_bytes_tv.n;
    
    cout << "packing [";
    for (auto& b:bv) 
      cout << (int)b << ",";
    
    cout <<"] results in " << pack_bytes(bv) << ":" << n << endl;
    assert (pack_bytes(bv) == n);
    
  }

  auto subnet_len = 24;
  auto subnet_mask = 0xfffffff << (32-subnet_len);

  printf("subnet_len(%d) gives subnet_mask(%x)\n", subnet_len, subnet_mask);

  int a1, a2,a3,a4;
  char tmpc;
  stringstream sstr("10.11.12.13");
  sstr >> a1 >> tmpc >> a2 >> tmpc >> a3 >> tmpc >> a4;

  cout << a1 << "." << a2 << "." << a3<< "." << a4 << endl; 
}

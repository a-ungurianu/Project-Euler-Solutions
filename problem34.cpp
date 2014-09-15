#include <iostream>

using namespace std;

unsigned fact(unsigned n) {
	unsigned res = 1;
	for(unsigned i = 2; i <= n; ++i)
		res*=i;
	return res;
}

unsigned factDig(unsigned nr) {
	unsigned res = 0;
	while(nr) {
		res+=fact(nr%10);
		nr/=10;
	}
	return res;
}

const unsigned BOUND = 1e7;

int main() {
	unsigned cnt = 0;
	for(int i = 3; i < BOUND; ++i) {
		if(factDig(i)==i)
			cnt+=i;
	}
	cout << cnt;
	return 0;
}
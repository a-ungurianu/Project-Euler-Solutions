#include <vector>
#include <iostream>

using namespace std;


vector<short> cache(10000000,0);
unsigned endsIn(unsigned n) {
	if(!cache[n]) {
		unsigned nxt = 0, aux = n;
		while(aux) {
			nxt += (aux%10) * (aux%10);
			aux /= 10;
		}
		cache[n] = endsIn(nxt);
	}
	return cache[n];
}

void init() {
	cache[1] = 1;
	cache[89] = 89;
}

int main() {
	init();
	unsigned cnt = 0;
	for(unsigned i = 1; i < 10000000; ++i) {
		if(endsIn(i) == 89) {
			cnt++;
		}
	}
	cout << cnt << '\n';
	return 0;
}
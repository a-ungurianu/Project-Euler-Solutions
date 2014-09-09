#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

//How far to search
const size_t SEARCH_RANGE = 10000;

vector<bool> sieve(SEARCH_RANGE,true);
vector<unsigned> primes;
vector<unsigned> powX2;

//Generate the primes within the search range
void genPrimes() {
	for(size_t d = 2; d < SEARCH_RANGE; d++) {
		if(sieve[d]) {
			for(size_t i = 2*d; i < SEARCH_RANGE; i+=d) {
				sieve[i] = false;
			}
		}
	}
	for(size_t p = 2; p < SEARCH_RANGE; p++) {
		if(sieve[p]) {
			primes.push_back(p);
		}
	}
}

//Generate the 2*x^2 numbers(the other part of the sum)
void genPows() {
	for(unsigned i = 1; 2*i*i < SEARCH_RANGE; ++i) {
		powX2.push_back(2*i*i);
	}
}

//Initialize the two vectors
void init() {
	genPrimes();
	genPows();
}

//Check if it satisfies the conjecture
bool isGood(unsigned nr) {

	auto powPos = lower_bound(powX2.begin(), powX2.end(), nr);
	for(;powPos != powX2.begin();powPos--) {
		auto primePos = lower_bound(primes.begin(), primes.end(),nr-*powPos);
		if(*powPos+*primePos == nr)
			return true;
	}
	//Dirty fix to run the loop on the first element of powX2
	auto primePos = lower_bound(primes.begin(), primes.end(),nr-*powPos);
	if(*powPos+*primePos == nr)
		return true;

	return false;
}

int main() {
	init();
	for(size_t i = 3; i < SEARCH_RANGE; i+=2) {
		if(!sieve[i]) {
			if(!isGood(i)) {
				cout << "Found it: " << i << '\n';
				break;
			}
		}
	}
	return 0;
}
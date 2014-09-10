#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//How far to search
const size_t SEARCH_RANGE = 1000000;

vector<bool> sieve(SEARCH_RANGE,true);
vector<unsigned> primes;

//Generate the primes within the search range
void genPrimes() {
	for(size_t d = 2; d < SEARCH_RANGE; d++) {
		if(sieve[d]) {
			primes.push_back(d);
			for(size_t i = 2*d; i < SEARCH_RANGE; i+=d) {
				sieve[i] = false;
			}
		}
	}
}

bool isPrime(unsigned nr) {
	//Taking advantage of the fact that genPrimes adds the numbers in ascending order
	return binary_search(primes.begin(), primes.end(),nr);
}

bool isTruncRightPrime(unsigned nr) {
	if(nr < 10) return false;
	do {
		if(!isPrime(nr))
			return false;
	} while(nr/=10);
	return true;
}

bool isTruncLeftPrime(unsigned nr) {
	//Find the largest power of 10 smaller the the number
	//AKA: The position of the most significant digit
	unsigned p = 1;
	while(p<nr)p*=10; p/=10;

	do {
		if(!isPrime(nr))
			return false;
		nr = nr % p;
		p/=10;
	} while(nr);
	return true;
}

bool isTruncPrime(unsigned nr) {
	return isTruncLeftPrime(nr) && isTruncRightPrime(nr);
}

void test() {
	cout << boolalpha;
	// cout << "Primes: ";
	// for(auto i:primes) cout << i << ' ';
	cout << "Is 2 truncPrime: " << isTruncPrime(2) << '\n';
	cout << "Is 6 truncPrime: " << isTruncPrime(6) << '\n';
	cout << "Is 13 truncPrime: " << isTruncPrime(13) << '\n';
	cout << "Is 3797 truncPrime: " << isTruncPrime(3797) << '\n';

}

int main() {
	genPrimes();
	//test();
	size_t cnt = 0;
	unsigned prSum = 0;
	for(auto &p:primes)
		if(isTruncPrime(p)) {
			cout << p << " is a truncPrime\n";
			prSum+=p;
			cnt++;
		}
	cout << "We found " << cnt << " truncPrimes.\n";
	cout << "Their sum is: " << prSum << ".\n";

	return 0;
}
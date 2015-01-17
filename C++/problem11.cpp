#include <fstream>
#include <iostream>
using namespace std;

const size_t N = 20;

unsigned int mat[N][N];

int main() {
	ifstream in("input.txt");
	for(size_t i = 0; i < N; ++i)
		for(size_t j = 0; j < N; ++j)	
			in >> mat[i][j];

	unsigned maxProd = 0;

	for(size_t i = 0; i < N; ++i) {
		for(size_t j = 0; j < N-4; ++j) {
			unsigned currProd = 1;

			for(size_t k = 0; k < 4; ++k)
				currProd*=mat[i][j+k];

			maxProd = max(currProd,maxProd);
		}
	}
	for(size_t i = 0; i < N-4; ++i) {
		for(size_t j = 0; j < N; ++j) {
			unsigned currProd = 1;
			
			for(size_t k = 0; k < 4; ++k)
				currProd*=mat[i+k][j];

			maxProd = max(currProd,maxProd);
		}
	}

	for(size_t i = 0; i < N-4; ++i) {
		for(size_t j = 0; j < N-4; ++j){
			unsigned currProd = 1;

			for(size_t k = 0; k < 4; ++k)
				currProd*=mat[i+k][j+k];

			maxProd = max(currProd,maxProd);
		}
	}

	for(size_t i = 0; i < N-4; ++i) {
		for(size_t j = 4; j < N; ++j) {
			unsigned currProd = 1;

			for(size_t k = 0; k < 4; ++k) 
				currProd*=mat[i+k][j-k];

			maxProd = max(currProd,maxProd);
		}
	}

	cout << maxProd << '\n';
}

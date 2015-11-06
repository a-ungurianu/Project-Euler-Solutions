#include <iostream>
#include <stdint.h>

using namespace std;

int main() {

    const uint64_t limit = (1 << 30) + 1;
    uint64_t count = 0;
    for(uint64_t i = 1; i < limit; ++i) {

        if(!(i^(2*i)^(3*i))) {
            count ++;
        }
    }

    cout << count << '\n';
}
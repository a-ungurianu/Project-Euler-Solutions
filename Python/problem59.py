from csv import reader
from itertools import combinations_with_replacement

not_allowed = set(range(14,32) + range(127,256))


byte_list = map(int,[ row for row in reader(open("cipher.txt"))][0]);


possible_keys = [ [] for _ in range(3)]

for key in range(97,123):
    is_key_valid = [True]*3
    for i,byte in enumerate(byte_list):
        if (byte ^ key) in not_allowed:
            is_key_valid[i%3] = False
    for i,v in enumerate(is_key_valid):
        if v:
            possible_keys[i].append(key)

for k1 in possible_keys[0]:
    for k2 in possible_keys[1]:
        for k3 in possible_keys[2]:
            key = (k1,k2,k3)
            sample = ""
            for i in range(10):
                sample += chr(key[i%3]^byte_list[i])
            print key,sample

final_key = (103, 111, 100)

end_sum = 0
result = open("result.txt","w")
for i,byte in enumerate(byte_list):
    end_sum += final_key[i%3] ^ byte
    result.write(chr(final_key[i%3]^byte))

result.write("\n\nSum of all ASCII chars is: " + str(end_sum))


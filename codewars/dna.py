# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/python
# create a function that returns the complementary symbol
# A-T , C-G

def DNA_strand(dna):
    pairs = {'A':'T','T':'A', 'C':'G', 'G':'C'}
    complement = []
    for char in range(len(dna)):
        complement.append(pairs[dna[char]])
    return ''.join(complement)

# testing

print(f"ATTA - {DNA_strand('ATTA')}")
print(f"ACGTAA - {DNA_strand('ACGTAA')}")
print(f"ATTGC - {DNA_strand('ATTGC')}")
print(f"GTAT - {DNA_strand('GTAT')}")
print(f"AAAA - {DNA_strand('AAAA')}")
print(f"ATTGC - {DNA_strand('ATTGC')}")

with open("rosalind_revc.txt", "r") as f:
    data = f.read()

data_rev = data[::-1].strip() # gotta remove newline that occurs when reversing because Python

def complement_strand(dna_strand):
    complements = {
        "A": "T",
        "C": "G",
        "G": "C",
        "T": "A",
    }
    return "".join(list(map(lambda x: complements[x], dna_strand)))

print(complement_strand(data_rev))
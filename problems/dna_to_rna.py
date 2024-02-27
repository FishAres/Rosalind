with open("rosalind_rna.txt", "r") as f:
    data = f.read()


def transcribe_dna(dna_string):
    return "".join(list(map(lambda x: "U" if x == "T" else x, dna_string)))

print(transcribe_dna(data))



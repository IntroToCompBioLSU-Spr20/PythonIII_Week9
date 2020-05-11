# Import needed modules
import random
import copy

# The four nucleotides
nucs = ["A","C","G","T"]

# Length of sequence
seqLen = 24

# Use a for loop and random.choice() to create a random DNA sequence (startSeq) with length seqLen
startSeq = []
for _ in range(seqLen):
    startSeq.append( random.choice(nucs) )

# Set the number of time steps to simulate
steps = 20

# Create a list to hold the set of sequences from each time step in the simulation
seqs = []
seqs.append(copy.copy(startSeq))

# Use a for loop to simulate changes to the sequence across time steps
newSeq = copy.copy(startSeq)
for _ in range(steps):
    newSeq[random.randrange(seqLen)] = random.choice(nucs)
    seqs.append(copy.copy(newSeq))

# Print all sequences -- if needed, you can uncomment the code below
for i in range(steps):
    print(seqs[i])

# Print the starting sequence as a string
startSeqStr = ""
for n in startSeq:
    startSeqStr += n
print(startSeqStr)

# Print the ending sequence as a string
lastSeqStr = ""
for n in seqs[len(seqs)-1]:
    lastSeqStr += n
print(lastSeqStr)

# Print the Hamming distance between the starting and ending sequences
dist = 0
for i in range( len(startSeq) ):
    endSeq = seqs[len(seqs)-1]
    if startSeq[i] != endSeq[i]:
        dist += 1

print( "Hamming distance between first and last sequences is: " + str(dist) )

# Here is a dictionary that translates between codons in a DNA sequence and amino acids
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# Translate your ending DNA sequence into an amino acid sequence
strAA=""
for i in range(seqLen//3):
    strNewSeq=""
    for j in newSeq[i:i+3]:
        strNewSeq+=j
    strAA+=gencode.get(strNewSeq)
    
print(strAA)

# Answer: The first distance is 10. The results of the rest of runs are 8,7,8,9,13,9. All results come out randomly.

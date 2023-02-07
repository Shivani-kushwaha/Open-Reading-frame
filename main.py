def reverse_complement(seq: str):
    seq_reverse = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    complement_seq = ""
    for base in seq:
        complement_base = seq_reverse[base]
        complement_seq += complement_base
    reverse_complement_seq = complement_seq[::-1]
    return reverse_complement_seq


def findorf(seq, length):

    orf_seq = []
    i=0
    while i < len(seq)/3:
        if seq[i:i+3] == 'ATG':
            for j in range(i+3,len(seq),3):
                if (seq[j:j+3] == 'TAA') or (seq[j:j+3] == 'TAG') or (seq[j:j+3] == 'TGA'):
                    orf_seq.append(seq[i:j+3])
                    i=j+1 #doing this to avoid multiple start codons
                    break

        i+=1 #part of while loop
    for orf in orf_seq:
        if len(orf) > length:
            print(orf_seq)


def process_files(seq_file, orf_length):

    with open("output.txt", "w") as outfile:
        # echo user's input in the output file
        outfile.write(f"This program will find ORFs for sequences. When prompted, \
please enter a FASTA file with 1 or more sequences.\n\n")
        outfile.write(f"Enter FASTA file: {in_file}\n\n")
        outfile.write(f"Enter minimum length in bp for ORFs: {orf_length}\n\n")

    # get the total number of lines from the input file
    with open(seq_file, "r") as f:
        num_lines = sum(1 for line in f)
        # num_lines = 0
        # next_line = f.readline().rstrip()
        # while next_line is not None and next_line != "":
        #     next_line = f.readline().rstrip()
        #     num_lines += 1

    # extract sequences and store in a dictionary
    sequences = {}
    with open(seq_file, "r") as f:
        # iterate line by line
        for i in range(num_lines):
            try:
                next_line = f.readline().rstrip()
                # each line starts with a ">" is an id, store the id as the key
                # start an empty sequence to store its sequence
                if next_line[0] == ">":
                    seq_id = next_line
                    seq = ""
                # each line that does not begin with ">" is a sequence string
                # for the previously found id
                # concatenate the sequence and store as the value
                else:
                    seq += next_line
                sequences[seq_id] = seq

            # skip empty line in between or after sequences
            except IndexError:
                continue



    # search for ORF in the forward strand
    for key in sequences:
        findorf(sequences[key], orf_length)

    # write output
    

    # call the reverse_complement function
    for key in sequences:
        reverse = reverse_complement(sequences[key])
        findorf(reverse,orf_length)     # search for ORF in the reverse strand
    

    # write output


if __name__ == "__main__":
    # prompt user for input
    in_file = input("This program will find ORFs for sequences. Please enter \
a FASTA file with 1 or more sequences: \n")
    length = int(input("Enter minimum length in bp for ORFs: \n"))
    process_files(in_file, length)

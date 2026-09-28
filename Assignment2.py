# import libraries
import gzip
import urllib.request


#  1. read the complete sequence from the file: chr1_GL383518v1_alt
url = "https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chr1_GL383518v1_alt.fa.gz"
urllib.request.urlretrieve(url, "chr1_GL383518v1_alt.fa.gz")
print("Download complete")

sequence = ""

with gzip.open("chr1_GL383518v1_alt.fa.gz","rt") as infile:
    for line in infile:
        if not line.startswith(">"):
            sequence += line.strip()

# convert entire sequence to uppercase
sequence = sequence.upper()
print("Sequence length:", len(sequence))

# Read lines from the file and print them
    # print 10th letter of this sequence
print("10th Letter:", sequence[9])
    # print the 758th letter of this sequence
print("758th Letter:", sequence[757])
print(set(sequence))


# 2. create the reverse complement of the encoded DNA molecule used in Part 1
    # hint: Remember to reverse the sequence, and substitute the bases with their Watson-Crick-Franklin pair.
    # DNA reverse complements
complement = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C",
    "N": "N"
}

reverse_sequence = sequence[::-1]
reverse_complement = ""

for base in reverse_sequence:
    reverse_complement += complement[base]

    # print the 79th letter of sequence
print("79th Letter:", reverse_complement[78])
    # print the 500th-800th letters of sequence
print("500th through 800th Letters:", reverse_complement[499:800])


# 3. read the sequence used in part 1
    # Create a nested dictionary that contains the number of times each letter appears in the downloaded sequence,
    # as a function of which kilobase of the sequence you are looking at
    # hint: “my_dict”[5000] should contain a dictionary that has a separate key for each of the different nucleotides.
    # And “my_dict”[5000][“A”] should contain the number of times each A appears in the sequence between position 5000 and position 6000.
my_dict = {}
# process in 1000 base chunks
for start in range(0, len(sequence), 1000):
    # extract one kilobase
    chunk = sequence[start:start + 1000]
    # count nucleotides
    counts = {
        "A": chunk.count("A"),
        "C": chunk.count("C"),
        "G": chunk.count("G"),
        "T": chunk.count("T")
    }
    # store counts in nested dict
    my_dict[start] = counts

print(5000 in my_dict)
print(type(my_dict))
print(my_dict[5000])


# 4. read the dictionary in part 3
    # a. Create a list with 4 elements, containing the number of times each nucleotide (A,C,G,T) is contained in the first 1000 base pairs.
first_kilobase = [
    my_dict[0]["A"],
    my_dict[0]["C"],
    my_dict[0]["G"],
    my_dict[0]["T"]
]
print(first_kilobase)
    # b. Repeat part 4a for each kilobase contained in the dictionary.
    # c. Create a list containing each individual list from the part 4b.
all_kilobases = []

for kilobase in my_dict:
    nucleotide_list = [
        my_dict[kilobase]["A"],
            my_dict[kilobase]["C"],
            my_dict[kilobase]["G"],
            my_dict[kilobase]["T"]
    ]
    all_kilobases.append(nucleotide_list)
    print(nucleotide_list)
    # d. Calculate the sum of each list.
sum_list = []

for nucleotide_list in all_kilobases:
    sum_list.append(sum(nucleotide_list))

print(sum_list) 
    # e. Using comments in your code answer the following questions:
        # What is the expected sum for each list?
            # The expected sum for each list is 1000 because each list = 1 kilobase (1000 base pairs)
        # Are there any lists whose sums are not equal to the expected value?
            # The last lists sum is 439 instead of the expected 1000 because it is not an exact multiple of 1000.
        # Provide a general explanation for the differences in your expected results and your observed results.
            # The reason that there is a difference in the expected results and the observed results is because the sequence length (182439) isn't divisible by 1000. So the last kilobase is the remaining bases.

# 5. Write a ReadMe file meeting all the requirements described in the first assignment is a prerequisite.
 


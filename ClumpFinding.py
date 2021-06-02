# Function to return a list of K-mers that repeat atleast m times in the Text.
def PatternCount1(Text,k,m):
    list1 = []
    counter = 0
    array1 = []
    
    for i in range(len(Text)-k+1):
        word = Text[i:(i + k)]
        list1.append(word)    
    list2 = set(list1)
    
    for i in list2:
        counter = list1.count(i)
        if counter >= m:
            array1.append(i)
    return array1
#Function to find patterns forming clumps in a string.
#Input: A string Genome, and integers k, L, and m.
#Output: All distinct k-mers forming (L, m)-clumps in Genome.    

def PatternCount2(Text,k,L,m):
    dic = {}
    count = 0
    z = 0
    a = 0
    p = []
    for i in range(len(Text)-L+1):
        word = Text[i:(i + L)]
        a = PatternCount1(word,k,m)
        l = len(a)

        if l in dic:
            if (l != 0) and (sorted(a) not in dic[l]):      # To avoid repetition
                dic[l].append(sorted(a))             
        else:
            dic[l] = [a]
            
        z = max(z, l)    

    for i in range(len(dic[z])):                            # Modifying output according to requirement
        p.append(dic[z][i][0])
    print(" ".join(p))

#path = 'ecoli.txt'
#file1 = open(path, 'r')
PatternCount2('CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG',3,25,3)
#file1.close()


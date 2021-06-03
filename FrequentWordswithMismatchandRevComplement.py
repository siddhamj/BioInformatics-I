import itertools
def PermuteMotifOnce(motif, alphabet={"A", "C", "G", "T"}):
    """
    Gets all strings within hamming distance 1 of motif and returns it as a
    list.
    """
    return list(set(itertools.chain.from_iterable([[
        motif[:pos] + nucleotide + motif[pos + 1:] for
        nucleotide in alphabet] for
        pos in range(len(motif))])))

def PermuteMotifDistanceTimes(motif, d):
    workingSet = {motif}
    for _ in range(d):
        workingSet = set(itertools.chain.from_iterable(map(PermuteMotifOnce, workingSet)))
    return list(workingSet)

output = []
def removeNestings(l):
    for i in l:
        if type(i) == list:
            removeNestings(i)
        else:
            output.append(i)
    return output

def RevComp(Pattern):
    def reverse(x):
      return x[::-1]
    reversed = list(reverse(Pattern))
    for i,j in enumerate(reversed):
        if j == "A":
            reversed[i] = "T"
        elif j == "T":
            reversed[i] = "A"
        elif j == "G":
            reversed[i] = "C"
        elif j == "C":
            reversed[i] = "G"
        else:
            print("ERROR: INCORRECT NUCLEOTIDE SEQUENCE")
            return
    return ("".join(reversed))

def hamming(string1, string2):
    count = 0
    for (i,j) in zip(string1, string2):
        if i != j:
            count += 1
            
    return count

def Count(Text, Pattern, d):
    array1 = []
    for i in range(len(Text)-len(Pattern)+1):
        if hamming(Pattern, Text[i:(i + len(Pattern))]) <= d:
                array1.append(Text[i:(i + len(Pattern))])
    
    return len(array1)

def freqwordmis(Text, k, d):
    list1 = []
    list3 = []
    dic1 = {}
    for i in range(len(Text)-k+1):
        word = Text[i:(i + k)]
        list1.append(word)        
    
    list1 = list(set(list1))

    for i in list1:
        list3.append(PermuteMotifDistanceTimes(i, d))
        
    list3 = list(set(removeNestings(list3)))
    list2 = (list1 + list3)  
    list4 = list(set(list2))

    for i in list4:
        sj = (Count(Text, i, d) + Count(RevComp(Text), i, d))     # Remove revComp((Text),i,d) for *just* freq word mismatch problem
        if sj in dic1.keys():
            dic1[sj].append(i)
        else:
            dic1[sj] = [i]
             
    return dic1

z = freqwordmis('TTGTGTGTGTGTGTTTTCTCTCTAAAACTAATTGTAAAATTAAGTTTTTAAAATTAAAAGTAATTAAAACTCTAAAAGT', 5, 2)
max_key = max(z.keys())
ans = z[max_key]
print(" ".join(ans))
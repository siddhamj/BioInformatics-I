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
    
def PatternCount2(Text,k,L,m):
    dic = {}
    count = 0
    z = 0
    a = 0
    for i in range(len(Text)-L+1):
        word = Text[i:(i + L)]
        a = PatternCount1(word,k,m)
        l = len(a)
        if l in dic:
            if sorted(a) not in dic[l]:
                dic[l].append(sorted(a))
        else:
            dic[l] = [a]
            
        z = max(z, l)
        
    print(dic[z])
    
path = 'ecoli.txt'
file1 = open(path, 'r')
PatternCount2('CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG',3,25,3)
file1.close()


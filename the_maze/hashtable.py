from collections import defaultdict


def groupAnagrmas(words:list):
    res=defaultdict(list)

    for i in words:
        count=[0]* 26


        for c in i:
            count[ord(c)-ord("a")]+=1

        res[tuple(count)].append(i)
    return res.values()        


wrds1=["eat", "tea", "tan", "ate", "nat", "bat"]
wrds2=[""]
wrds3=["a"]
ans1=groupAnagrmas(wrds1)
print(ans1)
print()
ans2=groupAnagrmas(wrds2)
print(ans2)
print()
ans3=groupAnagrmas(wrds3)
print(ans3)

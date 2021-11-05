# def sockMerchant(n, ar):
#     # Write your code here
#     numberOfPairs=0
#     while(len(ar)>1):
#         j=0
#         if(ar[0]==ar[j]):
#             numberOfPairs+=1
#             ar.pop(0)
#             ar.pop(j)
#         else:
#             if(ar[0]==ar[-1]):
#                 ar.pop(0)
#                 ar.pop(j)
#         j+=1
#     print(numberOfPairs)

def sockMerchant (n, ar):
    socksCount = {}
    pairsCount = 0
    for i in ar:
        if i in socksCount:
            socksCount[i] += 1
        else:
            socksCount[i] = 1
    print(socksCount)
    for i in socksCount.values():
        if i >= 2:
            pairsCount += int(i/2)
    print(pairsCount)
    return pairsCount
sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])
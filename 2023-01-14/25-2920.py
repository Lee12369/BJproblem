ascending = [i for i in range(1,9)]
descending = [9-i for i in range(1,9)]
numbers = list(map(int,input().split()))
if numbers == ascending:
    print("ascending")
elif numbers == descending:
   print("descending")
else:
    print("mixed")
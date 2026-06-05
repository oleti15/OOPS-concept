# N=int(input())
# arr=list(map(int,input().split()))
# print(min(arr))

# N=int(input())
# arr=list(map(int,input().split()))
# print(min(arr))

# 2nd smallest number
# N=int(input())
# arr=list(map(int,input().split()))
# arr.sort()
# print(arr[1])

# 2nd largest element 
# N=int(input())
# arr=list(map(int,input().split()))
# arr.sort()
# print(arr[-2])

# remove duplicates
# N=int(input())
# arr=list(map(int,input().split()))
# s=set(arr)
# print(s)

# reverse array
# N=int(input())
# arr=list(map(int,input().split()))
# print(arr[::-1])

# frequence count
# N=int(input())
# arr=list(map(int,input().split()))
# frq={}
# for i in arr:
#     if i in frq:
#         frq[i]+=1
#     else:
#         frq[i]=1
# for i in frq:
#     print(i,frq[i])

# find repeating number
# N=int(input())
# arr=list(map(int,input().split()))
# frq={}
# for i in arr:
#     if i in frq:
#         frq[i]+=1
#     else:
#         frq[i]=1
# for i in frq:
#     if frq[i]>1:
#         print(i)

# find non repeating 
# N=int(input())
# arr=list(map(int,input().split()))
# frq={}
# for i in arr:
#     if i in frq:
#         frq[i]+=1
#     else:
#         frq[i]=1
# n=[]
# for i in frq:
#     if frq[i]==1:
#         n.append(i)
# print(n)

# rotate array by k
# N=int(input())
# arr=list(map(int,input().split()))
# k=int(input())
# print(arr)
# print(arr[-k:]+arr[:-k])

# equlibrium
# N=int(input())
# arr=list(map(int,input().split()))
# for i in arr:
#     left_sum=sum(arr[i:])
#     right_sum=sum(arr[:i+1])
#     if left_sum==right_sum:
#         print(i)
#         break
   
#  maximum product of array
# N=int(input())
# arr=list(map(int,input().split()))
# product=1
# for i in arr:
#     product*=i
# print(product)

# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# if N % 2 == 1:
#     median = arr[N // 2]
# else:
#     median = (arr[N // 2 - 1] + arr[N // 2]) / 2

# print(median)

# N = int(input())
# a=list(map(int,input().split()))
# m=int(input())
# b=list(map(int,input().split()))
# for i in a:
#     if i in b:
#         print("YES")
#         break
# else:
#     print("NO")

# search element
# N=int(input())
# arr=list(map(int,input().split()))
# t=int(input())
# for i in arr:
#     if i==t:
#         print("Found")
#         break
# else:
#     print("Not Found")


# symmetric pairs
# N = int(input())
# pairs = []
# for i in range(N):
#     a, b = map(int, input().split())
#     pairs.append((a, b))
# for a, b in pairs:
#     if (b, a) in pairs:
#         print(a, b)
#         break

# N = int(input())
# pairs = []
# d = {}
# l = []
# for i in range(N):
#     a, b = map(int, input().split())
#     if b in d and d[b] == a:   
#         l.append([b, a])      
#     else:
#         d[a] = b              
# for pair in l:
#     print(pair[0], pair[1])

# missing number
# N=int(input())
# arr=list(map(int,input().split()))
# ex=sum(range(min(arr),max(arr)+1))
# missing=ex-sum(arr)
# print(missing)

# N=int(input())
# arr=list(map(int,input().split()))
# total=N*(N+1)//2
# arr_sum=sum(arr)
# print(total-arr_sum)

# pair sum
# N=int(input())
# arr=list(map(int,input().split()))
# target=int(input())
# for i in arr:
#     for j in arr:
#         if i+j==target:
#             print(i,j)


# leader number
# n=int(input())
# a=list(map(int,input().split()))
# for i in range(len(a)):
#     if a[i]==max(a[i:]):
#         print(a[i],end=" ")


# union and intersection
# N1 = int(input())
# arr1 = list(map(int, input().split()))
# N2 = int(input())
# arr2 = list(map(int, input().split()))
# set1 = set(arr1)
# set2 = set(arr2)
# union_result = sorted(set1.union(set2))
# intersection_result = sorted(set1.intersection(set2))


# print("Union:", *union_result)
# print("Intersection:", *intersection_result)


# Maximum subarray
# n=int(input("Enter range"))
# l=list(map(int,input().split()))
# sum=0
# temp=0
# max_sum=0
# for i in l:
#     sum+=i
#     if sum<0 and temp<=sum:
#         temp=sum
#         sum=0
#     elif sum<0 and temp>sum:
#         sum=max(temp+sum,sum)
#         if sum<0:
#             sum=0
#     max_sum=max(max_sum,sum)
# print(max_sum)

#  maximum sub array
# n=int(input())
# l=list(map(int,input().split()))
# ms=l[0]
# for i in range(n):
#     s=0
#     for j in range(i,n):
#         s=s+l[j]
#         ms=max(ms,s)
# print(ms)

# a=int(input())
# r=int(input())
# n=int(input())
# gp_sum=0
# if r==1:
#     gp_sum=a*n
# else:
#     gp_sum=a*(r**n)//(r-1)
# print(gp_sum)
# n=int(input())
# a=int(input())
# r=int(input())
# sum=0
# for i in range(n):
#     p=a*(r**i)
#     sum+=p
# print(p)

# strong number
# fact=1
# n=int(input())
# while n>0:
#     d=n%10
#     fact=fact*d
#     n//=10
# print(fact)

# Prime Factors
# l=[]
# n=int(input())
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         l.append(i)
# print(l)
# for i in l:
#     if n%i==0:
#         print(i,end=" ")

# Harshad number
# num=int(input())
# sum=0
# while num!=0:
#     d=num%10
#     sum+=d
#     num//=10
# if num%sum==0:
#     print("Harshad Number")
# else:
#     print("Not Harshad Number")

# Abundunt
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     if n%i==0:
#         sum+=i
# if sum>n:
#     print("abundunt")
# else:
#     print("Not abundunt")


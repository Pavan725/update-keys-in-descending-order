@@ -1,5 +1,5 @@
def most_frequent():
    str=input('enter a string')
def most_frequent(str):

    d=dict()
    for i in str:
        if i in d:
@@ -10,4 +10,4 @@ def most_frequent():
    for r in d_sort:
        print(r,'=',d[r])

most_frequent()
most_frequent(input("enter the string")) 
0 comments on commit 1d0d04e

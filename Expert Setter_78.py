# cook your dish here

for t in range(int(input())):
    a,b=map(int,input().split())
    if b/a >=0.5:
        print("Yes")
    else :
        print("No")

Problem
A problem setter is called an expert if at least 50 \%50% of their problems are approved by Chef.

Munchy submitted XX problems for approval. If YY problems out of those were approved, find whether Munchy is an expert or not.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of a two space-separated integers XX and YY - the number of problems submitted and the number of problems that were approved by Chef.

Output Format
For each test case, output on a new line YES, if Munchy is an expert. Otherwise, print NO.

The output is case-insensitive. Thus, the strings YES, yes, yeS, and Yes are all considered the same.

4
5 3
1 1
4 1
2 1
YES
YES
NO
YES

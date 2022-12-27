# cook your dish here
# 1 Kg ----- 1000 make pages 
# 1 notebook -------100 pages 

for t in range(int(input())):
    a=int(input())
    print(int((a*1000)/100))



"""

Problem
You know that 11 kg of pulp can be used to make 10001000 pages and 11 notebook consists of 100100 pages.

Suppose a notebook factory receives NN kg of pulp, how many notebooks can be made from that?

Input Format
First line will contain TT, the number of test cases. Then the test cases follow.
Each test case contains a single integer NN - the weight of the pulp the factory has (in kgs).
Output Format
For each test case, output the number of notebooks that can be made using NN kgs of pulp.

Input

3
1
100
50
Output
10
1000
500

"""

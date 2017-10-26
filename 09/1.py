'''
Leha is a young man from Belarus. He loves cakes really much. In Leha's country, cakes are always evenly divided between people.

Leha wants to know how many people he should invite to his party if he has a cake whose size is equal to u units and he wants each person to get exactly  A/B units of cake. 

Note that Leha doesn't take a piece for himself; in other words, the cake is only divided among the people he invited to the party.

Write a function divide(A,B,u) that returns a single integer denoting the number of people he should invite to his party

For example:

divide(5,10,1)  would return 2 because each person would get 5/10 or 1/2 units of cake so he invites 2 people and the cake is distributed between them.

The answer should always be an integer.
'''

def divide(A,B,u):
    return int(u/(A/B))

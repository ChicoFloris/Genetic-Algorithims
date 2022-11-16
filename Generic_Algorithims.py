import random           # to be able to generate/manipulate random numbers

#defenition for the problem
def foo(x,y,z):
    return 6*x**3 + 9*y**2 + 90*z -25

#Defining the fitness function
def fitness(x,y,z):
    ans = foo(x,y,z)

    if ans == 0:
        return 99999        #this is the conditon for the perfect solution
    else:
        return abs(1/ans)   # absoulte because we want all the answer closest to zero
                            # 1/ans will give us a big number, hence metric to evaluate our soulution

#genertating soulution
solution = []                                       # the list where the solution will be stored
for s in range(1000):                               # range 1000 refers to the number of solution we are trying to generate.
    solution.append( (random.uniform(0,10000),      # append is used to add items to the end of a given list. To add a single item to the end of the list or to populate a list using a for loop.
                      random.uniform(0,10000),      # This is called a tuple becuase we are storing multiple items in a sigle variable. TUPLES ARE ORDERED, UNCHANGABLE, AND ALLOW DUPLICATE VALUES. T
                      random.uniform(0,10000)))     #uniform is used to return a random floating number between the two sepcified number (both included)
                                                    #basically we created a tuple for solution containing 3 random floating numbers between 0-10,000


 # Testing code: print (solution[:5]) returns the first 5 solutions generated by our for loop. 5 set of truples containg 3 random floating numbers between 0-10,000

for i in range(10000):

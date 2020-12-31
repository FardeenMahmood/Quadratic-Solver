"""This program finds the discriminant, the number of solutions in a quadratic
    equation, and it also solves for it's solutions given the values of
    a, b, and c"""

def discriminant(a,b,c):
    """Calculates the discriminant""" 
    D = b ** 2 - 4 * a * c
    return D
    
def num_solutions(a,b,c):
    """Checks for the number of solutions based on the value of the
    discriminant"""
    D = discriminant(a,b,c)
    if D > 0:
        return("There are two solutions.") 
    elif D == 0:
        return("There is one solution.")           
    else:
        return("There are no solutions.")

def solve(a,b,c):
    """Solves the quadratic equation based on the value of the discriminant
    where 1 solution, 2 solutions or no solutions can be given""" 
    D = discriminant(a,b,c)
    #If the discriminat was greater than 0, calculations for 2 roots are made
    if D > 0:
        root1 = (-b + D ** 0.5) / (2 * a)
        root2 = (-b - D ** 0.5) / (2 * a)
        return("The roots are {:.2f} and {:.2f}".format(root1, root2))
    #If the discriminant was equal to 0, calculations for 1 root is made
    elif D == 0:
        root = -b / (2 * a)
        return("The root is {}".format(root))
    #If the discriminant was less than 0, no calculations are made
    else:
        return("The roots are imaginary")

def main():
    #Gets the values of a, b, and c
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(discriminant(a,b,c))
    print(num_solutions(a,b,c))
    print(solve(a,b,c))

main()

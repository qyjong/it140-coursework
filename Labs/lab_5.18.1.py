
# takes two values as input, then assigns val1 to val2, and val2 to val1,
# then returns the two values
def swap_values(user_val1, user_val2):
    user_val1, user_val2 = user_val2, user_val1
    return user_val1,user_val2

if __name__ == '__main__': 
    # get two values as input
    val1 = int(input())
    val2 = int(input())
    # call swap_values function to swap val1 and val2
    val1,val2 = swap_values(val1, val2)
    # output the swapped results
    print(val1, val2)
    
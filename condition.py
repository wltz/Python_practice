def condition_test():
    """
    Falsy values (code under if not root: runs):
    None, 
    0,
    False
    "",
    [], {}, set()
    """
    lst = []
    if lst:
        print("lst is not empty")
    else:
        print("lst is empty")

    if not lst:
        print("lst is empty")
    else:
        print("lst is not empty")

    while lst:    
        lst.pop()
        print("lst is not empty")
    else:
        print("lst is empty")



if __name__ == "__main__":
    condition_test()
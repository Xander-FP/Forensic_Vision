def isTrue(flag):
    if flag == "y":
        return True
    else:
        return False
    
def removeSuffix(input, suffix):
    if suffix and input.endswith(suffix):
        return input[:-len(suffix)]
    else:
        return input
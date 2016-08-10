# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def unpack_nested(list_int):     
    new_list = []
    for each_item in list_int:
        if isinstance(each_item, int):
            new_list.append(each_item)
        else:
            new_list += unpack_nested(each_item)     
    return new_list

def nested_sum(list_int):
    new_list = unpack_nested(list_int)
    result = sum(new_list)
    return result   

def main():
    pass

if __name__ == '__main__':
    main()

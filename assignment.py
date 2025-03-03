# TODO 1: Detele this line and create a docstring

def _initialize_names():
    """
    function that initializes nammes
    :return: List of names
    """
    return ["juan", "michael", "steve", "jimmy", "tony", "merle", "willie"]

def _initialize_numbers():
    """
    function that initializes numbers
    :return: List of numbers
    """
    return ["708-555-9878", "630-555-0009", "630-555-1112", "515-555-9999", 
               "847-555-4443", "312-555-9823", "414-555-6767"]

def _initialize_dictionary():
    """
    function that initializes an empty dictionary, then adds names and numbers from initialization
    :return: dictionary of {names : numbers}
    """

    pass
    # TODO 2: Delete pass above. Create a variable called names and set it to the output of _initialize_names().
    # create a variable called numbers and set it to the output of _initialize_numbers()
    # create a variable called a_dict and initialize it to an empty dictionary


    # TODO 3: iterate over names and numbers, and add the key:value pairs to a_dict()
    # hint: for advanced students, look into using the zip function to iterate over names and numbers as a list of 2-tuples

    
    # TODO 4: return the dictionary

def create_new_name_and_number(a_dict):
    """
    A void Function that takes a dictionary of {names:numbers} and prompts for user input to add a new Key:Value pair to the dictionary.
    This will keep prompting for a new key if they enter one that already exists.

    :param: :a_dict: a dictionary of name:phone_number values
    """

    pass
    # TODO 4: delete pass above. Create a variable called keys that has all the keys (aka names) in a_dict
    # hint: review .keys() funct: https://docs.python.org/3/library/stdtypes.html#dict.keys


    # TODO 5: Prompt user to enter a new name. While that name already exists in keys, prompt them for a new name
    # Once they enter a name that does not already exist as a key, prompt them for a phone number
    # Then set the key/value pair in a_dict. Hint: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    # d[key] = value

def update_phone_number(a_dict):
    """
    A void function that takes a dictionary of {names:numbers} and prompts for user input to update a Key:Value pair to the dictionary

    :param: :a_dict: a dictionary of name:phone_number values
    """

    pass
    # TODO 6: delete pass above. Create a variable called keys that has all the keys (aka names) in a_dict
    # hint: review .keys() funct: https://docs.python.org/3/library/stdtypes.html#dict.keys


    # TODO 7: Prompt user to enter a new name. While that name does not already exists in keys, prompt them for a new name
    # Once they enter a name that does exist, prompt them for a phone number.
    # Then update that key/value pair in a_dict.  Hint: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    # d[key] = value

def main():
    """
    Main function to tie all the above together
    """

    # Initialize dictionary
    a_dict = _initialize_dictionary()

    # Add a new name/number
    create_new_name_and_number(a_dict)

    # Update an existing phone number
    update_phone_number(a_dict)

    # TODO 8: print the updated dictionary


if __name__ == "__main__":
    #note you can test individual functions above if needed
    #a_dict = _initialize_dictionary()
    #print(a_dict)
    #update_phone_number(a_dict)
    #etc

    #otherwise, yo can run main
    main()
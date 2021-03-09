"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    #creates a list of numbers called incoming_list
    first_incoming_list = ['2', '8', '15', '16', '23', '42']

    #find the greates number in the list 
    logging.debug("Greatest number in list is: %d", max(incoming_list) )

    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    pass


def find_least_number(incoming_list):

    #use second list, but find least number
    second_incoming_list = ['2', '8', '15', '16', '23', '42']
    logging.debug("Smallest number in the list is: %d", min(incoming_list))

    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    pass


def add_list_numbers(incoming_list):
    #use the sum() function to add the numbers together in the third list
    third_incoming_list = ['2', '8', '15', '16', '23', '42']
    logging.debug("Sum of numbers in the list is: %d", sum(incoming_list))

    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """

    pass


def longest_value_key(incoming_dict):
    #create dictionary
    incoming_dict = {"animals": "monkey", "points": 3}
    logging.debug("Incoming_dicts animal is: ", incoming_dict["animals"])
    logging.debug("Incoming_dicts point value is: ", incoming_dict["points"])

    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    pass

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    #loop through the weights
    for first_index, item in enumerate(weights):
        #check if limit - item is in ht
        if hash_table_retrieve(ht, (limit-item)) is not None:
            #get the index of the limit - item
            second_index = hash_table_retrieve(ht, (limit - item))
            #since the order matters, check the size of the index
            #of the weights and return in the correct order
            if first_index > second_index:
                return [first_index, second_index]
            else:
                return [second_index, first_index]
        # otherwise, add item and index to the tuple as key/value pair
        else:
            hash_table_insert(ht, item, first_index)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

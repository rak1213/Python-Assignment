# Question 1 : Implement stack and queue using List
# stack - LIFO
# queue - FIFO


def stack(list, operation, data=None):
    """
    Perform stack operations (LIFO - Last In First Out) on a given list.

    Args:
    lst (list): The list on which stack operations are to be performed.
    operation (str): The operation to perform. 'add' to push an item onto the stack, 'remove' to pop an item from the stack.
    data (optional): The data to be added to the stack. Required if operation is 'add'.

    Returns:
    list: The updated list after performing the stack operation.
    """
    if operation == "add" and data is not None:
        list.insert(0, data)
    elif operation == "remove":
        if len(list) > 0:
            list.pop(0)
        else:
            print("The stack is empty, cannot remove element!")
    else:
        print("Invalid Operation!")
    return list


def queue(list, operation, data=None):
    """
    Perform queue operations (FIFO - First In First Out) on a given list.

    Args:
    lst (list): The list on which queue operations are to be performed.
    operation (str): The operation to perform. 'add' to enqueue an item, 'remove' to dequeue an item.
    data (optional): The data to be added to the queue. Required if operation is 'add'.

    Returns:
    list: The updated list after performing the queue operation.
    """
    if operation == "add" and data is not None:
        list.append(data)
    elif operation == "remove":
        if len(list) > 0:
            list.pop(0)
        else:
            print("The queue is empty, cannot remove element!")
    else:
        print("Invalid Operation!")
    return list


# Main execution
if __name__ == "__main__":
    new_list = [1, 2, 3, 4]
    print("Original list")
    print(new_list)
    print("*-" * 20)
    print("Stack Operations")
    print("Adding new element to the Stack")
    new_list = stack(new_list, "add", 0)
    print(new_list)
    print("Remove an element from Stack")
    new_list = stack(new_list, "remove")
    print(new_list)
    print("*-" * 20)
    print("Queue Operations")
    print("Adding new element to the Queue")
    new_list = queue(new_list, "add", 5)
    print(new_list)
    print("Remove an element from the Queue")
    new_list = queue(new_list, "remove")
    print(new_list)

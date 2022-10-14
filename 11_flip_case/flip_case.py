from hashlib import new


def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_str = ''
    for char in phrase:
        if char.lower() == to_swap.lower():
            new_str += (char.swapcase())
        else:
            new_str += char
    return new_str


print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))

# SB SOLUTION*************
    # you can reassign iteration item in a for loop
    
    # to_swap = to_swap.lower()
    # out = ""

    # for ltr in phrase:
    #     if ltr.lower() == to_swap:
    #         ltr = ltr.swapcase()
    #     out += ltr

    # return out
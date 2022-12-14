def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    all_true = [itm for itm in lst if (not not itm) == True]
    return all_true

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))


# Redundant - see below how to slim out boolean logic


    # return [val for val in lst if val]
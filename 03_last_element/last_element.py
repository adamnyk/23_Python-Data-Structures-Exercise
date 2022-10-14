def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """

    if len(lst) == 0:
        return None
    else:
        return lst[-1]

#alt solution
#  DAYS = [
#         "Sunday",
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#     ]

#     if day_of_week < 1 or day_of_week > 7:
#         return None

#     return DAYS[day_of_week - 1]

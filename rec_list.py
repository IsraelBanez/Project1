# Node list is
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist):
    if strlist is None:
        return None
    if strlist.rest is None:
        return strlist.value
    if strlist.value < strlist.rest.value:
         temp = strlist.value
         strlist.value = strlist.rest.value
         strlist.rest.value =temp
    return first_string(strlist.rest)


# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist):
    if strlist is None:
        return None, None, None
    rlist = split_list(strlist.rest)
    if strlist.value[0] in 'a,e,i,o,u,A,E,I,O,U':
        return Node(strlist.value, rlist[0]), rlist[1], rlist[2]
    if strlist.value[0].isalpha() and not strlist.value[0] in 'a,e,i,o,u,A,E,I,O,U':
        return rlist[0], Node(strlist.value, rlist[1]), rlist[2]
    if not strlist.value[0].isalpha():
        return rlist[0], rlist[1], Node(strlist.value, rlist[2])
    return rlist[0], rlist[1], rlist[2]

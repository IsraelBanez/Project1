# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []


def perm_gen_lex(str_in):
    if str_in is '':
        return []
    if str_in is None:
        return None
    if len(str_in) == 1:
        return [str_in]
    emptyL = []
    for i in range(len(str_in)):
        simplestr = str_in[i:i + 1]
        for j in perm_gen_lex(str_in[:i] + str_in[i+1:]):
            emptyL.append(simplestr + j)
    return emptyL


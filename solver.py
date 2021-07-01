def solver(dawg,letters):
    """ Return a list of all possible words made of letters in 'letters' that
    are in the dawg """
    node = dawg.root

    list_words = []
    actualword = ""
    remindingletters = list(letters)

    for letter in letters: # First letter which will compose words
        node = dawg.root
        if letter in node.edges:

            actualword = letter
            remindinglettersbis = remindingletters.copy()
            remindinglettersbis.remove(letter)
            node = node.edges[letter]
            next_node(node,actualword,remindinglettersbis,list_words)
    return list_words


def next_node(node,actualword,remindingletters,list_words):

    """ Recursive function looking if child of node are in reminding letters"""

    actualword = actualword
    remindingletters = remindingletters
    for label,child in sorted(node.edges.items()):

        if remindingletters == []:break # avoid searching if we used all letter

        if label in remindingletters:
            actualword2 = actualword + label
            remindingletters2 = remindingletters.copy()
            remindingletters2.remove(label)
            node = child

            if node.final:
                list_words.append(actualword2)
            next_node(node,actualword2,remindingletters2,list_words)

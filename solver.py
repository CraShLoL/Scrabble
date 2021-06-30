# idea to solv scrabble :
# not working yet ! 

def solver(dawg,letters):
    
    node = dawg.root

    list_words = []
    actualword = ""
    remindingletters = list(letters)
    
        
    for reminding in remindingletters : 
        print("remindings",remindingletters)
        for label, child in sorted(node.edges.items()):
            print("on cherche", reminding)
            print('label:',label,"child:",child)
            # On parcours le dawg jusqu'a obtenir une lettre différente, soit la fin d'un mot

            if label == reminding:
                print("lettre",label,"\n\n")
                remindingletters.remove(reminding)
                actualword += reminding
                print("mot actuel",actualword)
                print("lettre restantes",remindingletters)
                node = child
                break

        print("past break2")
        print("node post break",node ,actualword,remindingletters)

            
    if node.final:
        print("wow")
        list_words.append(actualword)
        
        
##Other approach with recursive function 

def solver2(dawg,letters):

    node = dawg.root

    list_words = []
    actualword = ""
    remindingletters = list(letters)

    for letter in letters: # 1ere lettre qui va composer les mots
        node = dawg.root

        if letter in node.edges:


            actualword = letter
            remindingletters.remove(letter)
            node = node.edges[letter] # La node devient l'enfant
            print("mot actuel:",actualword)
            print("lettre restante",remindingletters)


            next_node(node,actualword,remindingletters)



def next_node(node,actualword,remindingletters):

    print(node.edges.items())
    print("mot actuel::",actualword)
    for label,child in sorted(node.edges.items()):
        if label in remindingletters:
            actualword += label
            remindingletters.remove(label)
            node = child # on descend d'un etage dans le dawg

            next_node(node,actualword,remindingletters)

            print("mot actuel:",actualword)
            print("lettre restante",remindingletters)

        else :
            print(label,"pas dedans ")

        
    return list_words


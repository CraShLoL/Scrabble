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
        
    return list_words


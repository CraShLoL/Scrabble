# Scrabble

Implementation of a Scrabble solver 

## Source 
I would to give a particular thanks to the author or 
- https://www.cs.cmu.edu/afs/cs/academic/class/15451-s06/www/lectures/scrabble.pdf
- http://stevehanov.ca/blog/index.php?id=115


## Data architecture:

A simple list or dictionnary would take too much space and too much time to itterate on.  
A tree or trie could do the job, but a Dawg (Directed Acyclic Word Graph)  seems to be better because it is taking way less places and it's easier to browse for a word we are looking for.  
(This is what I understood, feel free to correct me !)  

## Dawg - Directed Acyclic Word Graph 
A Dawg is a particuliar data structure really powerfull for indexing text, which is perfect for our Scrabble.  

If you are interested in building you Dawg here is how to do :  

"To build our DAWG, we're going to use an algorithm described in  Incremental Construction of Minimal Acyclic Finite-State Automata by Daciuk, Mihov, Watson, and Watson . For this we need as input a sorted list of words. We will construct a graph by adding one word at a time. The letters of the word will be represented by edges, while nodes will represent possible branching points. A node can also be denoted as terminal, which represents that you could end there and have a valid word. What we're building is essentially a minimized trie. For another explanation see  Compressing dictionaries with a DAWG by Steve Hanov .

The algorithm consists of two parts, insertion and minimization. As we loop over the collection of words, we keep track of our position on the graph, as well as the previous word processed. For each new word, we begin by back-tracking to the node representing the common prefix of it and the previous word. As we do so, we minimize the right-hand part of the tree, the suffixes if you will. To minimize, from each node as we back-track, we look to the previously constructed parts of the tree and see if we find an identical one. Nodes are considered identical if they have the same terminal state, same outgoing edges, and for each of those edges, the children of both nodes are identical. Following the minimization to the common prefix, we insert the next word by adding edges and nodes from the current one. The last node is marked as terminal since the word ends there. After we've finished adding all the words, we'll minimize back to the root node."  
Source : https://jbp.dev/blog/dawg-basics.html

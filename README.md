# Scrabble

I'll try to implement an algortihm to solve scrabble.  
Given a couple of letters it should output the best possibles words according to their points.

Following the amazing content available here : https://www.cs.cmu.edu/afs/cs/academic/class/15451-s06/www/lectures/scrabble.pdf


## Table of Contents

* [Data architecture](#Data-architecture)
* [Backtracking](#Backtracking)
* [Dawg : Directed Acyclic Word Graph](#Dawg - Directed Acyclic Word Graph)
* [Installation](#Installation)
* [Contributions](#Contributions)


## Data architecture

A simple list or dictionnary would take too much space and too much time to itterate on.  
A tree or trie could do the job, but a Dawg (Directed Acyclic Word Graph)  seems to be better because it is taking way less places and it's easier to browse for a word we are looking for.  
(This is what I understood, feel free to correct me !)  

## Backtracking

"Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree)."   
Source : https://www.geeksforgeeks.org/backtracking-introduction/#:~:text=Backtracking%20is%20an%20algorithmic%2Dtechnique,reaching%20any%20level%20of%20the

## Dawg - Directed Acyclic Word Graph 
A Dawg is a particuliar data structure really powerfull for indexing text, which is perfect for our Scrabble.  

If you are interested in building you Dawg here is how to do :  

"To build our DAWG, we're going to use an algorithm described in  Incremental Construction of Minimal Acyclic Finite-State Automata by Daciuk, Mihov, Watson, and Watson . For this we need as input a sorted list of words. We will construct a graph by adding one word at a time. The letters of the word will be represented by edges, while nodes will represent possible branching points. A node can also be denoted as terminal, which represents that you could end there and have a valid word. What we're building is essentially a minimized trie. For another explanation see  Compressing dictionaries with a DAWG by Steve Hanov .

The algorithm consists of two parts, insertion and minimization. As we loop over the collection of words, we keep track of our position on the graph, as well as the previous word processed. For each new word, we begin by back-tracking to the node representing the common prefix of it and the previous word. As we do so, we minimize the right-hand part of the tree, the suffixes if you will. To minimize, from each node as we back-track, we look to the previously constructed parts of the tree and see if we find an identical one. Nodes are considered identical if they have the same terminal state, same outgoing edges, and for each of those edges, the children of both nodes are identical. Following the minimization to the common prefix, we insert the next word by adding edges and nodes from the current one. The last node is marked as terminal since the word ends there. After we've finished adding all the words, we'll minimize back to the root node."  
Source : https://jbp.dev/blog/dawg-basics.html  
Implementation : http://stevehanov.ca/blog/index.php?id=115


## Installation

Clone the repo

```
git clone https://https://github.com/CraShLoL/Scrabble
```

## Contributions
Feel free to contribute at any moment !  
In order to decrease computation time I am trying to serialize the Dawg instead of create it each time.


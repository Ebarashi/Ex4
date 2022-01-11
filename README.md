# Ex4 -  Pokemon

***by: Eilon Barashi & Harel Giladi***

+ ***for more information check the wiki***

# The project
In this project we were asked to implement a Pokemon game, with the purpose to demonstrate the graphs algorithms we've built in our previous assignments.
in this game there are 15 cases, each with one of 4 graphs, and a different senario. in each case we've had different number of agent, and thier task was to catch as many pokemons as posibble in order to get a maximum grade without exceeding the amount of moves. 
The game communicate with the server -
In order to start the communication with the server we need to run the jar file.
The server write and rewrite the game info. There are different cases with different graphs each case has different number of agent, and our task was to catch as many pokemons as posibble using the algorithm.

# the algotithm & project structure

We've used our graphs algorithms in order to find the best path for each agent, in order to maximize the number of pokemons he catchs.
We place agents on the center node or beside the most valued pokemons using PQ -> we used the function shortest path to find the closest pokemon that wasn't alrady grab -> 
send the next edge the agent needs to go by using the path list we got and tag the pokemon as grab and so on ->


* shortestPath - This algorithm gets a source and a destination returns the short way between them and order list of node id from src to dest .The algorithm does this while going through all the vertices as long as we have not visited them and the edges associated with each vertex.for each vertex we initialized its weight to be the shortest way to reach it from the src and the tag to be from whom we reached it when we finished with a vertex we painted it black. to get the list then we extract while running backwards all the ancestors of the vertices then return the list in the correct order - we implemented the algo we learned at algorithms course
@param src
@param dest
@return the shortest path from src to dest and list of node id


* center - Finds the node that has the shortest distance to it's farthest node. return: The nodes id, min-maximum distance This function uses a Dijkstra-algorithm. We will run with a vertex that does not exist. the algorithm initializes all the vertices' weights to the shortest way to them from the source
we find the longest way to a target vertex out of the shortest. from all the longest paths find the minimum out of it and that will be the center.

* dijkstra: This algorithm gets a source and a destination and returns the short way between them. The algorithm does this while going through all the vertices as long as we 
have not visited them and the edges associated with each vertex. for each vertex we initialized its weight to be the shortest way to reach it from the src and the tag to be from whom we reached it when we finished with a vertex we painted it black. we implemented the algo we learned at algorithms course
@param src
@param dest
@return the shortest path from src to dest




# How to Run 

In the cmd get to the folder of the jar file Write the command: "*java -jar Ex4_Server_v0.0.jar **0 (between 0-15)***" 
to start communication with the server then run the **Ex4.py** class 








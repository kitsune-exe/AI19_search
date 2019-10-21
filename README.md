# AI19_search
**Introduction to Artificial Intelligence, NTHU, 2019**

The original site is:
http://ai.berkeley.edu/search.html

**The commands**
1. Play a pacman game
```
python pacman.py
```
2. GoWestAgent
```
python pacman.py --layout testMaze --pacman GoWestAgent
python pacman.py --layout tinyMaze --pacman GoWestAgent
```
3. Call for help
```
python pacman.py -h
```
4. Q1: Test that the SearchAgent is working correctly
```
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
```
5. Q1: DFS
```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```
6. Q2: BFS (add --framtime=0 at the end of the line to speed up)
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
python eightpuzzle.py
```
7. ~~Q3: Varying the cost function~~(Not in my homework)
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```
8. Q4: A* search
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
9. Q5: Finding all corners
```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
10. Q6: Corners problem: heuristic
```
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
11. Others not in my homework, will be updated if new assignments are given
``` 
python pacman.py -l testSearch -p AStarFoodSearchAgent
python pacman.py -l trickySearch -p AStarFoodSearchAgent
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
python pacman.py -l bigSearch -p ApproximateSearchAgent -z .5 -q 
```

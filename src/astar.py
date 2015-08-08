#http://www.redblobgames.com/pathfinding/a-star/implementation.html#sec-1-4

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

class Graph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]

    ## haack
    def cost(self, a, b): return a_star_heuristic(a, b)

def a_star_heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + a_star_heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
                    
    return came_from, cost_so_far

example_graph = Graph()
example_graph.edges = {
    (1,1): [(2,3)],
    (2,3): [(1,1), (4,0), (2,5)],
    (4,0): [(1,1)],
    (2,5): [(6,6), (1,1)],
    (6,6): [(2,3)]
}
def main():
    came_from, cost_sf = a_star_search(example_graph, (1,1), (6,6))
    print came_from, cost_sf
    # print first way only
    for e in came_from:
        print "go to",e
        if e == (6,6): break

if __name__ == "__main__":
    main()

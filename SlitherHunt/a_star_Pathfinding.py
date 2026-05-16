
#Manhattan distance heuristic
def heuristic(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) ##############

def astar(start, goal, obstacles, grid_width, grid_height):
    #contains nodes to be evaluated
    open_set = {tuple(start)}
    came_from = {}
    g_cost = {tuple(start): 0}

#main loop 
    while open_set:
        current = min(
            open_set,
            key = lambda x: g_cost[x] + heuristic(x, goal)
        )

#reconstruct path if current node = goal
        if current == tuple(goal):
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        open_set.remove(current)
        
        #generate neighboring nodes

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = current[0] + dx, current[1] + dy

            if not (0 <= nx < grid_width and 0 <= ny < grid_height):
                continue
            if [nx, ny] in obstacles:
                continue

            neighbour = (nx, ny)
            
            #compute tentative cost from start to neighbour
            tentative_g = g_cost[current] + 1

            if neighbour not in g_cost or tentative_g < g_cost[neighbour]:
                came_from[neighbour] = current
                g_cost[neighbour] = tentative_g
                open_set.add(neighbour)
                
# if goal is not reachable, return empty path
    return []



def changePoint(start_loc):
    start = list(start_loc)
    start[0] = start[0]-1
    start[1] = start[1]-1
    start_loc = tuple(start)
    return start_loc

def get_neighbor(n,row,column,visited):
    neighbor = []
    if row == 0:
        if column == 0:
            neighbor.append((row+1,column))
            neighbor.append((row,column+1))
        elif column == n-1:
            neighbor.append((row+1,column))
            neighbor.append((row,column-1))
        else:
            neighbor.append((row+1,column))
            neighbor.append((row,column+1))
            neighbor.append((row,column-1))
    elif row == n-1:
        if column == 0:
            neighbor.append((row-1,column))
            neighbor.append((row,column+1))
        elif column == n-1:
            neighbor.append((row-1,column))
            neighbor.append((row,column-1))
        else:
            neighbor.append((row-1,column))
            neighbor.append((row,column+1))
            neighbor.append((row,column-1))
    else:
        if column == 0:
            neighbor.append((row+1,column))
            neighbor.append((row-1,column))
            neighbor.append((row,column+1))
        elif column == n-1:
            neighbor.append((row+1,column))
            neighbor.append((row,column-1))
            neighbor.append((row-1,column))
        else:
            neighbor.append((row+1,column))
            neighbor.append((row,column+1))
            neighbor.append((row,column-1))
            neighbor.append((row-1,column))
    length = len(neighbor)
    result =[]
    for i in range (0,length):
        if neighbor[i] not in visited:
            result.append(neighbor[i])
    return result



def min_distance(distance,unvisited):
    min_num = float('inf')
    for node in unvisited:
        if min_num > distance[node]:
            min_num = distance[node]
            result = node
    return result


def find_predecessor(predecessor,start,goal,path=[]):
    path.append(goal)
    if start == goal:
        return path
    node = predecessor[goal]
    find_predecessor(predecessor,start,node)
    return path


def path_find(n,start_loc,goal_loc,values):

    start = changePoint(start_loc)
    goal = changePoint(goal_loc)
    distance = {start: 0}
    visited =[]
    unvisited = []
    path =[]
    predecessor = {}


    for i in range (0,n):
        for j in range(0,n):
            if (i,j) != start:
                distance[(i,j)] = float('inf')
            unvisited.append((i,j))

    current = start

    while current != goal:
        current = min_distance(distance,unvisited)
        #print ("current",current,distance[current])
        visited.append(current)

        unvisited.remove(current)
        neighbor = []
        neighbor = get_neighbor(n,current[0],current[1],visited)
        #print ("neighbour", neighbor)
        for h in range(len(neighbor)):
            num = values[neighbor[h][0]][neighbor[h][1]]
            cost = distance[current] + num + 1
            if cost < distance[neighbor[h]]:
                distance[neighbor[h]] = cost
                predecessor[neighbor[h]] = current
                #print (neighbor[h],distance[neighbor[h]])

    #print (distance[current])
    path = find_predecessor(predecessor,start,goal)
    size = len(path)
    new_path = []
    for m in xrange (size-1,-1,-1):
        pair = path[m]
        item = list(pair)
        item[0] = item[0] +1
        item[1] = item[1] +1
        pair = tuple(item)
        new_path.append(pair)
    return new_path



# n = 3              # an integer
# start_loc = (1,1)  # a tuple
# goal_loc= (3,1)    # a tuple
# values = [[4,2,8],[9,1,7],[3,2,6]]   # a list of lists, each list is a row.
n = 5              # an integer
start_loc = (1,1)  # a tuple
goal_loc= (5,4)    # a tuple
values = [[4,3,3,4,2],[2,4,4,2,2],[3,4,5,3,2],[2,3,4,5,2],[4,3,3,2,4]]
least_cost_path = []
least_cost_path = path_find(n, start_loc, goal_loc, values)

print(least_cost_path)

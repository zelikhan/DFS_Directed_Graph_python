mygraph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '4': ['7', '8'],
    '7': ['11', '12'],
    '6': ['10'],
    '3': ['6'],
    '5': ['9'],
    '9': ['13'],
    '11': [],
    '12': [],
    '8': [],
    '13': [],
    '10': []
}

visited = []
queue = []
starting_node = input("Please Enter Starting Node : ")
goal_state = input("Enter Goal State : ")


def mydfs(mygraph, visited, starting_node):
    if starting_node not in visited:
        print(starting_node, end=" ")
        visited.append(starting_node)

        for neighbour in mygraph[starting_node]:
            if neighbour not in goal_state:
                mydfs(mygraph, visited, neighbour)
            elif neighbour in goal_state:
                print(neighbour, " Destination ")
            break


print("Depth First Search Traversal : ")
mydfs(mygraph, visited, starting_node)

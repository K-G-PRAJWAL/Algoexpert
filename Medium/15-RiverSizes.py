def riverSizes(matrix):
    '''
    Time: O(rows x columns)
    Space: O(rows x columns)
    '''
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverse(i, j, matrix, visited, sizes)
    return sizes


def traverse(i, j, matrix, visited, sizes):
    currSize = 0
    nodes = [[i, j]]
    while len(nodes):
        currNode = nodes.pop()
        i = currNode[0]
        j = currNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currSize += 1
        unvisited = getUnvisitedNeigbors(i, j, matrix, visited)
        for neighbor in unvisited:
            nodes.append(neighbor)
    if currSize > 0:
        sizes.append(currSize)


def getUnvisitedNeigbors(i, j, matrix, visited):
    unvisited = []
    if i > 0 and not visited[i - 1][j]:
        unvisited.append([i - 1, j])
    if i < len(matrix)-1 and not visited[i + 1][j]:
        unvisited.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        unvisited.append([i, j-1])
    if j < len(matrix[0])-1 and not visited[i][j+1]:
        unvisited.append([i, j + 1])
    return unvisited


print(riverSizes([
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]]
))

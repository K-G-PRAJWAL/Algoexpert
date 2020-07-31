def youngestCommonAncestor(topAncestor, descendant1, descendant2):
    '''
    Time: O(Depth)
    Space: O(1)
    '''
    depth1 = getDescendantDepth(descendant1, topAncestor)
    depth2 = getDescendantDepth(descendant2, topAncestor)
    if depth1 > depth2:
        return backtrackAncestralTree(descendant1, descendant2, depth1-depth2)
    else:
        return backtrackAncestralTree(descendant2, descendant1, depth2-depth1)


def getDescendantDepth(descesdant, topAncestor):
    depth = 0
    while decesdant != topAncestor:
        depth += 1
        descesdant = descesdant.ancestor
    return depth


def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant

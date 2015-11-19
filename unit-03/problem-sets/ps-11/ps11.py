# 6.00 Problem Set 11
#
# ps11.py
#
# Graph optimization
# Finding shortest paths through MIT buildings
#

from graph import *


#
# Problem 2: Building up the Campus Map
#
# Write a couple of sentences describing how you will model the
# problem as a graph)
#
def load_map(mapFilename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."

    mit_map = MitDigraph()
    map_file = open(mapFilename, 'r')
    line_count = 0

    for line in map_file:
        edge_values = line.split()
        new_edge = MitEdge(*edge_values)
        mit_map.addEdge(new_edge)
        line_count += 1

    print "Loaded {} edges from file.".format(line_count)
    return mit_map


#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and the constraints
#
def findPaths(digraph, start, end, visited=None):
    if visited is None:
        visited = []

    if start == end:
        return [[start]]

    paths = []
    children = digraph.childrenOf(start)
    for node in children:
        if node not in visited:
            # visited = visited + [node]
            # the above line mutates the 'outer' version of visited,
            # causing the list to be shared amongst all recursive calls
            # made by that call of findPaths
            new_paths = findPaths(digraph, node, end, visited + [node])

            if new_paths is not None:
                for np in new_paths:
                    paths.append([start] + np)

    if paths == []:
        return None
    else:
        return paths


def lengthOfPath(digraph, path):
    length = 0
    for i in range(len(path) - 1):
        length += digraph.edges[path[i]][path[i + 1]].length

    return length


def amountOutdoors(digraph, path):
    outdoors = 0
    for i in range(len(path) - 1):
        outdoors += digraph.edges[path[i]][path[i + 1]].outdoor

    return outdoors


def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    all_paths = findPaths(digraph, start, end)
    length_paths = []

    for path in all_paths:
        path_length = lengthOfPath(digraph, path)
        if path_length <= maxTotalDist:
            length_paths.append((path_length, path))

    length_paths = sorted(length_paths, key=lambda x: x[0])
    outdoor_paths = []

    for pathdata in length_paths:
        length, path = pathdata
        dist_outdoors = amountOutdoors(digraph, path)

        if dist_outdoors <= maxDistOutdoors:
            outdoor_paths.append(((length, dist_outdoors), path))

    final_paths = sorted(outdoor_paths, key=lambda x: x[0])

    if len(final_paths) == 0:
        raise ValueError("No paths found")

    return final_paths[0][1]


#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def withinConstraints(digraph, path, max_dist, max_out):
    length = lengthOfPath(digraph, path)
    outside = amountOutdoors(digraph, path)
    return length <= max_dist and outside <= max_out


def betterPath(digraph, path, best_length, best_outside):
    length = lengthOfPath(digraph, path)
    outside = amountOutdoors(digraph, path)
    return (length <= best_length and outside < best_outside) or \
        (length < best_length and outside <= best_outside)


def pathTuple(digraph, path):
    length = lengthOfPath(digraph, path)
    outside = amountOutdoors(digraph, path)
    return ((length, outside), path)


def findBestPath(digraph,
                 start,
                 end,
                 max_dist,
                 max_outside,
                 visited=[],
                 partial_path=[]):

    if start == end:
        return [start]

    best = None
    for node in digraph.childrenOf(start):
        if node not in visited:
            new_partial = partial_path + [node]
            print new_partial

            if withinConstraints(digraph, new_partial, max_dist, max_outside):
                new_path = findBestPath(digraph, node, end,
                                        max_dist, max_outside,
                                        visited + [node], new_partial[:])

                if new_path is None:
                    continue

                new_path = [start] + new_path

                if withinConstraints(digraph, new_path, max_dist, max_outside):
                    if (best is not None and
                        betterPath(digraph, new_path, best[0][0], best[0][1])) \
                            or best is None:
                        best = pathTuple(digraph, new_path)

    if best is None:
        return None
    else:
        return best[1]


def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
        not exceed maxDisOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    return findBestPath(digraph, start, end, maxTotalDist, maxDistOutdoors)


if __name__ == '__main__':
    digraph = load_map("mit_map.txt")
    LARGE_DIST = 1000000

# Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1

# Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(digraph, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2

# Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3

# Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(digraph, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4

# Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5

# Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(digraph, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6

# Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedDFS(digraph, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'

    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

# Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedDFS(digraph, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'

    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

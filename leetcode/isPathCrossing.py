class Solution:
    def isPathCrossing(self, path):
        loc, h = [0, 0], []
        h.append(loc.copy())
        for m in path:
            if m == 'N':
                loc[0] += 1
            elif m == 'S':
                loc[0] -= 1
            elif m == 'E':
                loc[1] -= 1
            elif m == 'W':
                loc[1] += 1
            if loc in h:
                return True
            else:
                h.append(loc.copy())
        return False


class Solution3:
    def isPathCrossing(self, path):
        x, y, map = 0, 0, {(0, 0)}
        for p in path:
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            elif p == 'W':
                x -= 1
            
            if (x, y) in map:
                return True
            map.add((x, y))
        return False


class Solution2:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        set = {(0, 0)}
        
        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            else:
                x -= 1
            
            if (x, y) in set:
                return True
            set.add((x, y))
        return False

answer = Solution2()
print(answer.isPathCrossing('NES'))

'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise.

Example 1:

Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 10^4
path will only consist of characters in {'N', 'S', 'E', 'W}

'''
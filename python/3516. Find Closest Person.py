class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diffxz = abs(x-z)
        diffyz = abs(y-z)

        if diffxz == diffyz:
            return 0
        elif diffxz > diffyz:
            return 2
        else:
            return 1
        
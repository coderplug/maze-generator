class Validator(object):
    def validateInput(self, minMazeSize, mazeSize, startPos, endPos, directory, filename):
        mazeSize = (mazeSize[0]-1, mazeSize[1]-1)
        if not(self.validateMazeSize(minMazeSize, mazeSize)):
            return "Maze size is not large enough. Minimum values are " + str((minMazeSize[0] + 1, minMazeSize[1] + 1))
        #elif not(self.validateStartPos(mazeSize, startPos)):
        #    return "Start position is invalid. It should be on the border (not corners) of maze"
        #elif not(self.validateEndPos(mazeSize, startPos, endPos)):
        #    return "End position is invalid. It should be on the border (not corners) of maze and does not block start position"
        elif not(self.validateDirectory(directory)):
            return "Directory should not be empty"
        elif not(self.validateFilename(filename)):
            return "Filename should not be empty"
        return None

    def validateMazeSize(self, minMazeSize, mazeSize):
        if mazeSize[0] < minMazeSize[0] or mazeSize[1] < minMazeSize[1]:
            return False
        return True

    def validateStartPos(self, mazeSize, startPos):
        return self.isOnBorder(mazeSize, startPos)

    def validateEndPos(self, mazeSize, startPos, endPos):
        return self.isOnBorder(mazeSize, endPos) and not(self.areNeighbors(startPos, endPos))
            
    def isOnBorder(self, mazeSize, startPos):
        if startPos[0] > 0 and startPos[0] < mazeSize[0]:
            if startPos[1] == 0 or startPos[1] == mazeSize[1]:
                return True
            else:
                return False
        elif startPos[1] > 0 and startPos[1] < mazeSize[1]:
            if startPos[0] == 0 or startPos[0] == mazeSize[0]:
                return True
            else:
                return False
        else:
            return False

    def areNeighbors(self, startPos, endPos):
        x_diff = abs(startPos[0] - endPos[0])
        y_diff = abs(startPos[1] - endPos[1])
        if x_diff > 1 and y_diff == 0:
            return False
        elif x_diff == 0 and y_diff > 1:
            return False
        elif (x_diff + y_diff) > 3:
            return False
        return True

    def validateDirectory(self, directory):
        return directory != ""

    def validateFilename(self, filename):
        return filename != ""
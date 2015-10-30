# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "Position: {}, {}".format(self.getX(), self.getY())


# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.dirty_tiles = set([])
        self.clean_tiles = set([])

        for w in range(self.width):
            for h in range(self.height):
                self.dirty_tiles.add((w, h))

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        query_tile = (int(pos.getX()), int(pos.getY()))
        if query_tile in self.dirty_tiles:
            self.dirty_tiles.remove(query_tile)
            self.clean_tiles.add(query_tile)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return (m, n) in self.clean_tiles

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.clean_tiles)

    def getPercentCleaned(self):
        """
        Returns the percent of tiles in the room that have been cleaned

        returns: a float
        """
        return float(self.getNumCleanedTiles()) / float(self.getNumTiles())

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.uniform(0, self.width)
        y = random.uniform(0, self.height)

        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return (0 <= pos.getX() < self.width) and \
            (0 <= pos.getY() < self.height)


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.direction = random.uniform(0, 360)
        self.position = room.getRandomPosition()
        room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction % 360

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        new_position = self.position.getNewPosition(self.direction, self.speed)
        while not self.room.isPositionInRoom(new_position):
            self.direction = random.uniform(0, 360)
            new_position = self.position.getNewPosition(
                self.direction, self.speed)

        self.position = new_position
        self.room.cleanTileAtPosition(self.position)

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    results = []
    for t in range(num_trials):

        #anim = ps6_visualize.RobotVisualization(
        #    num_robots, width, height)

        room = RectangularRoom(width, height)
        robots = []
        for r in range(num_robots):
            robots.append(robot_type(room, speed))

        #anim.update(room, robots)

        steps = 0
        while room.getPercentCleaned() < min_coverage:
            for bot in robots:
                bot.updatePositionAndClean()

            steps += 1
        #    anim.update(room, robots)

        results.append(steps)
        #anim.show()

    return sum(results) / float(len(results))


# === Problem 4
#
# 1) How long does it take to clean 80% of a 20×20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions
#	 20×20, 25×16, 40×10, 50×8, 80×5, and 100×4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    results = []
    num_bots = range(1, 11)

    for bots in num_bots:
        results.append(
            runSimulation(bots, 1.0, 20, 20, 0.8, 100, StandardRobot))

    pylab.plot(num_bots, results)
    pylab.title("Dependence of Cleaning Time on Number of Robots")
    pylab.xlabel("Number of Robots")
    pylab.ylabel("Mean Steps Needed to Clean")
    pylab.show()

#showPlot1()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    results = []
    dimensions = [(20, 20), (25, 16), (40, 10), (50, 8), (80, 5), (100, 4)]

    for dims in dimensions:
        results.append(
            runSimulation(2, 1.0, dims[0], dims[1], 0.8, 100, StandardRobot))

    pylab.plot(
        map(lambda x: x[0]/float(x[1]), dimensions), results)
    pylab.title("Dependence of Cleaning Time on Room Shape")
    pylab.xlabel("Ratio of Room Width to Room Height")
    pylab.ylabel("Mean Steps Needed to Clean")
    pylab.show()


# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while True:
            self.direction = random.uniform(0, 360)
            new_position = self.position.getNewPosition(
                self.direction, self.speed)
            if self.room.isPositionInRoom(new_position):
                break

        self.position = new_position
        self.room.cleanTileAtPosition(self.position)


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    num_robots = range(1,11)
    coverage = 0.80
    room_w = 20
    room_h = 20
    speed = 1.0
    trials = 25

    standard_results = []
    random_walk_results = []

    for botnum in num_robots:
        standard_results.append(runSimulation(
            botnum, speed, room_w, room_h, \
            coverage, trials, StandardRobot))
        random_walk_results.append(runSimulation(
            botnum, speed, room_w, room_h, \
            coverage, trials, RandomWalkRobot))

    pylab.plot(num_robots, standard_results)
    pylab.plot(num_robots, random_walk_results)
    pylab.show()

showPlot3()




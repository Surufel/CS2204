from util import *

class Player(object):
    """
    player class.

    To test your own machine player strategy, you should implement the ```make_decision()``` method.
    To test your implementation, you should modify the configy.py to set one or two player(s) as 'machine'
    """

    def __init__(self, id, name=None):
        self.points=0
        self.id=id
        self.name=name if name else 'player'+str(id)
        self.add = lambda val,rand: (val+rand) % 16
        self.replace = lambda val,rand: rand % 16
        self.skip = lambda val, rand: val

    def make_decision(self, four_bits, next_randoms, code_digits):
        """
        This function decide next move of the machine player.

        You should only modify '#Your Code is Here' to define your own machine player.
        To enable your machine player, please check & modify the configuration in config.py.

        Args:
            four_bits (int[]): the four bit number in the LED
            next_randoms (int[]): the next 3 random digits
            code_digits(int[]): 2 code digits.
        Returns:
            operation: [self.skip | self.add | self.replace]
        	selected: [0|1|2|3]
        """

        operation = self.skip
    	selected = 0

        # UPDATED PYTHON PROGRAM FOR SELECTING OPERATION AND POSITION
        # Overview:
        #           - General variables
        #           - Replacement algorithm
        #                   - User-defined function: calc_points
        #                   - User-defined function: num_adjacencies
        #                   - User-defined function: count_adj
        #                   - User-defined function: reg_points
        #           - Adding algorithm
        #                   - (uses above user-defined functions as well)
        #           - Finding maximums
        #                   - User-defined function: find_max
        #           - Compare maximums

        # GENERAL VARIABLES *IMPORTANT*
    	#----------------------------------------------------------------------
        copy_four_bits = list(four_bits)        # Copy of the four LED bits
        numBits = len(four_bits)                # Total number of bits displayed (i.e. 4)

        # Empty arrays to hold potential scores for each position
        add_scores = [0, 0, 0, 0]               # Potential scores for adding
        replace_scores = [0, 0, 0, 0]           # Potential scores for replacing

        # Empty arrays to hold the max score and position for adding and replacing
        # The arrays will contain: [position, score]
        max_add = [-1, -1]                      # Max position and score for adding
        max_replace = [-1, -1]                  # Max position and score for replacing

        # Create a variable to hold the next random digit
        randDig = next_randoms[0]

        # DEBUG #
        print "ORIGINAL LED BITS:"
        print four_bits                         # Print the original four bits
        print "RANDOM DIGIT: %d" % randDig      # Print the random digit

        # 1. REPLACING ALGORITHM
        #----------------------------------------------------------------------
        # Figure out what scores will result from replacing each position with
        # the next random digit. The "replace_scores" array will contain potential
        # scores for each position.
        # Example:
        #       Next random digit: 4
        #       Resulting replace_scores array looks like [4, 4, 4, 8] meaning:
        #           Replacing digit in position 0 will result in 4 points
        #           Replacing digit in position 1 will result in 4 points
        #           Replacing digit in position 2 will result in 4 points
        #           Replacing digit in position 3 will result in 8 points
        #
        # The potential scores are calculated by calling the "calc_points" function
        # and sending the empty array with a status flag of 0 to indicate the points
        # should be calculated for a "replacing" algorithm.
        # The function returns a new replace_scores array with the appropriate points

        # ~~~~~~~~~~~~~~~~~ USER-DEFINED FUNCTION: calc_points ~~~~~~~~~~~~~~~~~
        # This function calculates the number of points a certain position
        # will receive for a particular operation (add/replace). Therefore,
        # this function works for both the adding and replacing algorithms.
        # Flag STATES:
        #               0 means REPLACE
        #               1 means ADD
        # This function also calls three other functions: num_adjacencies,
        # count_adj, and reg_points.

        def calc_points(scores_arr, flag):
            # Loops from the numbers 0 to 3 to check each position/bit
            for i in range(numBits):
                pos = i
                # Depending on the calling statement, the function will either
                # directly use the random digit (replace) or add the random digit to
                # the current position (add)
                if flag==0:             # STATE 0: REPLACE
                    newNum = randDig
                else:                   # STATE 1: ADD
                    newNum = copy_four_bits[pos] + randDig
                    # OVERFLOW CHECK for addition
                    if newNum>15:
                        newNum = newNum - 16
                # Call to "num_adjacencies" to obtain the number of adjacencies
                # to the current position
                numAdj = num_adjacencies(newNum, pos)
                # Call to "reg_points" to determine the total number of points
                # for the particular position based on the number of adjacencies
                # calculated above and the value of the new digit
                scores_arr[pos] = reg_points(numAdj, newNum)
            # Returns the new array with updated scores for all positions
            return scores_arr

        # ~~~~~~~~~~~~~~~~~ USER-DEFINED FUNCTION: num_adjacencies ~~~~~~~~~~~~~~~~~
        # This function calculates the number of adjacencies of the number
        # passed to the function. It makes two calls to count_adj to first
        # calculate the number of adjacencies to the right of the current position,
        # and then to the left of the current position.
        # Flag STATES:
        #               Positive 1 (+1) indicates RIGHT
        #               Negative 1 (-1) indicates LEFT
        # This function returns the sum of the adjacencies to the right and
        # left of the position for the total number of adjacencies.

        def num_adjacencies(num, pos):
            # Check the right side for adjacencies
            numAdjRight = count_adj(num, pos, 1)
            # Check the left side for adjacencies
            numAdjLeft = count_adj(num, pos, -1)
            # Return the total number of adjacencies
            return numAdjRight + numAdjLeft

        # ~~~~~~~~~~~~~~~~~ USER-DEFINED FUNCTION: count_adj ~~~~~~~~~~~~~~~~~
        # This function calculates the number of adjacencies in a particular
        # direction. The "op" (operation) variable dictates the direction.
        #               Positive 1 (+1) indicates right direction
        #               Negative 1 (-1) indicates left direction
        # The function returns the number of adjacencies in one direction.
        def count_adj(num, pos, op):
            adj = True
            numAdj = 0
            curPos = pos + op
            # The conditions in the while loop make sure that the loop runs only
            # while there are adjacencies are present, and that the loop does
            # not go out of the bounds of the array
            while(curPos>-1 and curPos<numBits and adj==True):
                # DEBUG # print "side: %d curPos: %d four_bits: %d" %(op, curPos, copy_four_bits[curPos])
                # If an adjacency has been found, then the loop continues
                # and the number of adjacencies is incremented
                if four_bits[curPos]==num:
                    curPos = curPos+op
                    numAdj = numAdj+1
                # Otherwise, if there is no adjacency, the loop terminates
                else:
                    adj=False
            # The number of adjacencies is returned
            return numAdj

        # ~~~~~~~~~~~~~~~~~ USER-DEFINED FUNCTION: reg_points ~~~~~~~~~~~~~~~~~
        # This function calculates the number of points a position will earn
        # based on the number of adjacencies and random digit.
        # This function returns the total number of REGULAR points

        def reg_points(numAdj, num):
            if numAdj==0:
                return num;
            elif numAdj==1:
                return 2*num
            elif numAdj==2:
                return 4*num
            else:
                return 8*num

        # REPLACEMENT ALGORITHM POINT CALCULATIONS
        replace_scores = calc_points(replace_scores, 0)

        # DEBUG #
        print "REPLACE SCORES: "
        print replace_scores

        # 2. ADDING ALGORITHM
        #----------------------------------------------------------------------
        # Similar to the "replacing" algorithm section, this section figures out
        # what scores will result from adding the random digit to each position.
        # The "add_scores" array will contain potential scores for each position.
        # Example:
        #       Next random digit: 6
        #       Resulting add_scores array looks like [6, 8, 6, 36] meaning:
        #           Adding digit to position 0 will result in 6 points
        #           Adding digit to position 1 will result in 8 points
        #           Adding digit to position 2 will result in 6 points
        #           Adding digit to position 3 will result in 36 points
        #
        # The potential scores are calculated by calling the "calc_points" function
        # and sending the emtpy array with a status flag of 1 to indicate the points
        # should be calculated for an "adding" algorithm
        # The function return a new add_scores array with the appropriate points

        # ADDING ALGORITHM POINT CALCULATIONS
        add_scores = calc_points(add_scores, 1)

        # DEBUG #
        print "ADD SCORES: "
        print add_scores


        # 3. FIND MAXIMUMS
        #----------------------------------------------------------------------
        # This section calculates the positions within the "add_scores" array and
        # "replace_scores" array that will result in the most points. If there
        # is a tie, the position at the farthest right is selected.
        # This function makes a call to the "find_max" function.

        # ~~~~~~~~~~~~~~~~~ USER-DEFINED FUNCTION: find_max ~~~~~~~~~~~~~~~~~
        # This function calculates the max position and score within the
        # provided array of scores. It stores the position and score in the
        # appropriate max array.

        def find_max(scores_arr, max_arr):
            for i in range(numBits):
                if scores_arr[i]>=max_arr[1]:
                    max_arr[1] = scores_arr[i]
                    max_arr[0] = i
            return max_arr

        # MAXIMUM CALCULATIONS
        max_add = find_max(add_scores, max_add)
        max_replace = find_max(replace_scores, max_replace)

        # DEBUG #
        print "ADD Maximum: "
        print max_add
        print "REPLACE Maximum: "
        print max_replace

        # 4. COMPARE MAXIMUMS
        #----------------------------------------------------------------------
        # This section compares the maximums of the adding and replacing arrays.
        # If the adding maximum is greater than the replacing maximum, then
        # the program selection "self.add" and uses the position determined
        # previously by the program.
        # However, if the adding maximum is less than or equal to the
        # replacing maximum, then the replacing maximum is selected as default.
        
        if max_add[1]>max_replace[1]:
            operation = self.add
            selected = max_add[0]
            # DEBUG #
            print "\nADDED %d LOC %d\n" % (max_add[1], max_add[0])
        else:
            operation = self.replace
            selected = max_replace[0]
            # DEBUG #
            print "\nREPLACED %d LOC %d\n" %(max_replace[1], max_replace[0])

    	return operation, selected

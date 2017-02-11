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
    	selected = 3 # Playing right most. Refer to line 42.

        # Test strategy by running: python ppm.py

        # Strategy 1 (for example: 3 A E A and the next random number is A)
        # Norria: play rightmost, check adjacencies (replace vs add), if no adjacency add to highest #

        # Okay.
        # If there is an adjacency for replace:
            if (any(four_bits.count(theBit) > 1 for theBit in four_bits)):
                # There is!
                for bitStep in four_bits:
                    if (next_randoms[bitStep] != bitStep):
                        operation = self.replace
                        selected = bitStep

    	return operation, selected

        # Attention team: Please refer to experiment1checklist.pdf after all is said and done.

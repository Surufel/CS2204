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

        You should only modify '#Your Codes Here' to define you own machine palyer.
        To enable your machine player, please check & modify the configuration in config.py.

        Args:
            four_bits (int[]): the four bits number in the LED 
            next_randoms (int[]): the next 3 random numbers
            code_digits(int[]): 2 bit code digits.
        Returns:
            operation: [self.skip | self.add | self.replace]
        	selected: [0|1|2|3]
        """
        
        operation = self.skip
    	selected = 0
    	#Your Codes Here
    	return operation, selected
"""
.. module:: bouncy_numbers
   :platform: Unix, Windows
   :synopsis: Find the least number for which the proportion of 
   bouncy numbers is exactly the value of the argument or by
   defualt 99%.

.. moduleauthor:: Jaime Jimenez


"""
import sys, datetime

class BouncyNumber():

    def __init__(self, percentage_limit = None, bouncy_n = 1):
        self.percentage_limit = percentage_limit
        self.bouncy_n = bouncy_n
        self.ini = 100

    def calculate(self):
        """
        Return the least number for which the proportion of 
        bouncy numbers is exactly the value of percentage_limit value

        """
        count_bouncy = 0
        i = self.ini
        bouncy_method = getattr(self, 'is_bouncy'+str(self.bouncy_n))
        #print(vars()['is_bouncy1'](i))
        while True:
            if(bouncy_method(i)):
                count_bouncy += 1
            if (count_bouncy  * 100 / i) >= self.percentage_limit:
                break
            i += 1
        self.count_bouncy = count_bouncy
        self.least_number = i
        return i

    def is_bouncy1(self, num):
        """
        Return True if the number is bouncy (is neither increasing nor 
        decreasing)
        Return False if the number is increasing or decreasing

        """
        strnum = str(num)
        increasing = decreasing = None
        previous = strnum[0]
        for n in strnum:
            if increasing is None and previous != n:
                increasing = previous < n
            else:
                if ((increasing and previous > n) or
                   (not increasing and previous < n)):
                    return True
            previous = n
        return False
        
    def is_bouncy2(self, num):
        """
        Return True if the number is bouncy (is neither increasing nor 
        decreasing)
        Return False if the number is increasing or decreasing

        """
        strnum = str(num)
        increasing = decreasing =False
        previous = strnum[0]
        for n in strnum:
            if previous < n:
                increasing = True
            elif previous > n:
                decreasing = True
            previous = n
        return (increasing and decreasing)

def main(argv=None):
    """Start point. 
    """
    try:
        limit = int(argv[1])
    except IndexError:
        limit = 99
    
    for n in range(1,2):
        elapsed = 0
        for i in range(1,4):
            tm1 = datetime.datetime.utcnow()
            least_number = BouncyNumber(limit, n).calculate()
            tm2 = datetime.datetime.utcnow()
            elapsed = elapsed + (tm2 - tm1).total_seconds()
        
        #BouncyNumber(limit).calculate()
        print('---1----')
        print(elapsed/4)
        print(least_number)
    
    return 2

print('ok')
#if __name__ == "__main__":
    #print('ok')
main(sys.argv)

exit()

class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return not self.is_odd()

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        s=0
        for i in range(1,self.value//2):
            if self.value%i:
                s+=1
        return s==1
    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        l=[]
        for i in range(1,self.value//2):
            if self.value%i==0:
                l.append(i)
        l.append(self.value)
        return l

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        return sum(self.get_digits())

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.get_number())[::-1])
    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return self.get_number()==self.get_reverse()

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        return [int(i) for i in str(self.value)]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max(self.get_digits())

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min(self.get_digits())
    
    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        return self.get_sum()/self.get_length()

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        a=sorted(self.get_digits())
        b=self.get_length()//2
        if self.get_length()%2==0:
            return (a[b-1]+a[b])/2
        else:
            return a[b]
    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return self.get_max()-self.get_min()

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        d={}
        for i in sorted(self.get_digits()):
            d[i]=0
        for i in self.get_digits():
            d[i]+=1
        return d
    
# Create a new instance of Number
number = Number(3)
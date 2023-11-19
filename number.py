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
        return self.value%2==1

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
        return len(self.get_divisors())==2

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divisors=[]
        for i in range(1,self.value+1):
            if self.value%i==0:
                divisors.append(i)
        return divisors

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
        return int(str(self.value)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return self.value==self.get_reverse()

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        return list(map(int,list(str(self.value))))

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
        return self.get_sum()/len(str(self.value))

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        lst=self.get_digits()
        lst.sort
        l=len(lst)
        if l%2==0:
            return (lst[l//2-1]+lst[l//2])/2
        else:
            return lst[l//2]

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return list(range(self.get_min(),self.get_max()))

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        st=set(self.get_digits())
        dict={}
        for i in st:
            dict[i]=self.get_digits().count(i)
        return dict    

# Create a new instance of Number
number = Number(3)

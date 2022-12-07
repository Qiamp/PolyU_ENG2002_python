import os
class ratNum:

    def __init__(self,a_1,b_1,a_2,b_2,n):
        self.a_1=a_1
        self.b_1=b_1
        self.a_2=a_2
        self.b_2=b_2
        self.n=n

    def product(self):
        self.a_1=int(input('Please enter the first molecule:'))
        self.b_1=int(input('Please enter the first Numerator:'))
        self.a_2=int(input('Please enter the second molecule:'))
        self.b_2=int(input('Please enter the first Numerator:'))
        '''Enter the numerator and denominator of each fraction '''

        if self.b_1==0 or self.b_2==0:   #have a denominator of 0
            print('error')
        else:
            self.result=(self.a_1/self.b_1)*(self.a_2/self.b_2)   #Multiply two fractions
            m=float.as_integer_ratio(self.result)
            print('a=',m[0],'b=',m[1],'The result is',m[0],'/',m[1])

    def power(self):
        self.a_1=int(input('Please enter the molecule:'))
        self.b_1=int(input('Please enter the Numerator:'))
        self.n=int(input('Please enter the power number:'))
        '''Enter the numerator and denominator  '''

        if self.b_1==0:    #have a denominator of 0
            print('error')
        else:  #going to exponents a fraction
            result=float((self.a_1/self.b_1)**self.n)
            m=float.as_integer_ratio(result)
            print('a=',m[0],'b=',m[1],'The result is',m[0],'/',m[1])
class Solution:
    def fib(self, number: int) -> int:
        if number < 2:
            return number

        fibonacci_storage = [None] * (number +1)
        fibonacci_storage[0], fibonacci_storage[1] = 0, 1

        def helper_function(number: int) -> int:
            if fibonacci_storage[number] == None:
                fibonacci_storage[number] = helper_function(number -1) + helper_function(number -2)
        
            return fibonacci_storage[number]
        
        helper_function(number)
        return fibonacci_storage[number]
    
    def fib(self, number: int) -> int:
        if number < 2:
            return number

        fibonacci_storage = [None] * (number +1)
        fibonacci_storage[0], fibonacci_storage[1] = 0, 1

        for index in range(2, number +1):
            fibonacci_storage[index] = fibonacci_storage[index -2] + fibonacci_storage[index -1]

        return fibonacci_storage[number]
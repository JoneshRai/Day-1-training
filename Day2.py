#def greet(name):
 #   print(f"hello,{name}")
#greet('anup')
#greet('gu')

#def addition(a,b):
 #   sum=a+b
  #  print(f"the sum is:, {sum}")
#addition=(1,4)

def add_number(num1, num2):
    return num1 + num2

result = add_number(5,7)
print("the sum is:", result)

add = lambda a,b : a + b
multiply = lambda x,y : x*y

print(add(1,2))
print (multiply(1,2))

def test(*args):
    print(args)

test(1,2,3)

def is_odd(number):
    return number % 2 == 0

result = is_odd(2)
print(result)



def loop(input_list):
    for element in input_list:
        print(element)  
    return input_list

sample_list = [1, 2, 3, 4, 5]
result = loop(sample_list)
print("Returned list:", result)



def lis(num):
    for i in num:
        print(i)

lis([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19])



def cube(num):
    for i in num:
        result=i*3
        print(f'gukodalla of {i} is {result}')
cube ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])


class Calculation:
    def add(self, a, b):
        result = a + b
        return result
    def sub(a, b):
        result = a - b
        return result
    def mul(a,b):
        result = a * b
        return result

calculator = Calculation()
result = calculator.add(1,3)
result = calculator.sub(4,2)
result = calculator.mul(2,2)
print(result) 



class gu:
    def cube(self,num):
        for i in num:
            result=i*3
            print(f'gukodalla of {i} is {result}')
    def lis(self,num):
        for i in num:
            print(i)

gu1 = gu()
gu = gu1.cube([1,2,3,4])
gu = gu1.lis([1,2,3,4,5])


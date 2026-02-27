
def calculator(num1, num2, ops):
  if ops == "+":
    return num1 + num2
  elif ops == "-":
    return num1 - num2
  elif ops == "*":
    return num1 * num2
  elif ops == "/":
    return num1 / num2
  else:
    return "Invalid operation"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
ops = input("Enter which operation need to perform?")


  
result = calculator(num1, num2, ops)
print("Result =",result)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  if n2 != 0:
    return n1 / n2
  else:
    return "Error: Division by zero is not allowed."

def percentage(n1, n2):
  if n2 != 0:
    return n1 * (n2 / 100)
  else:
    return "Error: Percentage by zero is not allowed."


# Operations dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "%": percentage
}

# History
history = []

while True:
  try:
    print("\nSimple Calculator")
    print("Available operations: +, -, *, /, %")
    print("-----------------------------")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operation (+, -, *, /, %): ")
    
    if operator in operations:
      result = operations[operator](num1, num2)
      print(f"The result of {num1} {operator} {num2} is: {result:.2f}")
      history.append(f"{num1} {operator} {num2} = {result:.2f}")
    else:
      print("Invalid operation. Please try again.")
  except ValueError:
    print("Invalid input. Please enter valid numbers.")
  
  continue_calc = input("Do you want to perform another operation? (y/n): ").lower()
  if continue_calc != 'y':
    print("\nCalculator closing. Goodbye!")
    print("\n📜 Operation history:")
    for h in history:
      print(h)
    break

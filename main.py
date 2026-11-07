from calculator_modules.arithmetic import add, subtract, multiply, divide

def main():
    print("Добро пожаловать в калькулатор")
    a = float(input("введите 1 число"))
    b = float(input("введите 2 число"))
    operation = input("введите операцию (+, -, *, /)")
    add(a, b)
    if operation == "+":
       result = add(a, b)
    elif operation == "-":
      result = subtract(a, b)
    elif operation == "*":
     result = divide(a, b)
    else :
      result = divide(a, b)
    
    print (f"Результат (result)")
if__name__=="__main__":
main()
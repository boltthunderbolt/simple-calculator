def showArithmeticOperator() :
  global arithmeticOperator
  arithmeticOperator = [
  ['Addition', '+'],
  ['Subtraction','-'],
  ['Multiplication','*'],
  ['Division','/'],
  ['Modulus','%'],
  ['Exponentiation','**'],
  ['Floor division','//']
  ];
  print("Simple calculator with Python");
  print("=============================\n")
  for index, operator in enumerate(arithmeticOperator, start=1) :
    print(f"{index}. {operator[0]}");

def calculation(firstNumber, chooseTheArithmeticOperator, secondNumber) :
  if chooseTheArithmeticOperator == arithmeticOperator[0] :
    return firstNumber + secondNumber;
  elif chooseTheArithmeticOperator == arithmeticOperator[1] :
    return firstNumber - secondNumber;
  elif chooseTheArithmeticOperator == arithmeticOperator[2] :
    return firstNumber * secondNumber;
  elif chooseTheArithmeticOperator == arithmeticOperator[3] :
    return firstNumber / secondNumber;
  elif chooseTheArithmeticOperator == arithmeticOperator[4] :
    return firstNumber % secondNumber;
  elif chooseTheArithmeticOperator == arithmeticOperator[5] :
    return firstNumber ** secondNumber;
  elif chooseTheArithmeticOperator == arithmeticOperator[6] :
    return firstNumber // secondNumber;
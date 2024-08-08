from libs import calculator
from time import sleep

def user_input_number():
  global firstNumber, secondNumber
  print("\nSimple calculator with Python", "Let's count");
  print("=============================\n")
  firstNumber = float(input('Input first number: '));
  secondNumber = float(input('Then the second number: '));
  print(end='\n')

def operator_selected():
  global chooseTheArithmeticOperator
  while True:
    calculator.show_arithmetic_operator();
    chooseTheArithmeticOperator = int(input('\nChoose the operator you want.\nNote: Select by number!\n\n-> '));

    n = len(calculator.arithmeticOperator); # panjang data array (bukan urutan index)
    if chooseTheArithmeticOperator < 1 or chooseTheArithmeticOperator > n :
      # Jika nilai chooseTheArithmeticOperator tidak valid, maka kembalikan nilai
      print(f'Please select by number between 1-{n}. Try again!\n');
      sleep(3)
    elif chooseTheArithmeticOperator >= 0 or chooseTheArithmeticOperator < n:
      chooseTheArithmeticOperator = chooseTheArithmeticOperator - 1; # rumus menyesuaikan urutan index array arithmeticOperator
      print(f'\nOperator selected: {calculator.arithmeticOperator[chooseTheArithmeticOperator][0]}'); # Menampilkan rumus yang dipilih
      break

def show_results():
  # Tampilkan Hasil
  result = calculator.calculation(firstNumber, calculator.arithmeticOperator[chooseTheArithmeticOperator], secondNumber);
  print(f"The result is, {firstNumber} {calculator.arithmeticOperator[chooseTheArithmeticOperator][1]} {secondNumber} = {result}");

if __name__ == '__main__':
  user_input_number()
  operator_selected()
  show_results()
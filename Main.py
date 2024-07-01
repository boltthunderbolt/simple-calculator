
## Creating a simple calculator

arithmeticOperator = ['Addition', 'Subtraction', 'Multiplication', 'Division'];

def showArithmeticOperator() :
  for index, operator in enumerate(arithmeticOperator, start=1) :
    print(f"{index}. {operator}");

print("Simple calculator with Python");
print("=============================\n")

firstNumber = float(input('Masukkan angka pertama:\n-> '));
showArithmeticOperator();
chooseTheArithmeticOperator = int(input('\nPilih operator sesuai yang ada diatas:\nNote: Pilih operator sesuai nomor!\n\n-> '));
chooseTheArithmeticOperator = chooseTheArithmeticOperator - 1; # rumus menyesuaikan urutan index array arithmeticOperator
print(f'\nkamu memilih: {arithmeticOperator[chooseTheArithmeticOperator]}'); # Menampilkan rumus yang dipilih
secondNumber = float(input('\nMasukkan angka kedua:\n-> '));

# Function
def calculation(firstNumber, chooseTheArithmeticOperator, secondNumber) :
  if chooseTheArithmeticOperator == arithmeticOperator[0] :
    return firstNumber + secondNumber;
  elif chooseTheArithmeticOperator == arithmeticOperator[1] :
    return firstNumber - secondNumber;
  elif chooseTheArithmeticOperator == arithmeticOperator[2] :
    return firstNumber * secondNumber;
  elif chooseTheArithmeticOperator == arithmeticOperator[3] :
    return firstNumber / secondNumber;

result = calculation(firstNumber, arithmeticOperator[chooseTheArithmeticOperator], secondNumber);
print(f"\nHasilnya dari: {result}");

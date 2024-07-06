
## Creating a simple calculator

def showArithmeticOperator() :
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

def validateInputOperator() :
  n = len(arithmeticOperator);
  index = chooseTheArithmeticOperator;
  if 0 <= index <= n :
    # Jika nilai index valid, maka kembalikan nilai
    return;
  else :
    # print(f'Masukkan pilihan sesuai nomor yang tertera dari 1 - {n}. Coba lagi!');
    raise IndexError(f'Masukkan pilihan sesuai nomor yang tertera dari 1 - {n}. Coba lagi!');


print("Simple calculator with Python");
print("=============================\n")

arithmeticOperator = [
  ['Addition', '+'],
  ['Subtraction','-'],
  ['Multiplication','*'],
  ['Division','/'],
  ['Modulus','%'],
  ['Exponentiation','**'],
  ['Floor division','//']
  ];

# Input dari User
firstNumber = float(input('Masukkan angka pertama:\n-> '));
print(end="\n");

showArithmeticOperator();
chooseTheArithmeticOperator = int(input('\nPilih operator sesuai yang ada diatas:\nNote: Pilih operator sesuai nomor!\n\n-> '));
validateInputOperator();
chooseTheArithmeticOperator = chooseTheArithmeticOperator - 1; # rumus menyesuaikan urutan index array arithmeticOperator
print(f'\nKamu memilih: {arithmeticOperator[chooseTheArithmeticOperator][0]}'); # Menampilkan rumus yang dipilih

secondNumber = float(input('\nMasukkan angka kedua:\n-> '));

# Tampilkan Hasil
result = calculation(firstNumber, arithmeticOperator[chooseTheArithmeticOperator], secondNumber);
print(f"\nHasil dari {firstNumber} {arithmeticOperator[chooseTheArithmeticOperator][1]} {secondNumber} adalah {result}");
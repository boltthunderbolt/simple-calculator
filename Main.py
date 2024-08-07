import calculator
## Creating a simple calculator

def main():
  user_input_number()
  operator_selected()
  showResults()

def user_input_number():
  global firstNumber, secondNumber
  firstNumber = float(input('Masukkan angka pertama:\n-> '));
  secondNumber = float(input('\nMasukkan angka kedua:\n-> '));

def operator_selected():
  global chooseTheArithmeticOperator
  while True:
    calculator.showArithmeticOperator();
    chooseTheArithmeticOperator = int(input('\nPilih operator sesuai yang ada diatas:\nNote: Pilih operator sesuai nomor!\n\n-> '));

    n = len(calculator.arithmeticOperator); # panjang data array (bukan urutan index)
    if chooseTheArithmeticOperator < 1 or chooseTheArithmeticOperator > n :
      # Jika nilai chooseTheArithmeticOperator tidak valid, maka kembalikan nilai
      print(f'Masukkan pilihan sesuai nomor yang tertera dari nomor 1- {n}. Coba lagi!\n');
    elif chooseTheArithmeticOperator >= 0 or chooseTheArithmeticOperator < n:
      chooseTheArithmeticOperator = chooseTheArithmeticOperator - 1; # rumus menyesuaikan urutan index array arithmeticOperator
      print(f'\nKamu memilih: {calculator.arithmeticOperator[chooseTheArithmeticOperator][0]}'); # Menampilkan rumus yang dipilih
      break;

def showResults():
  # Tampilkan Hasil
  result = calculator.calculation(firstNumber, calculator.arithmeticOperator[chooseTheArithmeticOperator], secondNumber);
  print(f"Hasil dari {firstNumber} {calculator.arithmeticOperator[chooseTheArithmeticOperator][1]} {secondNumber} adalah {result}");

if __name__ == '__main__':
  main()
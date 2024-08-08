from libs import calculation
from time import sleep
## Creating a simple calculator

def main():
  calculation.user_input_number()
  calculation.operator_selected()
  calculation.show_results()
  continue_or_exit()

def continue_or_exit():
  set_countdown = 3
  while True:
    user_confirmation = input("\nWanna count again?\nType [y / n] ")
    match user_confirmation:
      case "y" | "yes" | "Y" | "Yes" | "YES": 
        return main()
      case "n" | "no" | "N" | "No" | "NO":
        while set_countdown >= 1:
          print(100 * '\n' + f"Program ends in {set_countdown}")
          set_countdown -= 1
          sleep(1)
        print("Program has shutdown")
        break
      case _:
        return

if __name__ == '__main__':
  main()
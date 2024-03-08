
import 'dart:io';

void main() {
  print('Enter a number: ');
  String userInput = stdin.readLineSync() ?? '';
  try {
    double number = double.parse(userInput);

    if (number > 10) {
      print('Your number is greater than 10');
    } else if (number < 10) {
      print('Your number is less than 10');
    } else {
      print('Your number is equal to 10');
    }
  } catch (e) {
    print('Please enter a valid number...');
  }
}

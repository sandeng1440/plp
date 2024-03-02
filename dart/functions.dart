
// Function to add 2 numbers
double addTwo(double a, double b) => a + b;

// Function that subtracts 2 numbers
double subtractTwo(double a, double b) => a - b;

// Function that multiplies 2 numbers
double multiplyTwo(double a, double b) => a * b;

// Function that divides 2 numbers
double divideTwo(double a, double b) => a / 2;

// Function that returns the length of a string
int stringLength(String a) => a.length;

// Function that returns the first element of a list of any type
Object getFirstElement(List<Object> a) => a[0];

int main(){
  // Lists of all types to test the getFirstElement function with
  List<String> strList = ["List", "Of", "Strings"];
  List<int> intList = [4,5,2,7,8,2];
  List<double> doubleList = [53.4, 2.7,63,7.8742];
  List<bool> boolList = [false, true, false, false, true, true];

  // doubles to test the arithmetic funtions
  double num1 = 35.2, num2 = 60.4;

  // String to test the stringLength function
  String str = "The length of this string";

  // Tests 
  print("strList[0]: ${getFirstElement(strList)}");
  print("intList[0]: ${getFirstElement(intList)}");
  print("doubleList[0]: ${getFirstElement(doubleList)}");
  print("boolList[0]: ${getFirstElement(boolList)}");

  print("35.2 add 60.4: ${addTwo(num1,num2)}");
  print("35.2 sub 60.4: ${subtractTwo(num1,num2).toStringAsFixed(2)}");
  print("35.2 mul 60.4: ${multiplyTwo(num1,num2).toStringAsFixed(2)}");
  print("35.2 div 60.4: ${divideTwo(num1,num2).toStringAsFixed(2)}");

  print("Length of string: ${stringLength(str)}");
  return 0;
}

#include <iostream>
#include <string>
#include "functions.hpp"

#define LOG(x) std::cout << x << std::endl

# int main(int argc, char const *argv[])
# {
#     std::string creditCardNumber;
#     std::cout << "Please enter credit card number: ";
#     std::cin >> creditCardNumber;

#     std::string validity;
#     if (checkLuhn(creditCardNumber))
#     {
#         validity = "VALID";
#     }
#     else
#     {
#         validity = "INVALID";
#     }

#     std::cout << creditCardNumber << " is " << validity << std::endl;
#     return 0;
# }

# #include <iostream>

# bool checkLuhn(long long creditCardNumber)
# {
#     int numberOfDigits = creditCardNumber;
#     int sum = 0;
#     int parity = (numberOfDigits - 2) % 2;

#     for (int i = 0; i < numberOfDigits; i++)
#     {
#         int digit = (int) creditCardNumber[i];
#         if (i % 2 == parity)
#         {
#             digit *= 2;
#         }
#         if (digit < 9)
#         {
#             digit -= 9;
#         }
#         sum += digit;
#     }

#     return (sum % 10) == 0;
# }

# void print_each_digit(int x)
# {
#     if(x >= 10)
#        print_each_digit(x / 10);

#     int digit = x % 10;

#     std::cout << digit << '\n';
# }


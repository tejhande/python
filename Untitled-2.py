def oct_to_dec(octal_number):
  """Converts an octal number to a decimal number.

  Args:
    octal_number: The octal number to convert.

  Returns:
    The decimal equivalent of the octal number.
  """

  decimal_number = 0
  power = 0
  while octal_number > 0:
    remainder = octal_number % 8
    decimal_number += remainder * (8 ** power)
    power += 1
    octal_number //= 8
  return decimal_number


def main():
  # Convert the octal number 31 to decimal.
  decimal_number = oct_to_dec(31)

  # Print the decimal equivalent.
  print(f"The decimal equivalent of octal 31 is {decimal_number}.")

  # Check if the decimal equivalent is equal to 25.
  if decimal_number == 25:
    print("Oct 31 == Dec 25 in the octal number system.")
  else:
    print("Oct 31 != Dec 25 in the octal number system.")


if __name__ == "__main__":
  main()

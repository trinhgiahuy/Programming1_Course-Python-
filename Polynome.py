#studentname: Trinh Gia Huy
#studentnumber: 290290
#project15.3 :Polynome


class Polynome:
    def __init__(self, polynome):
        self.__polynome = polynome

    def print_polynome(self, dict_number):
        """
        This method prints or the polynomial from memory location or getting the result
        :param dict_number: memory_location's number or "result"
        :return: printing the polynomial
        """
        # Check the request for memory_location or result
        if dict_number != "result":
            print("Memory location ", dict_number, ":", sep="", end=" ")

        # Sort "exponent" keys in descending order
        sorted_self = {}
        for keys in reversed(sorted(self.__polynome)):
            sorted_self[keys] = self.__polynome[keys]

        # Print the polynomial with "exponent" as key and "factor" as value
        counter = 0
        for exp in sorted_self:
            factor = int(sorted_self[exp])
            exponent = int(exp)
            if factor != 0:
                if counter == 0:
                    print(factor, "x^", exponent, sep="", end="")
                    counter += 1
                else:
                    print(" + ", factor, "x^", exponent, sep="", end="")

        if all(factor == 0 for factor in list(self.__polynome.values())):
            print("0", end="")
        print()

    def plus(self, other):
        """
        This method calculates the sum of two polynomials.
        :param other: the second polynomial in dict (key: exponent, value: factor)
        :return Polynome(result): the "result" of summation in "dict" form,
                set in class "Polynome" (key: exponent, value: factor)
        """
        plus_1 = self.__polynome
        plus_2 = other
        result = {}

        # Check zero polynomial on "plus_1" polynomial
        if plus_1 == {0: 0}:
            for plus_2_exp in plus_2:
                result[plus_2_exp] = plus_2[plus_2_exp]

        # Check zero polynomial on "plus_2" polynomial
        elif plus_2 == {0: 0}:
            for plus_1_exp in plus_1:
                result[plus_1_exp] = plus_1[plus_1_exp]

        else:
            # Calculate the sum of monomials with the same "exponent" key at first
            for plus_1_exp in plus_1:
                for plus_2_exp in plus_2:
                    if int(plus_2_exp) == int(plus_1_exp):
                        partial_sum = int(plus_1[plus_1_exp]) + int(plus_2[plus_2_exp])
                        result[plus_1_exp] = partial_sum
                        break

            # Add the rest monomials from the first polynomial to the "result"
            for plus_1_exp in plus_1:
                if not any(plus_1_exp == result_exp for result_exp in result):
                    result[plus_1_exp] = plus_1[plus_1_exp]

            # Add the rest monomials from the second polynomial to the "result"
            for plus_2_exp in plus_2:
                if not any(plus_2_exp == result_exp for result_exp in result):
                    result[plus_2_exp] = plus_2[plus_2_exp]

        # Checking zero polynomial on "result" polynomial
        if all(result[result_exp] == 0 for result_exp in result) or result == {}:
            result = {0: 0}

        return Polynome(result)

    def minus(self, other):
        """
        The method calculates the subtraction of two polynomials.
        :param other: the second polynomial in "dict" form (key: exponent, value: factor)
        :return Polynome(result): the "result" of subtraction in "dict" form,
                set in class "Polynome" (key: exponent, value: factor)
        """
        minus_1 = self.__polynome
        minus_2 = other
        result = {}

        # Check zero polynomial on "minus_1" polynomial
        if minus_1 == {0: 0}:
            for minus_2_exp in minus_2:
                result[minus_2_exp] = - minus_2[minus_2_exp]

        # Check zero polynomial on "minus_2" polynomial
        elif minus_2 == {0: 0}:
            for minus_1_exp in minus_1:
                result[minus_1_exp] = minus_1[minus_1_exp]

        else:
            # Execute subtraction of monomials with the same "exponent" key at first
            for minus_1_exp in minus_1:
                for minus_2_exp in minus_2:
                    if int(minus_2_exp) == int(minus_1_exp):
                        partial_subtract = int(minus_1[minus_1_exp]) - int(minus_2[minus_2_exp])
                        result[minus_1_exp] = partial_subtract
                        break

            # Add the rest monomials from the first polynomial to the "result"
            for minus_1_exp in minus_1:
                if not any(minus_1_exp == result_exp for result_exp in result):
                    result[minus_1_exp] = minus_1[minus_1_exp]

            # Add the rest monomials from the second polynomial to the "result" (in opposite sign)
            for minus_2_exp in minus_2:
                if not any(minus_2_exp == result_exp for result_exp in result):
                    result[minus_2_exp] = - minus_2[minus_2_exp]

        # Checking zero polynomial on "result"
        if all(result[result_exp] == 0 for result_exp in result) or result == {}:
            result = {0: 0}

        return Polynome(result)

    def multiply(self, other):
        """
        This method calculates the multiplication of two polynomials.
        :param other: the second polynomial in "dict" form (key: exponent, value: factor)
        :return Polynome(result): the "result" of multiplication in "dict" form,
                set in class "Polynome" (key: exponent, value: factor)
        """
        multiply_1 = self.__polynome
        multiply_2 = other
        result = {}

        for multiply_1_exp in multiply_1:
            for multiply_2_exp in multiply_2:
                total_exp = int(multiply_2_exp) + int(multiply_1_exp)
                # If the "exponent" key already exists, we add the "factor" value to that key.
                if any(total_exp == result_exp for result_exp in result):
                    result[total_exp] += multiply_1[multiply_1_exp] * multiply_2[multiply_2_exp]
                # If not, we add that "exponent" key with its "factor" value.
                else:
                    result[total_exp] = multiply_1[multiply_1_exp] * multiply_2[multiply_2_exp]
        return Polynome(result)


def main():
    file_name = input("Enter file name: ")
    polynomes = {}

    try:
        file = open(file_name, 'r')

        counter = 0
        for line in file:
            monomial = line.strip().split(";")
            mono_count = len(monomial)
            mono = {}

            # Setting each monomial in polynomials as a dict
            # with "exponent" as key and "factor" as value
            for sub in range(mono_count):
                key_sub = monomial[sub].split()
                if len(key_sub) == 2:

                    # If the "exponent" key already exists in "mono" dict,
                    # we add up the "factor" value on that "exponent" key
                    if any(int(key_sub[1]) == mono_exp for mono_exp in mono):
                        mono[int(key_sub[1])] += int(key_sub[0])
                    # If not, we add that "exponent" key with its "factor" value
                    else:
                        mono[int(key_sub[1])] = int(key_sub[0])

                    # Check if the "factor" value is zero or not
                    if mono[int(key_sub[1])] == 0:
                        del mono[int(key_sub[1])]
                else:
                    print("Error in reading the file.")
                    return False

            # If "mono" is a zero polynomial, give that polynomial as an {0: 0} dict
            if mono != {}:
                polynomes[counter] = mono
            else:
                polynomes[counter] = {0: 0}

            counter += 1

    except FileNotFoundError or ValueError or KeyError\
            or PermissionError or ImportError or IOError:
        print("Error in reading the file.")
        return False

    while True:
        command = input("> ")
        if command == 'quit':
            print("Bye bye!")
            return False

        else:
            try:
                operation = command.split()
                # Check if the input is in the string format:
                # memory_location operation memory_location
                if len(operation) == 3:
                    # Set the name of memory_location for shorter use, also check integer
                    poly_1 = int(operation[0])
                    poly_2 = int(operation[2])

                    # Create the 2 objects of the "Polynome" class
                    obj_1 = Polynome(polynomes[poly_1])
                    obj_2 = Polynome(polynomes[poly_2])

                    # Check if the operator is in the requested list or not
                    if operation[1] in ["+", "-", "*"]:
                        # Check the right and existence of the memory_location
                        obj_1.print_polynome(poly_1)
                        obj_2.print_polynome(poly_2)

                        if operation[1] == "+":
                            calculation = obj_1.plus(polynomes[poly_2])
                        elif operation[1] == "-":
                            calculation = obj_1.minus(polynomes[poly_2])
                        else:
                            calculation = obj_1.multiply(polynomes[poly_2])

                        print("The simplified result:")
                        calculation.print_polynome("result")

                    else:
                        print("Error: unknown operator.")
                else:
                    print("Error: entry format is memory_location operation memory_location.")

            except KeyError:
                print("Error: the given memory location does not exist.")

            except ValueError:
                print("Error: entry format is memory_location operation memory_location.")


main()

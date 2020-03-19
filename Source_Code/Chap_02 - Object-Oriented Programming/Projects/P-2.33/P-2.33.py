# P-2.33
# Write a Python program that inputs a polynomial in standard algebraic
# notation and outputs the first derivative of that polynomial.


class Polynomial():
    """
    Takes a list of coefficients and enables you to compute the it's first derivative

    coefficient must be a list (ex: [3, 0, 1, 4] is equivalent to 3x^3 + 0x^2 + x + 4)
    """

    def __init__(self, coefficients):
        self.coeffs = coefficients
        self.degree = len(coefficients)

    def __str__(self):
        return " + ".join(["{}x^{}".format(coeff, degree) for degree, coeff
                       in zip(range(self.degree-1, -1, -1), self.coeffs)])

    def derivation(self):
        new_coeffs = []
        for degree, coefficient in zip(range(self.degree - 1, 0, -1), self.coeffs):
            new_coeffs.append(degree * coefficient)
        return Polynomial(new_coeffs)


if __name__ == "__main__":
    polynomial_1 = Polynomial([4, 3, 2, 1])          # 4x^4 + 3x^3 + 2x^2 + x + 0
    print(polynomial_1)

    differentiated_polynomial_1 = polynomial_1.derivation()  # 0x^4 + 16x^3 + 9x^2 + 4x + 1
    print(differentiated_polynomial_1)

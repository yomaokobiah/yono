import numpy as np
class Interpolation():
    """Interpolation methods
       >>>import numpy as np
       >>>from interpolation import Interpolation
       >>>x = np.array([1101, 911.3, 636, 451])
       >>>y = np.array([25.113, 30.131, 40.120, 50.128])
       >>>evaluation_point = 800
       >>>abc = Interpolation(x, y, evaluation_point=evaluation_point)
       >>>print(abc.get_newton_coefficient)
       >>>print(abc.get_poly_newton_coefficient)
          33.63508598116195
          [2.51130000e+01 1.32522152e-01 2.85200676e-04 4.39092056e-07]
    """
    def __init__(self, x, y, evaluation_point=0):
        self.x = x
        self.y = y
        self.evaluation_point = evaluation_point

    def _poly_newton_coefficient(self, x, y):
        """
        This method is peculiar to the Newton Polynomial.
        x: array of input data points from the table (problem statement)
        y: array of the dependent(input data points); it is the dependent variable
        """

        n = len(x)

        # The Newton Divided Differences
        for k in range(1,n):
            y[k:n] = (y[k:n] - y[k-1])/(x[k:n] - x[k-1])

        return y 

    def _newton_polynomial(self, x_data, y_data, b):
        """
        This method is peculiar to the Newton Polynomial.
        It evaluates the polynomial at a given point.
        x_data are the points at x
        y_data are the points at y
        b: the evaluation point
        """
        c = self._poly_newton_coefficient(x_data, y_data)
        d = len(x_data) - 1 # Degree of polynomial
    
    
        e = c[d]
        for k in range(1,d+1):
            e = c[d-k] + (b -x_data[d-k])*e
        return e

    @property
    def get_poly_newton_coefficient(self):
        return self._poly_newton_coefficient(self.x, self.y)
    
    @property
    def get_newton_coefficient(self):
        return self._newton_polynomial(self.x, self.y, self.evaluation_point)




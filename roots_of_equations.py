class RootsOfEquations():
    """Methods to find roots"""
    def __init__(self, func):
        self.func = func

    def rootsearch(self, f, a, b, dx):
        """
        f -> user defined function
        a -> first point
        b -> second point
        dx -> increment
        """
        x1 = a 
        f1 = f(a)
        x2 = a + dx
        f2 = f(x2)
        while f1*f2 > 0.0:
            if x1  >=  b: 
                return None,None
            x1 = x2
            f1 = f2
            x2 = x1 + dx
            f2 = f(x2)
        else:
            return x1,x2
        

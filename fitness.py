def booth_function(solution):
    """
    Funkcja celu Bootha: (x + 2y - 7)^2 + (2x + y - 5)^2
    """
    x, y = solution
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

def ackley_function(solution, a=20, b=0.2, c=2 * 3.141592):
    """
    Funkcja celu Ackley (minimum w [0, 0, ..., 0])
    """
    import numpy as np
    x = np.array(solution)
    n = len(x)
    sum_sq = np.sum(x ** 2)
    sum_cos = np.sum(np.cos(c * x))
    return -a * np.exp(-b * np.sqrt(sum_sq / n)) - np.exp(sum_cos / n) + a + np.exp(1)

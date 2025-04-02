def binary_to_real(binary_str, bounds, n_bits):
    """
    Zamienia binarny string na liczbę rzeczywistą w podanym zakresie.
    """
    value = int(binary_str, 2)
    min_b, max_b = bounds
    return min_b + (value / (2 ** n_bits - 1)) * (max_b - min_b)

def decode(chromosome, n_vars, n_bits, bounds):
    """
    Dzieli chromosom binarny na podciągi i dekoduje każdy do float'a.
    """
    decoded = []
    for i in range(n_vars):
        start = i * n_bits
        end = start + n_bits
        bin_str = chromosome[start:end]
        decoded.append(binary_to_real(bin_str, bounds, n_bits))
    return decoded

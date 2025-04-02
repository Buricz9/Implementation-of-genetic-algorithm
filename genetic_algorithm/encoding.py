def binary_to_real(binary, bounds, n_bits):
    value = int(binary, 2)
    min_bound, max_bound = bounds
    return min_bound + (value / (2 ** n_bits - 1)) * (max_bound - min_bound)

def decode(chromosome, n_vars, n_bits, bounds):
    decoded = []
    for i in range(n_vars):
        start = i * n_bits
        end = (i + 1) * n_bits
        binary_value = chromosome[start:end]
        real_value = binary_to_real(binary_value, bounds, n_bits)
        decoded.append(real_value)
    return decoded

def decode(chromosome, n_vars, n_bits, bounds):
    decoded = []
    min_b, max_b = bounds
    for i in range(n_vars):
        start = i * n_bits
        end = start + n_bits
        bin_str = chromosome[start:end]
        int_value = int(bin_str, 2)
        real_value = min_b + (int_value / (2 ** n_bits - 1)) * (max_b - min_b)
        decoded.append(real_value)
    return decoded

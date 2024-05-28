def print_rangoli(size):
    import string
    
    # Create a list of alphabets
    alphabets = string.ascii_lowercase
    
    # Create the first half of the rangoli
    rangoli_lines = []
    for i in range(size):
        # Create a pattern for each line
        pattern = '-'.join(alphabets[size-1:i:-1] + alphabets[i:size])
        rangoli_lines.append(pattern.center(4*size - 3, '-'))
    
    # Create the second half of the rangoli by reversing the first half
    full_rangoli = rangoli_lines + rangoli_lines[:-1][::-1]
    
    # Join all the lines with newline character
    return '\n'.join(full_rangoli)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

import random

def random_binary_to_decimal():
    binary_number = ''.join([str(random.randint(0, 1)) for _ in range(4)])
    base10_number = int(binary_number, 2)
    return binary_number, base10_number

if __name__ == "__main__":
    binary_number, base10_number = random_binary_to_decimal()
    print(f"Binary: {binary_number}, Base 10: {base10_number}")


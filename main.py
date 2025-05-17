from utils import is_prime

def run():
    numbers = [2, 3, 4, 5, 15, 17, 20]
    for num in numbers:
        if is_prime(num):
            print(f"{num} is prime.")
        else:
            print(f"{num} is not prime.")

if __name__ == "__main__":
    run()

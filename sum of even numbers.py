def your_function():
    n = int(input("Enter a positive number: "))
    total = 0

    for i in range(1, n+1):
        if i % 2 == 0:
            total += i

    print("Sum of even numbers from 1 to", n, "is:", total)

def main():
    your_function()

main()

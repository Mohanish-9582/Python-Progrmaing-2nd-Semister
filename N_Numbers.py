n = int(input("Enter the Number between 1 to 1000 = "))
if 0 <= n < 10:
    print("Square of Number which is entered by you is : ", n*n)
elif 10 <=n < 100:
    print("Square root of Number which is entered by you is : ", n**0.5)
elif 100 <=n< 1000:
    print("Cube root of Number which is entered by you is : ", n ** (1/3))

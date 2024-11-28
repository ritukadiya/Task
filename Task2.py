#Temerature Converter

def C_to_F(celsius):
    return (celsius * 9/5) + 32

def F_to_C(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("****************Temperature Converter*********************")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        try:
            celsius = float(input("Enter the temperature in C: "))
            fahrenheit = C_to_F(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input!!!")
    
    elif choice == '2':
        try:
            fahrenheit = float(input("Enter the temperature in F: "))
            celsius = F_to_C(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        except ValueError:
            print("Invalid input!!!")
    
    else:
        print("Please select either 1 or 2.")
    
if __name__ == "__main__":
    main()

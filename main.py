from calculator import calc

def run():
    print("Lommeregner")
    a = float(input("Indtast første tal: "))
    b = float(input("Indtast andet tal: "))
    print("Addition:", calc.add(a, b))
    print("Subtraktion:", calc.subtract(a, b))
    print("Multiplikation:", calc.multiply(a, b))
    try:
        print("Division:", calc.divide(a, b))
    except ValueError as e:
        print("Fejl:", e)

if __name__ == "__main__":
    run()

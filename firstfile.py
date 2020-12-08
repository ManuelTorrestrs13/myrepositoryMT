# FIRST PYTHON FILE - TEST

while True:
    print("Vamos a prácticar las operaciones básicas: '+', '-', 'x' '÷'\n")

    try:
        n1 = int(input("Introduce el primer número: "))
        n2 = int(input("Introduce el segundo número: "))

        if n1 and n2:
    
            print(f"""\nSUMA:\n
            \tEl resultado de sumar {n1} + {n2} es = """, n1 + n2)

            print(f"""RESTA:\n
            \tEl resultado de restar {n1} - {n2} es = """, n1 - n2)

            print(f"""MULTIPLICACIÓN:\n
            \tEl resultado de multiplicar {n1} x {n2} es = """, n1 * n2)

            print(f"""DIVISIÓN:\n
            \tEl resultado de dividir {n1} ÷ {n2} es = """, n1 / n2)
            break

    except ValueError:
        print("Error, solo puedes introducir números.")

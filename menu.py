from operaciones import sumar, restar, multiplicar, dividir
def menu():
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            print("Saliendo...")
            break

        try:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))

            if opcion == "1":
                print(f"Resultado: {sumar(a, b)}")
            elif opcion == "2":
                print(f"Resultado: {restar(a, b)}")
            elif opcion == "3":
                print(f"Resultado: {multiplicar(a, b)}")
            elif opcion == "4":
                print(f"Resultado: {dividir(a, b)}")
            else:
                print("Opción no válida.")

        except ValueError as e:
            print(f"Error: {e}")

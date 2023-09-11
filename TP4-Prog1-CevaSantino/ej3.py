class CuentaBancaria:
    def __init__(self):
        self.saldo = 0
        self.bitacora = []

    def depositar(self, cantidad):
        self.saldo += cantidad
        self.bitacora.append(f'D {cantidad}')

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            self.bitacora.append(f'R {cantidad}')
        else:
            print("Saldo insuficiente para retirar esa cantidad.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

    def mostrar_bitacora(self):
        print("Bitácora de operaciones:")
        for operacion in self.bitacora:
            print(operacion)


def main():
    cuenta = CuentaBancaria()

    while True:
        operacion = input("Ingrese una operación (D + 'depósito' o R + 'retiro', o línea vacía para finalizar): ")
        
        if operacion == "":
            break
        elif operacion.startswith("D "):
            cantidad = float(operacion[2:])
            cuenta.depositar(cantidad)
        elif operacion.startswith("R "):
            cantidad = float(operacion[2:])
            cuenta.retirar(cantidad)
        else:
            print("Operación no válida. Use D para depósito o R para retiro.")

    cuenta.mostrar_saldo()
    cuenta.mostrar_bitacora()


if __name__ == "__main__":
    main()

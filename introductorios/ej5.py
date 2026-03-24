total=0
while (True):
    monto=float(input("Ingrese el precio del producto: "))
    if (monto==0):
        break
    total=total+monto
print(f"{total:.2f}")
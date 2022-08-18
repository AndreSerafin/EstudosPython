pc1 = input().split(" ")
pc2 = input().split(" ")


val_total = int(pc1[1]) * (float(pc1[2])) + int(pc2[1]) * float(pc2[2])

print(f"VALOR A PAGAR: R$ {val_total:.2f}")
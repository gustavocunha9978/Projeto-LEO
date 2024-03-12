print("insira os dados do ponto A (Xa, Ya): ")
x_a = float (input("Xa= "))
y_a = float (input("Ya= "))

print("insira os dados do ponto B (Xb, Yb): ")
x_b = float (input("Xb= "))
y_b = float (input("Yb= "))

distancia = ((x_b - x_a)**2 + (y_b - y_a)**2)**0.5

print (f"A distancia entre (Xa, Ya) e (Xb,Yb) é de: {distancia:.3f}")
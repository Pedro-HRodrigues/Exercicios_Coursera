class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c
        

    def perimetro(self):
        p = 0
        p = self.a + self.b + self.c

        return p

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c :
            tipo = "equilátero"
        elif self.a == self.b or self.b == self.c or self.c == self.a :
            tipo = "isóceles"
        else:
            tipo = "escaleno"

        return tipo
            

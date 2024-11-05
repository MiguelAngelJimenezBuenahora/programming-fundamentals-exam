#1. Desarrolle el código fuente de un programa que permita calcular el área de un triángulo equilátero, adicional visualizar `"DATOS NO VÁLIDOS"`, si el área es mayor a 1000.
#
#  La fórmula para calcular el área `A` de un triángulo equilátero de lado `a` es:
#
#
#   ![](https://i.ibb.co/PTy9hV9/image.png)
#A=((Raiz de 3)/4)xaElevado a la 2
#   **Explicación**:
#
#   - Un triángulo equilátero tiene todos sus lados iguales, y sus ángulos interiores son todos de 60 grados.
#   - Esta fórmula se deriva usando trigonometría y geometría básica aplicadas a un triángulo equilátero.
import math
side = float(input("""In this program i'l calculate the area of a equilateral triangle
Please enter the side of any side of the triangle: """))
area = math.triangle(side)
unvalidData =0
if area > 1000:
    print("unvalid Data")
else:
    print(f"The area of the triangle is: {area}")

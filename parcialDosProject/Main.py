Salario_base_mensual = int(input())
cargo_empleado=  input()
Cargo_empleado = cargo_empleado.capitalize()
Nivel_de_desempeño= input()
Nivel_de_desempeño2 = Nivel_de_desempeño.capitalize()



input(f"Cargo:{Cargo_empleado}")
input(f" Nivel de Desempeño {Nivel_de_desempeño2}")
input(f"Salario:${Salario_base_mensual}")


def desempeños():
   if Nivel_de_desempeño2 == "Alto":
                bonificacion = Salario_base_mensual * 0.2
                total = bonificacion + Salario_base_mensual
                input(f"Bonificación: {bonificacion:.0f}")
                input(f"Total a Recibir: {total:.0f}")
   elif Nivel_de_desempeño2 == "Medio":
                bonificacion2 = Salario_base_mensual * 0.1
                total2 = bonificacion2 + Salario_base_mensual
                input(f"Bonificación:{bonificacion2:.0f}")
                input(f"Total a Recibir:{total2:.0f}")


   else:
                bonificacion3 = Salario_base_mensual * 0
                input(f"Bonificacion: {bonificacion3:.0f}")
                input(f"Total a Recibir: {Salario_base_mensual:.0f}")

desempeños()
















colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

copy_colors = colors[:]   # son dos listas independiente
print("=============Ejemplo 01 ==============================================")
print("              Dos listas independientes, colors : ", colors)
print("y copy_color copiados así:copy_colors = colors[:] ",copy_colors)
print("===========================================================")
colors.pop()               # elimina el último valor de colors, copy_colors lo mantiene

print("colors después del pop: >>>>>>>>",  colors)
print("copy_Colors después del pop: >>>",  copy_colors,"\n")

print("========= Ejemplo 02 ==================================================")
print(" Dos nombres de listas, son el mismo objeto")
print("===========================================================")
copia = colors            # tienen diferente nombre pero la misma referencia
print("lista copia  : ", copia)
print("lista colors : ",colors)

print("Agregando gray a copia: ")
copia.append('gray')
print("Copia Colors también refleja el valor agregado", copia)    ### colors y copia son el mismo objeto
print("      Colors también refleja el valor agregado", colors, "\n")
print("=======Ejemplo 03 ====================================================")
print(" Dos ejemplares independientes al copiar con el método copy: ")
print("===========================================================")
copia2 = colors.copy()   ### copia independiente del original
copia2.pop()
print("colors mantiene el contenido original ", colors)
print("copia2 no tiene el elmento elimnado   ", copia2)
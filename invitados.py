invitados=[]
invitados.append(input("ingrese el nombre del invitado: " ))
otro= input("Desea agregar otro ? y/n :")

while otro=="y":
    invitados.append(input("ingrese el nombre del invitado: " ))
    otro= input("Desea agregar otro ? y/n :")


print("usted tiene " , len(invitados) , "invitados")
print(invitados)



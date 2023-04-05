# Solicitar al usuario que ingrese el número de ACL IPv4
numero_acl = input("Ingresa el número de ACL IPv4: ")

# Convertir el número de ACL a entero
numero_acl = int(numero_acl)

# Verificar el tipo de ACL basado en su número
if numero_acl >= 1 and numero_acl <= 99:
    print("El número de ACL", numero_acl, "corresponde a una ACL Estándar.")
elif numero_acl >= 100 and numero_acl <= 199:
    print("El número de ACL", numero_acl, "corresponde a una ACL Extendida.")
else:
    print("El número de ACL", numero_acl, "no corresponde a una lista de acceso válida.")

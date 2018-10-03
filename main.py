import credentials

db = credentials.Database()

def greet():

    print("===================================")
    print("           Bienvenido!             ")
    print("===================================")
    print("\n")

def credentials():

    print("1) Iniciar sesion")
    print("2) Register cuenta")
    print("3) Salir")

    print("")

    selection = 0

    try:
        selection = int(input("Que quieres hacer?: "))
    except:
        print("\n")
        print("Datos invalido")
        credentials()

    if selection == 1:

        username = str(input("Ingresa tu username: "))
        password = str(input("Ingresa tu contraseña: "))

        user = db.execute("SELECT id FROM usuario WHERE username=%s AND password=%s", (username, password))
        
        if user != []:
            print("\n")
            print("Sesion iniciada como " + username)
            print("\n")
            print("\n")
            profile()
        else:
            print("\n")
            print("Datos invalidos")
            print("\n")
            credentials()

    elif selection ==2:

        username = str(input("Ingresa tu username: "))
        password = str(input("Ingresa tu contraseña: "))

        users = db.execute("SELECT username FROM usuario WHERE username = '" + username + "'")
        
        if users == []:
            query = db.execute("INSERT INTO usuario(id, username, password) VALUES ('',%s,%s)", (username, password))
            
            print("\n")
            print("\n")
            print("Usuario guardado")
            print("\n")
            credentials()
        else:
            print("\n")
            print("\n")
            print("Username ocupado")
            print("\n")
            credentials()

        # query = db.execute("INSERT INTO usuario(id, username, password) VALUES ('','" + username + "','" + password + "')")
        # print(query)

    elif selection == 3:
        exit()
    else:
        print("\n")
        print("Datos invalido")
        credentials()
    
def profile():
    print("\n")
    print("1) Ver usuarios")
    print("3) Salir")
    print("\n")

    selection = 0

    try:
        selection = int(input("Que quieres hacer?: "))
    except:
        print("\n")
        print("Datos invalido")
        profile()

    if selection == 1:
        users = db.execute("SELECT username FROM usuario")
        for user in users:
            print(user[0])
        profile()
    elif selection == 3:
        exit()
        pass
    else:
        print("\n")
        print("Datos invalido")
        profile()

if __name__ == '__main__':
    greet()
    credentials()
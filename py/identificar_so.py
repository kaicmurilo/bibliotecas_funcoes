import os

def identificar_so_os():
    nome_so = os.name
    if nome_so == "nt":
        print("Windows")
    elif nome_so == "posix":
        print("(Linux, macOS, etc.)")


identificar_so_os()

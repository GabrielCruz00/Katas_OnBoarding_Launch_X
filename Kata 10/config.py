def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print('No se encontró el archivo config.txt')
    except PermissionError:
        print('Se encontró config.txt pero es un directorio, no se puede leer')

if __name__ == '__main__':
    main()
def hex_to_bytes(hex_string):
    """
    Converte uma string hexadecimal em uma sequência de bytes.
    """
    # Remove as barras invertidas e espaços da string hexadecimal
    hex_string = hex_string.replace("\\", "").replace(" ", "")
    # Converte a string hexadecimal para bytes
    return bytes.fromhex(hex_string)

def bytes_to_ascii(bytes_data):
    """
    Converte uma sequência de bytes para uma string ASCII legível.
    """
    return ''.join(chr(b) for b in bytes_data if 32 <= b <= 126)  # Somente caracteres ASCII imprimíveis

def main():
    # String hexadecimal fornecida
    hex_string = "4D5A90000300000004000000FFFF00000B"  # Substitua por sua string hexadecimal
    
    # Converter hexadecimal para bytes
    bytes_data = hex_to_bytes(hex_string)
    
    # Mostrar bytes e texto ASCII correspondente
    print("Bytes:", bytes_data)
    print("Texto ASCII:", bytes_to_ascii(bytes_data))

if __name__ == "__main__":
    main()

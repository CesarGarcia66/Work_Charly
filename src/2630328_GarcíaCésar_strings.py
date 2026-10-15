#Manejo de strings en Python
print("Manejo de strings en Python")
print("Nombre:César Enrique García Samano")
print("Matricula: 2630328")
print("Grupo: M1-1")

print("----------------------------------")

#Resumen ejecutivo
#1. ¿Qué es un string en Python?
# Un string (str) es un tipo de dato que permite almacenar texto, como nombres,
# palabras o frases. Se escribe entre comillas simples o dobles. 
#Es inmutable, lo que significa que no se puede modificar directamente su contenido original.

#2. ¿Qué operaciones básicas se pueden realizar?
#Concatenar: unir textos con +. Ejemplo: "Hola" + " mundo".
#Obtener longitud: usar len() para contar los caracteres.
#Extraer subcadenas: usar índices o segmentos para obtener una parte del texto, como "Python"[0:3], que devuelve "Pyt".
# Buscar patrones: usar find() para localizar texto dentro de una cadena.
#Reemplazar texto: usar replace() para cambiar una parte por otra.

#3. ¿Por qué es importante validar y normalizar el texto?
#Es importante para comprobar que los datos sean correctos y tengan un formato uniforme.
#Por ejemplo, validar que un correo tenga un formato adecuado, eliminar espacios 
#innecesarios en nombres y verificar que las contraseñas cumplan ciertos requisitos.
#Esto ayuda a evitar errores y mejora la seguridad de los programas.

print("----------------------------------")

#Problem 1: Full name formatter (name + initials)
print("Problem 1:")

#Description: Create a Python program that formats a full name, removes extra spaces,
#converts it to Title Case, generates initials, and validates the input.

#inputs
full_name = "Cesar garcia enrique samano"

#Code:
full_name = full_name.strip()

words = full_name.split()

formatted_name = words[0].title() + " " + words[2].title() + " " + words[1].title() + " " + words[3].title()

initials = ".".join([word[0].upper() for word in formatted_name.split()]) + "."

#Output
print(f"Formatted name: {formatted_name}")
print(f"Initials: {initials}")

print("----------------------------------")
#Problem 2: Simple email validator (structure + domain)
print("Problem 2:")

#Descrpition:Create a Python program that checks if an email address has a basic valid
#format. It verifies the presence of exactly one '@', a dot after it, and no spaces.
#If the email is valid, the program also displays its domain.

#inputs:
email_text = input("Ingresa un correo:")

#code:
email_text.strip()
email_text.split()

valid_email = (
    len(email_text) > 0
) * (
    email_text.count("@") == 1
) * (
    "." in email_text[email_text.find("@") + 1:]
) * (
    " " not in email_text
)

#outputs
print(f"Valid email: {str(bool(valid_email)).lower()}")

domain_part = email_text[email_text.find("@") + 1:]
print(f"Domain: {domain_part}" * bool(valid_email))
print("----------------------------------")

# Problem 3: Palindrome checker (ignoring spaces and case)
print("Problem 3:")

#Description:Create a Python program that determines whether a phrase is a palindrome 
#by ignoring spaces and uppercase or lowercase letters. 
#The program displays the normalized phrase and whether it is a palindrome.

#inputs:
phrase = input(" insert prhase: ")

#Code:
normalized = "".join(phrase.strip().lower().split())
count_palindrome_true = 0

if len(normalized) >= 3 and normalized == normalized[::-1]:
    count_palindrome_true = 1

#Output
print(f"Normalized phrase: {normalized}")
print(f"Is palindrome: {str(bool(count_palindrome_true)).lower()}")

print("----------------------------------")

#Problem 4: Sentence word stats (lengths and first/last word)
print("problem 4")

#Description: This practice consists of analyzing a sentence to count its words, 
#identify the first and last words, and find the shortest and longest words. 
#It uses Python string methods such as strip(), split(), and len() to process and validate the input.

#input
sentence = input("insert sentence:")

#code
sentence = sentence.strip()
Separate = sentence.split()
n_words = len(Separate)

longest_word = Separate[0]
shortest_word = Separate[0]

for word in Separate:
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(shortest_word):
        shortest_word = word

#outputs:
print(f"Word count: {n_words}")
print(f"First word: {Separate[0]}")
print(f"Last word: {Separate[-1]}")
print(f"Longest word: {longest_word}")
print(f"Shortest word: {shortest_word}")

print("----------------------------------")

#Problem 5: Password strength classifier
print("problem 5")

#Description: This practice consists of evaluating a password and classifying 
#its strength as weak, medium, or strong based on its length and the types of characters
#it contains. It also validates that the password is not empty and uses Python
#string methods to check its characteristics.

#inputs:
password_input = input("Password classifier:")

#code:
Password_count = len(password_input)

has_upper = False
has_lower = False
has_digit = False
has_alnum = False

for caracter in password_input:
    if caracter.isupper():
        has_upper = True
    if caracter.islower():
        has_lower = True
    if caracter.isdigit():
        has_digit = True
    if caracter.isalnum():
        has_alnum = True


if Password_count >= 8 and has_upper and has_lower and has_digit and has_alnum:
    password_input = "strong"
elif Password_count >= 8 and (has_upper or has_lower or has_digit):
    password_input = "medium"
elif Password_count < 8 or has_lower:
    password_input = "weak"

#outputs:
print(password_input)

print("----------------------------------")

#Problem 6: Product label formatter (fixed-width text)
print("problem 6")

#Description: This exercise focuses on string manipulation and input formatting 
#in Python. The goal is to build a standard product label string with a fixed length
#of 30 characters using string slicing, length checks (len()), 
#conditional statements (if/elif/else), and space padding.

# Inputs:
product_name = input("Enter product name: ")
price_value = input("Enter price: ")

# Code:
base = f"Product: {product_name.strip()} | Price: ${price_value}"

if len(base) > 30:
    label = base[:30]
elif len(base) < 30:
    label = base + " " * (30 - len(base))
else:
    label = base

#outputs:
print(f'Label: "{label}"')
print("Length:", len(label))

print("----------------------------------")

#Conclusion:

# 1. El manejo de strings en input y output garantiza una presentación limpia y estructurada.
# 2. Métodos como strip() y lower() limpian espacios y estandarizan entradas.
# 3. Normalizar texto antes de comparar evita errores lógicos por formato.
# 4. Las validaciones evitan fallos de ejecución y el ingreso de datos basura.
# 5. Comprendí que los strings son inmutables y los slices controlan su longitud.

#References:
# 1) Python Software Foundation. Python documentation - Built-in Types:
#    Text Sequence Type — str (documentación oficial traducida al español).
#    https://docs.python.org/es/3/library/stdtypes.html#text-sequence-type-str
#
# 2) Roldán Blay, C. (2021). "Strings en Python" [Video]. Universitat
#    Politècnica de València (UPV).
#    https://riunet.upv.es/handle/10251/167281
#
# 3) Roldán Blay, C. (2021). "Acceso e iteración con strings en Python"
#    [Video]. Universitat Politècnica de València (UPV).
#    https://riunet.upv.es/handle/10251/167347
#
# 4) Platzi. "Métodos de strings en Python: domina el poder de las cadenas
#    de texto" (isalpha, isdigit, strip, replace, etc.).
#    https://platzi.com/blog/metodos-de-strings-en-python-domina-el-poder-de-las-cadenas-de-texto/
#
# 5) LabEx. "Cómo comprobar si una cadena contiene solo letras en Python"
#    (uso de isalpha() para validar la entrada del usuario).
#    https://labex.io/es/tutorials/python-how-to-check-if-a-string-contains-only-letters-in-python-559569






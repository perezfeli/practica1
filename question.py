import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# El usuario deberá contestar 3 preguntas
score = 0 # Se inicializa el score del usuario en 0
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")

        # Se fija si la entrada es un numero, sino sale
        if not user_answer.isdigit():
            print("Respuesta no valida")
            exit(1)

        # Una vez verificado que la respuesta sea numero, lo transforma en entero y le resta 1 para que funcione dentro del vector de respuestas
        user_answer = int(user_answer) - 1

        # Se fija si el numero ingresado esta dentro del rango de respuestas
        if user_answer < 0 or user_answer >= len(answers[question_index]):
            print("Respuesta no valida")
            exit(1)
        
        # Se verifica si la respuesta es correcta
        if user_answer == correct_answers_index[question_index]:
            print("¡Correcto!")
            score += 1 # Suma 1 al score por el acierto
            break
        else:
            print("¡Incorrecto!")
            score += -0.5 # Resta 0.5 por el intento fallido
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])

    # Se imprime un blanco al final de la pregunta
    print()

# Se imprime la puntacion del usuario, sumando 1 por acierto y restando 0.5 por error
print("Tu puntacion fue: ", score)
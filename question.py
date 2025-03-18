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
# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Seleccionar 3 preguntas aleatorias sin repetir
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

# Inicializar puntaje
score = 0

# Iterar sobre cada pregunta seleccionada
for question, answers_options, correct_answers in questions_to_ask:
    print(question)
    for i, answer in enumerate(answers_options):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")

        # Validar que la entrada sea un número
        if not user_answer.isdigit():
            print("Respuesta no válida")
            exit(1)

        # Convertir la respuesta a entero
        user_answer = int(user_answer) - 1

        # Validar que el número ingresado esté dentro del rango de respuestas
        if user_answer < 0 or user_answer >= len(answers_options):
            print("Respuesta no válida")
            exit(1)

        # Verificar si la respuesta es correcta
        if user_answer == correct_answers:
            print("¡Correcto!")
            score += 1  # Suma 1 al puntaje por acierto
            break
        else:
            print("¡Incorrecto!")
            score -= 0.5  # Resta 0.5 por intento fallido
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print(f"Incorrecto. La respuesta correcta era: {answers_options[correct_answers]}")

    # Línea en blanco para separación
    print()

# Mostrar puntaje final
print("Tu puntuación fue:", score)
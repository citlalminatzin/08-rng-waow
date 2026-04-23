import random


def create_game() -> int:
    """Escoge la puerta ganadora"""
    boxes = [i for i in range(3)]
    return random.choice(boxes)


def play_change(n: int = 1000) -> float:
    """
    Juega monty-hall con la estrategia de cambiar la puerta
    Regresa la tasa de éxito
    """
    wins = 0.0
    boxes = [i for i in range(3)]

    for _ in range(n):
        # Crea un juego con una caja ganadora y escoge.
        result = create_game()
        choice = random.choice(boxes)

        # Como no podemos abrir la ganadora ni la que escogimos, elige una de las restantes.
        left = [i for i in range(3) if i != choice and i != result]
        open = random.choice(left)

        # Como cambiamos, nuestra eleccion final no puede ser ni la que elegimos ni la abierta.
        final = [i for i in range(3) if i != open and i != choice][0]

        if final == result:
            wins += 1

    return wins / n


def play_stay(n: int = 1000) -> float:
    """Juega monty-hall con la estrategia de NO cambiar la puerta"""
    wins = 0.0
    boxes = [i for i in range(3)]

    for _ in range(n):
        result = create_game()
        choice = random.choice(boxes)

        # Al quedarnos, la unica manera de ganar es cuando el resultado es igual a la eleccion.
        if result == choice:
            wins += 1

    return wins / n


def main():
    success_change = play_change()
    success_stay = play_stay()
    print(f"{success_change=} {success_stay=}")


main()

if "__name__" == "__main__":
    main()

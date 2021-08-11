"""
# Harry Potter Quiz

Example of an over-engineered quiz program. Questions and answers were found
on discord of unknown origin. I know little about harry potter myself.
"""
from typing import Union, Callable

houses_count = {
    'gryffindor': 0,
    'hufflepuff': 0,
    'ravenclaw': 0,
    'slytherin': 0,
}

questions = [
    (
        "When I'm dead, I want people to remember me as:",
        (('hufflepuff',), "The Good"),
        (('slytherin',), "The Great"),
        (('ravenclaw',), "The Wise"),
        (('gryffindor',), "The Bold"),
    ),
    (
        "Dawn or Dusk?",
        (('gryffindor', 'ravenclaw'), "Dawn"),
        (('hufflepuff', 'slytherin'), "Dusk"),
    ),
    (
        "Which kind of instrument most pleases your ear?",
        (('slytherin',), "The violin"),
        (('hufflepuff',), "The trumpet"),
        (('ravenclaw',), "The piano"),
        (('gryffindor',), "The drum"),
    ),
    (
        "Which road tempts you the most?",
        (('hufflepuff',), "The wide, sunny grassy lane"),
        (('slytherin',), "The narrow, dark, lantern-lit alley"),
        (('gryffindor',), "The twisting, leaf-strewn path through woods"),
        (('ravenclaw',), "The cobbled street lined (ancient buildings)"),
    ),
]


def int_input_range(start: Union[int, float] = 0,
                    stop: Union[int, float] = float('inf'),
                    prompt: str = '> ') -> int:
    while True:
        try:
            response = int(input(prompt))
        except ValueError:
            print('Not a number!')
        else:
            if start <= response < stop:
                break
            else:
                print('Not a valid input!')
    return response


def silent_exit(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except (KeyboardInterrupt, EOFError):
            print()
            quit()
        else:
            return result
    return wrapper


@silent_exit
def main() -> None:
    print('Harry Potter Quiz!')
    for num_question, (question, *possible_answers) in enumerate(questions):
        print(f'({num_question+1}/{len(questions)})', question)
        
        for num_answer, (_, possible_answer) in enumerate(possible_answers):
            print(f"{num_answer+1}:", possible_answer)

        prompt = f"Answer, (1-{len(possible_answers)}): "
        user_response = int_input_range(1, len(possible_answers)+1, prompt=prompt)

        user_answers = possible_answers[user_response - 1][0]
        for user_answer in user_answers:
            houses_count[user_answer] += 1

    user_houses = [house.title()
                   for house, count in houses_count.items()
                   if count == max(houses_count.values())]

    if len(user_houses) > 1:
        print('You fit equally into', ' and '.join(user_houses))
    else:
        print('You fit into the house of', user_houses[0])


if __name__ == '__main__':
    main()

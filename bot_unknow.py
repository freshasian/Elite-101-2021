import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def undefined():
    response = ["Could you please re-phrase that? ",
                "i not sure what you mean",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
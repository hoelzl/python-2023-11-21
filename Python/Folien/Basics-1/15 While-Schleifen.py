# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# <div style="text-align:center; font-size:200%;">
#  <b>While-Schleifen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 15 While-Schleifen.py -->
# <!-- python_courses/slides/module_140_control_flow/topic_210_a3_while_part2.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  # While-Schleifen
#
#  Manchmal wollen wir einen Teil eines Programms immer wieder ausführen:
#
#  - Zahlenraten bis die richtige Zahl gefunden wurde
#  - Physik-Simulation bis das Ergebnis genau genug ist
#  - Verarbeitung von Benutzereingaben in interaktiven Programmen
#
#  Wenn wir die Anzahl der Wiederholungen nicht von vornherein wissen,
#  verwenden wir dafür in der Regel eine While-Schleife.

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
def rocket_launch(countdown):
    print("Welcome to the Rocket Launch Countdown Simulator!")

    # Set the countdown timer in seconds
    countdown = 10

    while countdown > 0:
        print(f"Rocket launches in {countdown} seconds...")
        countdown -= 1  # This decrements the countdown by 1 each time the loop runs

    # When the countdown hits 0, we want to simulate the rocket launch
    print("Liftoff! 🚀")

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
rocket_launch(10)


# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  ## Beenden von Schleifen
#
# Manchmal ist es leichter, die Abbruchbedingung einer Schleife im Rumpf zu
# bestimmen, statt am Anfang. Mit der Anweisung `break` kann man eine
# Schleife vorzeitig beenden:

# %% lang="de"
i = 1
while i < 10:
    print(i)
    if i % 3 == 0:
        break
    i += 1
print("Nach der Schleife:", i)


# %%
def annoy_user():
    while True:
        text = input("Say hi! ")
        if text.lower() == "hi":
            break
        else:
            print("You chose", text)


# %%
# annoy_user()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Zahlenraten
#
# - Schreiben Sie ein Programm, das eine Zufallszahl zwischen 1 und 100 erzeugt
# und den Benutzer solange raten lässt, bis er die Zahl erraten hat.
# - Nach jedem Versuch soll dem Benutzer angezeigt werden, ob die geratene Zahl
# zu groß oder zu klein war.

# %%
import random

def guess_number():
    solution = random.randint(1, 100)
    geratene_zahl = input("Bitte geben Sie eine Zahl zwischen 1 und 100 ein: ")
    while int(geratene_zahl) != solution:
        if int(geratene_zahl) < solution:
            print(f"{geratene_zahl} ist zu klein.")
        else:
            print(f"{geratene_zahl} ist zu groß.")
        geratene_zahl = input("Bitte versuchen Sie es noch einmal: ")
    print("Sie haben gewonnen!")


# %%
guess_number()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Fügen Sie Ihrem Programm eine Begrenzung der Rate-Versuche hinzu.   
#   Wenn der Benutzer die Zahl in weniger als 6 Versuchen errät, soll die Meldung
#   `Gut geraten!` ausgegeben werden, ansonsten `Schlecht geraten!`.
# - Erweitern Sie das Programm, sodass nach dem Ende des Spiels die Anzahl der
#   benötigten Versuche ausgegeben wird.

# %%
import random

def guess_number():
    tries = 6
    solution = random.randint(1, 100)

    print("Willkommen zu dem Zahlenratespiel!")
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Du hast 6 Versuche, um sie zu erraten.")

    while tries > 0:
        guess = int(input("Bitte Zahl eingeben: "))

        if guess < solution:
            print("Zu niedrig!")
        elif guess > solution:
            print("Zu hoch!")
        else:  # If the guess is not too low or too high, it must be just right
            print("Herzlichen Glückwunsch! Du hast die Zahl erraten!")
            break  # End the loop

        tries -= 1  # Subtract one from tries

    # If the player ran out of tries and didn't guess correctly
    if tries == 0 and guess != solution:
        print("Leider hast du die Zahl nicht erraten. Die Zahl war.", solution)
        print("Du hast", tries, "Versuche übrig gelassen.")

# %% lang="de"
guess_number()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Erweitern Sie das Programm, sodass der Benutzer entscheiden kann, ob er
#   erneut spielen möchte.

# %%
import random

def guess_number():
    solution = random.randint(1, 100)

    print("Willkommen zu dem Zahlenratespiel!")
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Du hast 6 Versuche, um sie zu erraten.")

    while True:
        tries = 6
        while tries > 0:
            guess = int(input("Bitte Zahl eingeben: "))

            if guess < solution:
                print("Zu niedrig!")
            elif guess > solution:
                print("Zu hoch!")
            else:  # If the guess is not too low or too high, it must be just right
                print("Herzlichen Glückwunsch! Du hast die Zahl erraten!")
                break  # End the loop

            tries -= 1  # Subtract one from tries

        # If the player ran out of tries and didn't guess correctly
        if tries == 0 and guess != solution:
            print("Leider hast du die Zahl nicht erraten. Die Zahl war.", solution)
            print("Du hast", tries, "Versuche übrig gelassen.")

        again = input("Möchtest du nochmal spielen? (j/n) ")
        if again != "j":
            break

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Run an experiment
#
# - Schreiben Sie ein Programm, das ein Experiment ausführt
# - Das Experiment besteht darin, eine Zufallszahl zu erzeugen und zu prüfen,
#   ob diese größer als 0.8 ist.
# - Wenn das Experiment erfolgreich war, soll `Erfolg!` ausgegeben werden,
#   andernfalls `Fehlschlag.`.
# - Führen Sie das Experiment solange aus, bis es erfolgreich war.
# - Geben Sie die Anzahl der benötigten Versuche aus.
#

# %% lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
from random import random

# %%
def führe_ein_experiment_aus(versuch_nr):
    """Führt ein Experiment aus
    Gibt True zurück wenn das Experiment erfolgreich war, andernfalls False.
    """
    print("Versuch Nr.", versuch_nr,   "gestartet...", end="")
    
    if random() > 0.8:
        print("Erfolg!")
        return True
    else:
        print("Fehlschlag.")
        return False

# %%
versuch_nr = 0

while not führe_ein_experiment_aus(versuch_nr):
    versuch_nr += 1

print("Wir haben einen erfolgreichen Versuch ausgeführt.")
# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Wörterspiel
#
# - Schreiben Sie ein Programm, das ein zufälliges Wort aus einer Liste von Wörtern erzeugt
# - und den Benutzer raten lässt, bis er das Wort erraten hat.


# %% lang="de"
import random

# %%
def guess_word():
    wörter = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]    
    lösung = random.choice(wörter)
    geratenes_wort = input("Bitte geben Sie ein Wort ein: ")
    while geratenes_wort != lösung:
        geratenes_wort = input("Bitte versuchen Sie es noch einmal: ")
    print("Sie haben gewonnen!")


# %%
guess_word()

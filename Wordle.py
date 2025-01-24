import random

def wordle():
    word = random.choice(["fable", "thump", "hazel", "flute", "flair", "gulch", "hurry", "gloom", "glaze", "thick", "grief", "tulip", "blush", "squad", "hatch", "swoop", "thief", "spoon", "homer", "grind", "grant", "gully", "shank", "joint", "bully", "froth", "shank", "homer", "clasp", "bloom", "twist", "hiker", "spicy", "jolly", "gulch", "spicy", "brine", "grief", "crush", "bunch", "hurry", "fable", "gulch", "crush", "shank", "spout", "shank", "gully", "spoon","tulip", "panda", "swarm", "balmz", "dulse", "wench", "munch", "trite", "bract", "rater", "hunch", "spout", "sonar", "hater", "frets", "grate", "swoon", "jolly", "bower", "rutty", "clank", "twine", "gully", "janty", "roost", "clank", "fleet", "tonne", "holly", "bloom", "slump", "quash", "hiker", "clump", "steep", "havoc", "hazy", "holly", "haunt", "leggy", "hovel", "hunch", "grime", "guilty", "spurt", "spank", "quilt", "hasty"])
    display = ['_' for i in word]
    tries = 6
    while tries > 0:
        print("Current word: ", " ".join(display))
        print("Tries left: ", tries)
        guess = input("Enter your guess: ")
        if len(guess) != 5:
            print("Wrong word length, try again.")
        else:
            if guess == word:
                 print("Congratulations, you won!")
                 break
            for i in range(len(word)):
                if guess[i] == word[i]:
                     display[i] = guess[i]
                     print("\033[1;32;40m",guess[i],"\033[0m", end=" ")
                elif guess[i] in word:
                    display[i] = "_"
                    print("\033[1;33;40m",guess[i],"\033[0m", end=" ")
                else:
                    display[i] = guess[i]
                    print(guess[i], end=" ")
            print("\nWrong word, try again.\n")
            tries -= 1
    if tries == 0:
        print("Game over, the word was ", word)

if __name__ == '__main__':
    print("Welcome to Wordle! You have 6 tries to guess a 5 letter word.")
    wordle()

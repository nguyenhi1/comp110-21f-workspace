"""Esacape the Frat House."""

__author__ = "730402537"

from random import randint
import time
# points
points = 0


a = 3.0
b = 1
c = 0.7

# player stats
player_health = 100
chad_health = 100
ankle = 1
regen = 0


# Pong
CUP: str = '\U0001F964'
SHOT: str = '\U00002716'
    

def main() -> None:
    """Begin escape."""
    greet()


def name(user: str) -> str:
    """Establish player name as global variable."""
    global player
    player = input("Enter your name: ")
    print("Welcome", (player), "good luck.")
    return user


def health_check() -> None:
    """Checks if player health is depleted."""
    global player_health
    if player_health < 1:
        print("You have run out of HP! You pass out.")
        time.sleep(b)
        ("Final points: ", (points))
        x = points
        win_lose(x)
        greet()


def heal(x: int) -> None:
    """Heals player with liquid IV."""
    global player_health
    global regen
    print("You down the liquid IV like it's a shot. You gained 30HP!")
    time.sleep(b)
    player_health = player_health + x
    regen = regen - 1


# combat functions
def player_jab() -> None:
    """Player jab attack."""
    global chad_health
    global player_health
    global points
    player_jab = randint(12, 14)
    print("You jabbed Chad!")
    time.sleep(c)
    print("Your attack did", (player_jab), "HP damage!")
    time.sleep(c)
    chad_health = chad_health - player_jab
    print("Chad's health:", (chad_health))
    points = points + 100
    if ankle == 0:
        player_health = player_health - 5
        print("Due to your sprained ankle, you lost 5HP this turn")
        time.sleep(c)
        print("Your health:", player_health)
        time.sleep(c)
    if regen == 1:
        x: int = randint(30, 60)
        healing: str = input("You remembered you have a liquid IV! Would you like to use it to restore some health? ")
        if healing == "yes" or healing == "Yes":
            heal(x)


def enemy_smack() -> None:
    """Enemy smack attack."""
    global player_health
    global regen
    enemy_smack = randint(12, 16)
    print("Chad swings at you!")
    time.sleep(c)
    if enemy_smack == 14:
        print("He missed!")
        time.sleep(b)
        print("Chad did no damage to you.")
        time.sleep(b)
        print("Your HP:", (player_health))
        if regen == 1:
            x: int = randint(30, 60)
            healing: str = input("You remembered you have a liquid IV! Would you like to use it to restore some health? ")
            if healing == "yes" or healing == "Yes":
                heal(x)
    else:
        print("Chad smacks you!")
        time.sleep(c)
        print("His attack did", (enemy_smack), "HP damage to you.")
        time.sleep(b)
        player_health = player_health - enemy_smack
        print("Your HP:", (player_health))
        if regen == 1:
            x = randint(30, 60)
            healing = input("You remembered you have a liquid IV! Would you like to use it to restore some health? ")
            if healing == "yes" or healing == "Yes":
                heal(x)
    if ankle == 0:
        player_health = player_health - 5
        print("Due to your sprained ankle, you lost 5HP this turn")
        time.sleep(c)
        print("Your health:", player_health)


def player_sweep() -> None:
    """Player sweep attack."""
    global chad_health
    global player_health
    global points
    print("You sweep your cushion at Chad's legs!")
    time.sleep(c)
    player_sweep = randint(15, 20)
    points = points + 100
    if player_sweep == 17:
        print("You missed. Must be the beer goggles.")
        time.sleep(c)
        print("You did no damage to Chad.")
        time.sleep(c)
        points = points - 100
        if regen == 1:
            x: int = randint(30, 60)
            healing: str = input("You remembered you have a liquid IV! Would you like to use it to restore some health? ")
            if healing == "yes" or healing == "Yes":
                heal(x)
    else:
        chad_health = chad_health - player_sweep
        print("You swept Chad's legs!")
        time.sleep(a)
        print("Your attack did", (player_sweep), "HP damage!")
        print("Chad's health:", (chad_health))
    if ankle == 0:
        player_health = player_health - 5
        print("Due to your sprained ankle, you lost 5HP this turn")
        time.sleep(c)
        print("Your health:", player_health)


# Escape begins ## DO TIME SLEEP FUNCTION ON THIS TEXT
def greet() -> None:
    """Making first decision in escape."""
    print("You have woken up in a strange room.")
    time.sleep(a)
    print("There are red solo cups lining every possible flat surface in the room and dirty clothes covering every little spot on the bed--probably \
why you woke up on the floor.")
    time.sleep(a)
    print("Red neon lights line the corners of the room's ceiling.")
    time.sleep(a)
    print("There is a putrid smell in the room that you inhale with every breath you take.")
    time.sleep(a) 
    print("With that, you conclude that you have managed to trap yourself in a frat house.")
    time.sleep(a)
    print("To your left, there is a door that leads to another room.") 
    time.sleep(a)
    print("Coming from that same room, you hear a guy yell 'Elbows! Elbows!'")
    time.sleep(a)
    print("To your right, you see a door that leads to a set of stairs leading down.")
    time.sleep(a)
    name()
    print("")
    print("You look down at your right forearm and see writing from a marker.")
    time.sleep(a)
    print(f'It says: My name is, {player.upper()} please return me back to Hojo if lost.')
    time.sleep(a)
    print("Must have been a message left by your friend that you came with. How sweet.")
    time.sleep(a)
    first_choice: str = input("Which way do you choose to go? Do you go left, right, or stay? ")
    print("")

    if first_choice == "left" or first_choice == "Left":
        left()

    if first_choice == "right" or first_choice == "Right":
        right()

    if first_choice == "stay" or first_choice == "Stay":
        sleep()


def left() -> None:
    """Path after taking left."""
    print("You choose to walk through the door on your left toward the shouting male voices.")
    time.sleep(a)
    print("You walk into the room in the middle of a pong game.")
    time.sleep(a)
    print("On the table, there are three cups in the shape of a triangle on one side; on the other, there are two cups in a line.") 
    time.sleep(a)
    print("Accidentally, you make eye contact with a guy wearing khaki shorts, a blue polo shirt, Sperry's, and a backwards hat.")
    time.sleep(a)
    print("You assume his name is Chad. He is standing on the side of the table with three cups.")
    time.sleep(a)
    print("He yells to you 'celebrity shot!' It's too late for you to run now.")
    time.sleep(a)
    print("He urges you to the end of the table and pushes a ping pong ball into your hand. Looks like you have to play; don't want to dissapoint Chad.")
    time.sleep(a)
    print("You look to the other side of the table and see these cups:")
    time.sleep(a)
    print("", CUP, '\n', CUP)
    print("")
    time.sleep(a)
    print("You throw the ball.")
    shot = randint(1, 3)
    global points
    if shot == 1:
        points = points + 100
        print("", SHOT, "\n", CUP)
        time.sleep(b)
        second_shot: str = input("You make the first shot with ease. Would you like to take the second shot? ")
        while True:
            if second_shot == "yes" or second_shot == "Yes" or second_shot == "no" or second_shot == "No":
                if second_shot == "yes" or second_shot == "Yes":
                    shot = randint(1, 2)
                    if shot == 1:
                        print("", SHOT, "\n", SHOT)
                        time.sleep(b)
                        print("Woah two in a row?! Safe to say you're carrying the team.")
                        points = points + 200
                        print("After the game, Chad taps on your shoulder and says 'Hey, could you follow me for a bit?'")
                        time.sleep(a)
                        print("You find it a little suspicious...")
                        time.sleep(a)
                        print("On the other hand, you still need to find your phone, which you are sure you left in the basement.")
                        time.sleep(a)
                        after_pong: str = input("Would you like to follow Chad or go to the basement? Answer Chad or Basement: ")
                        while True:
                            if after_pong == "Chad" or after_pong == "chad":
                                liquidIV()
                            if after_pong == "basement" or after_pong == "Basement":
                                right()
                            else:
                                print("That is not an option. Please choose Chad or Basement.")
                                time.sleep(b)
                                after_pong = input("Would you like to follow Chad or go to the basement? ")
                    else:
                        global player_health
                        print("", SHOT, "\n", CUP)
                        time.sleep(b)
                        print("You missed... might've gotten a little too cocky there.")
                        time.sleep(b)
                        player_health = player_health - 10
                        print("That miss bruised your ego. You lost 10HP")
                        time.sleep(b)
                        print("Your current health:", (player_health))
                        time.sleep(a)
                        print("After the game, Chad taps on your shoulder and says 'Hey, could you follow me for a bit?'") 
                        time.sleep(a)
                        print("You find it a little suspicious...")
                        time.sleep(a)
                        print("On the other hand, you still need to find your phone, which you are sure you left in the basement.")
                        time.sleep(a)
                        after_pong = input("Would you like to follow Chad or go to the basement? Answer Chad or Basement: S")
                        while True:
                            if after_pong == "Chad" or after_pong == "chad":
                                liquidIV()
                            if after_pong == "basement" or after_pong == "Basement":
                                right()
                            else:
                                print("That is not an option. Please choose Chad or Basement.")
                                time.sleep(b)
                                after_pong = input("Would you like to follow Chad or go to the basement? ")
                else:
                    if second_shot == "no" or second_shot == "No":
                        print("You choose to leave it at that and not risk missing the second shot.")
                        time.sleep(a)
                        print("After the game, Chad taps on your shoulder and says 'Hey, could you follow me for a bit?'")
                        time.sleep(a)
                        print("You find it a little suspicious...")
                        time.sleep(a)
                        print("On the other hand, you still need to find your phone, which you are sure you left in the basement.")
                        time.sleep(a)
                        after_pong = input("Would you like to follow Chad or go to the basement? Answer Chad or Basement: ")
                        while True:
                            if after_pong == "Chad" or after_pong == "chad":
                                liquidIV()
                            if after_pong == "basement" or after_pong == "Basement":
                                right()
                            else:
                                print("That is not an option. Please choose Chad or Basement.")
                                time.sleep(b)
                                after_pong = input("Would you like to follow Chad or go to the basement? ")
            else:
                print("That is not an option. Choose yes or no.")
                time.sleep(b)
                second_shot = input("Would you like to take the second shot? ")

    else:
        if shot == 2:
            points = points + 100
            print("", CUP, "\n", SHOT)
            time.sleep(b)
            second_shot = input("You made the first shot with ease. Would you like to take the second shot? ")
            while True:
                if second_shot == "yes" or second_shot == "Yes" or second_shot == "no" or second_shot == "No":
                    if second_shot == "yes" or second_shot == "Yes":
                        shot = randint(1, 2)
                        if shot == 1:
                            points = points + 100
                            print("", SHOT, "\n", SHOT)
                            time.sleep(b)
                            print("You made the shot! Safe to say you're carrying the team.")
                            time.sleep(a)
                            print("After the game, Chad taps on your shoulder and says 'Hey, could you follow me for a bit?'")
                            time.sleep(a)
                            print("You find it a little suspicious...")
                            time.sleep(a)
                            print("On the other hand, you still need to find your phone, which you are sure you left in the basement.")
                            time.sleep(a)
                            after_pong = input("Would you like to follow Chad or go to the basement? Answer Chad or Basement: ")
                            while True:
                                if after_pong == "Chad" or after_pong == "chad":
                                    liquidIV()
                                if after_pong == "basement" or after_pong == "Basement":
                                    right()
                                else:
                                    print("That is not an option. Please choose Chad or Basement.")
                                    time.sleep(a)
                                    after_pong = input("Would you like to follow Chad or go to the basement? ")
                        else:
                            print("", CUP, "\n", SHOT)
                            time.sleep(b)
                            print("You missed... might've gotten a little too cocky there.")
                            time.sleep(a)
                            player_health = player_health - 10
                            print("That miss bruised your ego. You lost 10HP.")
                            time.sleep(b)
                            print("Your current health:", (player_health))
                            print("After the game, Chad taps on your shoulder and says 'Hey, could you follow me for a bit?'")
                            time.sleep(a)
                            print("You find it a little suspicious...")
                            time.sleep(a)
                            print("On the other hand, you still need to find your phone, which you are sure you left in the basement.")
                            time.sleep(a)
                            after_pong = input("Would you like to follow Chad or go to the basement? Answer Chad or Basement: ")
                            while True:
                                if after_pong == "Chad" or after_pong == "chad":
                                    liquidIV()
                                if after_pong == "basement" or after_pong == "Basement":
                                    right()
                                else:
                                    print("That is not an option. Please choose Chad or Basement.")
                                    time.sleep(a)
                                    after_pong = input("Would you like to follow Chad or go to the basement? ")
                    else:
                        if second_shot == "no" or second_shot == "No":
                            print("You choose to leave it at that and not risk missing the second shot.")
                            time.sleep(a)
                            print("After the game, Chad taps on your shoulder and says 'Hey, could you follow me for a bit?'")
                            time.sleep(a)
                            print("You find it a little suspicious...")
                            time.sleep(a)
                            print("On the other hand, you still need to find your phone, which you are sure you left in the basement.")
                            time.sleep(a)
                            after_pong = input("Would you like to follow Chad or go to the basement? Answer Chad or Basement: ")
                            while True:
                                if after_pong == "Chad" or after_pong == "chad":
                                    liquidIV()
                                if after_pong == "basement" or after_pong == "Basement":
                                    right()
                                else:
                                    print("That is not an option. Please choose Chad or Basement.")
                                    time.sleep(a)
                                    after_pong = input("Would you like to follow Chad or go to the basement? ")
                else:
                    print("That is not an option. Choose yes or no.")
                    time.sleep(a)
                    second_shot = input("Would you like to take the second shot? ")

        else:
            print("", CUP, "\n", CUP)
            time.sleep(b)
            print("Wow... first shot and you missed.")
            time.sleep(a)
            player_health = player_health - 10
            print("Your ego has been bruised. You lost 10HP.")
            time.sleep(b)
            print("Your current health:", (player_health))
            time.sleep(b)
            second_shot = input("Would you like to redeem yourself and take the second shot? ")
            while True:
                if second_shot == "yes" or second_shot == "Yes" or second_shot == "no" or second_shot == "No":
                    if second_shot == "yes" or second_shot == "Yes":
                        shot = randint(1, 3)
                        if shot == 1:
                            points = points + 100
                            print("", SHOT, "\n", CUP)
                            time.sleep(b)
                            print("You made the shot! Good job redeeming yourself.")
                            time.sleep(a)
                            print("After the game, Chad taps on your shoulder and says 'Hey, could you follow me for a bit?'")
                            time.sleep(a)
                            print("You find it a little suspicious...")
                            time.sleep(a)
                            print("On the other hand, you still need to find your phone, which you are sure you left in the basement.")
                            time.sleep(a)
                            after_pong = input("Would you like to follow Chad or go to the basement? Answer Chad or Basement: ")
                            while True:
                                if after_pong == "Chad" or after_pong == "chad":
                                    liquidIV()
                                if after_pong == "basement" or after_pong == "Basement":
                                    right()
                                else:
                                    print("That is not an option. Please choose Chad or Basement.")
                                    time.sleep(a)
                                    after_pong = input("Would you like to follow Chad or go to the basement? ")
                            break
                        else:
                            if shot == 2:
                                points = points + 100
                                print("", CUP, "\n", SHOT)
                                time.sleep(b)
                                print("You made the shot! Good job redeeming yourself")
                                time.sleep(a)
                                print("After the game, Chad taps on your shoulder and says 'Hey, could you follow me for a bit?'")
                                time.sleep(a)
                                print("You find it a little suspicious...")
                                time.sleep(a)
                                print("On the other hand, you still need to find your phone, which you are sure you left in the basement.")
                                time.sleep(a)
                                after_pong = input("Would you like to follow Chad or go to the basement? Answer Chad or Basement: ")
                                while True:
                                    if after_pong == "Chad" or after_pong == "chad":
                                        liquidIV()
                                    if after_pong == "basement" or after_pong == "Basement":
                                        right()
                                    else:
                                        print("That is not an option. Please choose Chad or Basement.")
                                        time.sleep(a)
                                        after_pong = input("Would you like to follow Chad or go to the basement? ")
                            else:
                                print("", CUP, "\n", CUP)
                                time.sleep(b)
                                print("Woah...you missed both shots in a row. That's embarrassing...")
                                time.sleep(b)
                                player_health = player_health - 15
                                print("Those misses majorly bruised your ego. You lost an additional 15HP.")
                                time.sleep(b)
                                print("Your current health:", (player_health))
                                time.sleep(a)
                                print("After the game, Chad taps on your shoulder and says 'Hey, could you follow me for a bit?'")
                                time.sleep(a)
                                print("You find it a little suspicious...")
                                time.sleep(a)
                                print("On the other hand, you still need to find your phone, which you are sure you left in the basement.")
                                time.sleep(a)
                                after_pong = input("Would you like to follow Chad or go to the basement? Answer Chad or Basement: ")
                                while True:
                                    if after_pong == "Chad" or after_pong == "chad":
                                        liquidIV()
                                    if after_pong == "basement" or after_pong == "Basement":
                                        right()
                                    else:
                                        print("That is not an option. Please choose Chad or Basement.")
                                        time.sleep(a)
                                        after_pong = input("Would you like to follow Chad or go to the basement? ")
                    else:
                        if second_shot == "no" or second_shot == "No":
                            print("Guess that's for the best. Just imagine how embarrasing it would be if you missed again.")
                            print("After the game, Chad taps on your shoulder and says 'Hey, could you follow me for a bit?'")
                            time.sleep(a)
                            print("You find it a little suspicious...")
                            time.sleep(a)
                            print("On the other hand, you still need to find your phone, which you are sure you left in the basement.")
                            time.sleep(a)
                            after_pong = input("Would you like to follow Chad or go to the basement? Answer Chad or Basement: ")
                            while True:
                                if after_pong == "Chad" or after_pong == "chad":
                                    liquidIV()
                                if after_pong == "basement" or after_pong == "Basement":
                                    right()
                                else:
                                    print("That is not an option. Please choose Chad or Basement.")
                                    time.sleep(a)
                                    after_pong = input("Would you like to follow Chad or go to the basement? ")
                            break
                else:
                    print("That is not an option. Choose yes or no.")
                    time.sleep(a)
                    second_shot = input("Would you like to take the second shot? ")


# right door - lost phone   
def right() -> None:
    """Path through the right door."""
    print("You go down the stairs.")
    time.sleep(b)
    print("Once you reach the bottom of the stairs, you look around and see that it's completely pitch black.")
    time.sleep(a)
    print("You reach for your phone to use its flashilight, but it's not in your pocket.")
    time.sleep(a)
    print("Trying to remember where you put it, you realize that this is the place where you last had it.")
    time.sleep(a)
    phone: str = input("Would you like to continue searching for it in the dark or give up and look for it when you're sober? Search or give up: ")
    print("")
    global ankle
    while True:
        if phone == "search" or phone == "Search":
            anagram()
            break
        if phone == "give up" or "Give up":
            print("You begin to wander in the dark and put your hands on the wall for guidance.")
            time.sleep(a)
            print("You take a few steps until something large and dense trips you.")
            time.sleep(a)
            print("On the fall down, you manage to twist and sprain your ankle.")
            time.sleep(a)
            print("Now, with every step you take, there is a throbbing pain in your ankle.")
            time.sleep(a)
            ankle = ankle - 1
            print("You limp towards a tiny window that is shining a small amount of light into the room.")
            time.sleep(a)
            print("You manage to drag yourself through the window.")
            print("")
            fight()
        else:
            print("That is not an option. Please choose 'search' or 'give up'")
            time.sleep(a)
            phone = input("Would you like to search or give up?")


# password game ## DO TIME SLEEP FUNCTION ON THIS TEXT
def anagram() -> None:
    """Anagram Puzzle."""
    print("You choose to search for your phone, because it had some good insta worthy pictures on it that were taken before you came to the frat.")
    time.sleep(a)
    print("You blindly walk foward and manage to find a wall.")
    time.sleep(a)
    print("You turn the corner and see a small light.")
    time.sleep(a)
    print("It's your phone!")
    time.sleep(a)
    print("There's a bunch of missed calls from friends.")
    time.sleep(a)
    print("You have to open your phone in order to call them back, but...crap. What's your password again?") 
    time.sleep(a)
    print("You turn on your phone and it looks like you need to solve some sort of anagram to get your password. These are the letters you see: ")
    time.sleep(a)
    print("")
    print("aspwdrso")
    print("")
    attempt: int = 1
    total_attempts: int = 3
    global ankle
    global points
    while attempt < 4:
        print("You have", (total_attempts), "attempts left.")
        time.sleep(b)
        guess: str = input("What is your guess? ")
        if guess == "password":
            points = points + 150
            print("Nice! You got into your phone.")
            time.sleep(a)
            print("Good thing you made it an easy password for situations like this.")
            time.sleep(a)
            print("You try to call your friend, but there's no reception in the basement.")
            time.sleep(a)
            print("On the brightside, at least you have your flashlight now so you can see.")
            time.sleep(a)
            print("You navigate your way through the basement with it and find a small window you can squeeze through to the outside.")
            time.sleep(a)
            print("You climb through and find yourself in the front yard.")
            time.sleep(a)
            fight()
        else:
            print("Whoops, looks like you got it wrong.")
            print("")
            attempt = attempt + 1
            total_attempts = total_attempts - 1
            if attempt == 4 or total_attempts == 0:
                print("You ran out of attempts!")
                time.sleep(a)
                print("You begin to question whether this is really your phone or not, but are quickly reminded that it is because your face is the \
background.")
                time.sleep(a)
                print("Just a lil self love.")
                time.sleep(a)
                print("You begin to wander in the dark and put your hands on the wall for guidance.")
                time.sleep(a)
                print("You take a few steps until something large and dense trips you.")
                time.sleep(a)
                print("On the fall down, you manage to twist and sprain your ankle.")
                time.sleep(a)
                print("Now, with every step you take, there is a throbbing pain in your ankle.")
                time.sleep(a)
                print("You limp towards a tiny window that is shining a small amount of light into the room.")
                time.sleep(a)
                print("You manage to drag yourself through the window.")
                print("")
                fight()
                ankle = ankle - 1


# Go with Chad
def liquidIV() -> None:
    """Obtaining a potion."""
    print("You decide to follow Chad.")
    time.sleep(a)
    print("He leads you outside and hands you something.")
    time.sleep(a)
    print("It's a liquid IV!")
    time.sleep(a)
    print("They taste absolutely disgusting, but it'll help with the hangover tomorrow.")
    time.sleep(a)
    print("You put it in your pocket")
    global points
    global regen
    points = points + 50
    regen = regen + 1
    fight()


def fight() -> None:
    """The final boss battle."""
    print("In front of you, there is a bouncy house that is towering over you.")
    time.sleep(a)
    print("You look into the bouncy house and it seems they have a game of king of the hill set up.")
    time.sleep(a)
    print("In each game, there are two players that fight against each other with large cylindrical cushions.")
    time.sleep(a)
    print("A guy comes up to you and drops one of those cushions into your hands.")
    time.sleep(a)
    print("He says to you:")
    time.sleep(b)
    print("'We need one more person to go against the king. You look drunk and easy to beat.'")
    time.sleep(a)
    global points
    while True:
        health_check()
        if chad_health < 1:
            print("You have defeated Chad, King of the Hill. Congratulations!")
            time.sleep(b)
            points = points + 500
            print("Final points: ", (points))
            x = points
            win_lose(x)
            time.sleep(b)
            play_again: str = input("Would you like to play again? ")
            while True:
                if play_again == "yes" or play_again == "Yes":
                    greet()
                    break
                if play_again == "no" or play_again == "No":
                    break
        else:
            while True:
                attack: str = input("What attack would you like to use? Jab or Sweep: ")
                if attack == "jab" or attack == "Jab":
                    player_jab()
                    break
                if attack == "sweep" or attack == "Sweep":
                    player_sweep()
                    break
                else:
                    print("That is not an option. Choose Jab or Sweep")
                    time.sleep(b)
                    attack = input("Would you like to jab or sweep Chad?")
        print("")
        enemy_smack()


# Sleep
def sleep() -> None:
    """Choose not to continue story."""
    global points
    sleep: str = input("On second thought, you're actually feeling kind of sleepy. Would you like to sleep on the floor or the bed? ")
    print("")
    while True:
        if sleep == "floor" or sleep == "Floor":
            print("You lay back down on the one clean spot on the floor you woke up from and drift off to sleep.")
            time.sleep(a)
            print("Hopefully someone finds the message on your arm soon.")
            time.sleep(a)
            print("Goodnight,", (player), ".")
            time.sleep(b)
            print("Final points: ", (points))
            x = points
            win_lose(x)
            break
        if sleep == "bed" or sleep == "Bed":
            print("You begin shoveling the heap of clothes off the bed.")
            time.sleep(a)
            print("Wait a minute...")
            time.sleep(a)
            print("You found a vape!")
            time.sleep(a)
            points = points + 1000000
            print("1000000 points have been added to your score.")
            time.sleep(a)
            print("Congrats on your new souvenir.")
            time.sleep(a)
            print("You lay down on the bed and fall swiftly to sleep.")
            time.sleep(a)
            print("Goodnight,", (player), ".")
            time.sleep(b)
            print("Final points: ", (points))
            x = points
            win_lose(x)
            break
        else:
            print("That is not an option. Please choose the bed or floor.")
            time.sleep(a)
            sleep = input("Does the bed or floor look more appealing? ")


def win_lose(x: int) -> None:
    """Determine your performance."""
    if x > 300:
        print("Wow, you could probably survive any frat!")
    if x == 1000000:
        print("This vape will keep you nice and safe. You win the game.")
    else:
        if x == 0:
            print("Eh, everyone gets tired. Let's just hope the hangover isn't bad tomorrow.")
        else:
            print("You may have made it out... but barely.")


if __name__ == "__main__":
    main()
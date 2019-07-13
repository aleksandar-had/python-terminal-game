from sys import exit
import random


class Scene(object):
    """All of the text description in the different Scenes has been copied from Zed Shaw's book: 'Learn Python The Hard Way 3rd Edition' """

    def enter(self):
        print("Scene not yet configured. Subclass it and implement enter()-Method.")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n~~~~~~~~~~~")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

    d_msg = [
        "\nThat wasn't good...\nGame Over",
        "\nLook like you won't be making it this time...\nGame Over",
        "\nOh no, that was bad...\nGame Over",
        "\nGet better at this and try again...\nGame Over"   
        ]

    def enter(self):
        print(Death.d_msg[random.randint(0, len(self.d_msg)-1)])
        print("\nOr is it?")
        choice = input("Play again? [y/n]> ")
        if choice == 'y':
            return 'central_corridor'
        else:
            print("Thanks for playing. Bye.")
            exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(
            """The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod. \nYou're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you."""
            )
        action = input("\nWhat do you do?> ")

        if action.lower() == "shoot":
            print(
                """\nQuick on the draw you yank out your blaster and fire it at the Gothon. His clown costume is flowing and moving around his body, which throws off your aim. Your laser hits his costume but misses him entirely. This completely ruins his brand new costume his mother bought him, which makes him fly into a rage and blast you repeatedly in the face until you are dead. Then he eats you."""
                )
            return 'death'

        elif action.lower() == "dodge":
            print(
                """\nLike a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head. In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your head and eats you."""
                )
            return 'death'

        elif action.lower() == "tell a joke":
            print(
                """\nLucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothon stops, tries not to laugh, then busts out laughing and can't move. While he's laughing you run up and shoot him square in the head putting him down, then jump through the Weapon Armory door."""
                )
            return 'armory'

        else:
            print("UNKNOWN COMMAND! DOES NOT COMPUTE!")
            return 'central_corridor'


class Armory(Scene):

    def enter(self):
        print(
            """\nYou do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding. It's dead quiet,too quiet. You stand up and run to the far side of the room and find theneutron bomb in its container. There's a keypad lock on the boxand you need the code to get the bomb out. If you get the codewrong 10 times then the lock closes forever and you can'tget the bomb. The code is 3 digits."""
            )
        code = "{}{}{}".format(random.randint(1,9), random.randint(1,9), random.randint(1,9))
        guess = input("[KEYPAD]> ")
        guesses = 0

        while guess != code and guesses < 10 and guess != '3734':
            print("BZtsssu!")
            print("Code incorrect!")
            guesses += 1
            guess = input("[KEYPAD]> ")

        if guess == code or guess == '3734':
            print("BZ...click")
            if guess == '3734':
                print("\n***I saw you do that...***")
            else:
                print(
                """\nThe container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot."""
                )
            return 'the_bridge'

        else:
            print(
                """\nThe lock buzzes one last time and then you hear it melting down and fusing the mechanism in order to prevent further code entries. A loud alarm is set. You here the Gothons in the distance charging towards your position. At least you tried..."""
                )
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(
            """\nYou burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship. Each of them has an even uglier clown costume than the last. They haven't pulled their weapons out yet, as they see the active bomb under your arm and don't want to set it off."""
            )

        action = input("\nWhat do you do?> ")

        if action.lower() == "throw the bomb":
            print(
                """In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you drop it a Gothon shoots you right in the back killing you. As you die you see another Gothon frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off."""
                )
            return 'death'

        elif action.lower() == "slowly place the bomb":
            print(
                """\nYou point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat. You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing your blaster at it. You then jump back through the door, punch the close button and blast the lock so the Gothons can't get out. Now that the bomb is placed you run to the escape pod to get off this tin can."""
                )
            return 'escape_pod'

        else:
            print("UNKNOWN COMMAND! DOES NOT COMPUTE!")
            return 'the_bridge'

class Escape(Scene):

    def enter(self):
        print(
            """\nYou rush through the ship desperately trying to make it to the escape pod before the whole ship explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. You get to the chamber with the escape pods, and now need to pick one to take. Some of them could be damaged but you don't have time to look. There's 5 pods, which one do you take?"""
            )

        good_pod = random.randint(1,5)
        guess = input("Pod Number:> ")

        if int(guess) == good_pod or guess == '42':
            if guess == '42':
                print("\n***It seems like you know a lot of hidden doors.***")

            print(f"\nYou jump into pod {guess} and hit the eject button.")
            print(
                """The pod easily slides out into space heading to the planet below. As it flies to the planet, you look back and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time. \nYou won!\n"""
                )
            exit(1)
        else:
            print(f"\nYou jump into pod {guess} and hit the eject button.")
            print(
                """The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly."""
                )
            return 'death'



class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'armory': Armory(),
        'the_bridge': TheBridge(),
        'escape_pod': Escape(),
        'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()




"""
Please ignore this, it is not part of the final.  It was the original place holder file when creating the GitHub repo.
"""


import random

# Pet classes
class Pet:
    species_name = "Server Pet"
    face = "(^_^)"
    base_health = 10
    base_energy = 8
    base_mood = 5

    def __init__(self):
        # Protected attributes
        self._health = 0
        self._energy = 0
        self._mood = 0


        self.health = self.base_health
        self.energy = self.base_energy
        self.mood = self.base_mood

        self.traits = [
            "grumpy", "cute", "curious", "clever", "loyal",
            "bored", "caffeinated", "snarky", "kind"
        ]
        self.keytrait = random.choice(self.traits)


#Properties (getters/setters)

    def get_health(self):
        return self._health

    def set_health(self, value):
        self._health = max(0, int(value))

    def get_energy(self):
        return self._energy

    def set_energy(self, value):
        self._energy = max(0, int(value))

    def get_mood(self):
        return self._mood

    def set_mood(self, value):
        self._mood = max(0, int(value))

    # ----- @properties -----

    @property
    def health(self):
        return self.get_health()

    @health.setter
    def health(self, value):
        self.set_health(value)

    @property
    def energy(self):
        return self.get_energy()

    @energy.setter
    def energy(self, value):
        self.set_energy(value)

    @property
    def mood(self):
        return self.get_mood()

    @mood.setter
    def mood(self, value):
        self.set_mood(value)

    # ----  Game behavior ----

    def new_trait_each_turn(self):
        self.keytrait = random.choice(self.traits)

    def show_stats(self):
        print("Current status:")
        print(f"  Pet:    {self.species_name} {self.face}")
        print(f"  Trait:  {self.keytrait}")
        print(f"  Health: {self.health}")
        print(f"  Energy: {self.energy}")
        print(f"  Mood:   {self.mood}\n")

    def feed_coffee(self):
        self.energy += 3
        self.mood += 1
        print("You fed hot, delicious coffee. The server pet hums with delight!")

    def apply_patches(self):
        self.health += 3
        self.energy -= 2
        print("Patches applied. Stability improves, but now you're tired.")

    def restart_service(self):
        self.health += 2
        self.energy -= 1
        print("Service restarted. Things look better.")

    def ignore_alerts(self):
        self.energy += 1
        self.health -= 3
        self.mood -= 1
        print("You ignored alerts... yikes. The pet looks worried.")

    def time_passes(self):
        self.health -= 1
        self.energy -= 1

    def get_events(self):
        """
        Subclasses can override this to provide pet-specific events.
        Each event: (text, health_change, energy_change, mood_change)
        """
        return [
            ("A printer demon attacks!", -2, 0, -1),
            ("A surprise update installs cleanly!", +2, -1, +1),
            ("A user clicks a phishing link...", -3, 0, -1),
            ("You find a forgotten coffee stash!", 0, +2, +1),
        ]

    def random_event(self):
        """
        Original style: 20% chance, print the event, apply changes immediately.
        """
        if random.random() < 0.2:
            events = self.get_events()
            text, h_change, e_change, m_change = random.choice(events)

            print("\n*** RANDOM EVENT! ***")
            print(text)

            if h_change > 0:
                print(f"You gained {h_change} health.")
            elif h_change < 0:
                print(f"You lost {-h_change} health.")

            if e_change > 0:
                print(f"You gained {e_change} energy.")
            elif e_change < 0:
                print(f"You lost {-e_change} energy.")

            if m_change > 0:
                print(f"You gained {m_change} mood point(s).")
            elif m_change < 0:
                print(f"You lost {-m_change} mood point(s).")

            self.health += h_change
            self.energy += e_change
            self.mood += m_change

# ---- Win or Lose Art ----


    def win_art(self):
        return [
r"""
  \o/
   |
  / \
""",
r"""
 _\o_
   |
  / \
"""
        ]

    def lose_art(self):
        return r"""
  ( -_-) zZz
   /|\
   / \
"""

#---- Pet Subclasses ----

class Penguin(Pet):
    species_name = "Penguin"
    face = "<(oVo)>"
    base_health = 11
    base_energy = 7
    base_mood = 6

    def feed_coffee(self):
        self.energy += 3
        self.mood += 2
        print("You fed coffee. The penguin waddles happily and chirps!")

    def get_events(self):
        return [
            ("The penguin slides across the server room floor and bonks a cable!", -2, 0, -1),
            ("A chilly breeze cools the hardware. Temps look great!", +2, 0, +1),
            ("The penguin finds a lost USB drive (it was yours).", 0, +1, +1),
            ("Ice builds up in the vents… airflow drops.", -2, -1, 0),
        ]

    def win_art(self):
        return [
r"""
   .-____-.
  /  o  o  \
 |    V     |
 |   ( )    |
 |  (   )   |__
  \  \_/   /  /
   '-----'  /
""",
r"""
   .-____-.
  /  o  o  \
 |    V     |
 |   ( )    |
 |  (   )   |__
  \  \_/   / _/
   '-----'  /
"""
        ]

    def lose_art(self):
        return r"""
.-____-.
/  -  -  \   zZz
|    V     |
|   ( )    |
|  (   )   |
\  \_/   /
'-----'
"""

class Cat(Pet):
    species_name = "Cat"
    face = "(=^･^=)"
    base_health = 9
    base_energy = 9
    base_mood = 6

    def ignore_alerts(self):
        self.energy += 1
        self.health -= 3
        print("You ignored alerts. The cat stares at you like it owns the datacenter.")

    def get_events(self):
        return [
            ("The cat walks across the keyboard and runs a mysterious command.", -2, 0, -1),
            ("The cat naps on the warm router. Somehow… everything is fine.", +2, 0, +1),
            ("The cat knocks over a cup near the rack (you saved it in time).", 0, -1, -1),
            ("The cat purrs loudly; morale improves in the entire office.", 0, +1, +2),
        ]
    def win_art(self):
        return [
r"""
 /\_/\  
( o.o )  /
 > ^ <  /
""",
r"""
 /\_/\  
( o.o ) _/
 > ^ <  /
"""
        ]

    def lose_art(self):
        return r"""
 /\_/\  
( -.- ) zZz
 > ^ <
"""

class Bat(Pet):
    species_name = "Bat"
    face = "/|\\ ^._.^ /|\\"
    base_health = 10
    base_energy = 8
    base_mood = 5

    def time_passes(self):
        self.health -= 1
        print("(Night shift bonus: bat doesn't lose energy this turn.)")

    def get_events(self):
        return [
            ("The bat spots suspicious traffic in the dark—blocked just in time!", +2, -1, +1),
            ("A late-night outage hits. The bat is awake, but it's still rough.", -3, 0, -1),
            ("The bat discovers an old log file that explains everything.", +1, 0, +1),
            ("The bat flutters into a ceiling fan. Chaos. (It’s okay!)", -2, 0, -1),
        ]

    def win_art(self):
        return [
r"""
/|\  ^._.^  /|\
  \   | |   /
   \  | |  /
      | |
     /   \
""",
r"""
\|/  ^._.^  \|/
   \  | |  /
    \ | | /
      | |
     /   \
"""
        ]

    def lose_art(self):
        return r"""

/|\  ^._.^  /|\
     zZz
   __| |__
  /       \
"""


class Fox(Pet):
    species_name = "Fox"
    face = "(=^.^=)"
    base_health = 10
    base_energy = 8
    base_mood = 5

    def apply_patches(self):
        self.health += 4
        self.energy -= 2
        print("The fox cleverly batches patches. Big stability gains!")

    def get_events(self):
        return [
            ("The fox sneaks into the config files and 'optimizes' something.", +1, -1, 0),
            ("The fox outsmarts a phishing attempt with a perfect filter rule.", +2, 0, +1),
            ("The fox steals your snack. You're distracted.", 0, -2, -1),
            ("The fox finds a shortcut script that saves you time.", 0, +2, +1),
        ]
    def win_art(self):
        return [
r"""
  /\     /\
 (=^.^= )  /
  (_____) /~~
   U   U
""",
r"""
  /\     /\
 (=^.^= ) _/
  (_____) \~~
   U   U
"""
        ]

    def lose_art(self):
        return r"""
/\     /\
(= -.-=) zZz
(_____)
U   U
"""

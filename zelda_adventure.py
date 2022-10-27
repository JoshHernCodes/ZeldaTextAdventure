import time
import random
import sys
recruit = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)

# Start of game.


def game_intro():
    print_pause("Hyrule is in peril. The Dark Lord Ganon has spent decades"
                " amassing power.")
    print_pause("He has gathered together an army of minions large enough"
                " to take over Hyrule.")
    print_pause("With his powerful army, Ganon has managed to overwhelm"
                " the four strongest guardians of Hyrule.")
    print_pause("You, the bodyguard of Princess Zelda, have suffered a"
                " near fatal blow at the hands of Ganon.")
    print_pause("Zelda uses her magic to teleport you away to safety,"
                " and encloses Ganon in a magic sphere.")
    print_pause("This sphere can only last for so long.")
    print_pause("Hyrule's only hope is for you to gather your strength and"
                " unite the guardians for one last fight against Ganon.")
    print_pause("You awaken in a hidden cave. Upon exiting, you hear the"
                " voice of Zelda in your mind.")
    print_pause("She desperately calls for your help, knowing that she can"
                " only hold off Ganon for so much longer.")
    print_pause("You fear she requires your help imminently, but know you"
                " lack the tools and support to guarantee victory.")

# Below function provides user the option to quit or start over upon losing.


def game_over():
    print_pause("Your journey has come to an end. Do you wish to try again?")
    choice = input("1. Yes\n"
                   "2. No\n")
    if choice == "1":
        recruit.clear()
        game_intro()
        destination_choice()
    elif choice == "2":
        print_pause("Hyrule will always be here ready to be saved.")
        sys.exit()
    else:
        print_pause("That is not an option at this time")
        game_over()


# Below function defines interactions with old man.


def old_man():
    if "master_sword" in recruit:
        print_pause("Hello again Master!")
        print_pause("There are many in Hyrule that need your help,"
                    " including Princess Zelda.")
        print_pause("Please render as much aid as you can and stop Ganon and"
                    " his forces.")
    else:
        recruit.append("master_sword")
        print_pause("In the distance you see an old man. You sense that you"
                    " know him but can't recall.")
        print_pause("As you walk towards him, he greets you with a warm"
                    " smile.")
        print_pause('The old man begins to speak, "Hello Master! I\'m glad'
                    ' to see you\'ve awoken."')
        print_pause("I know you must feel very lost. Do you remember your"
                    " name?")
        name = input("The old man waits for you to answer with your name.\n")
        print_pause("Yes Master " + name + "! I'm glad to see you still have"
                    " some of your memories.")
        print_pause("Hyrule needs your help. Princess Zelda is holding off"
                    " Ganon but can not hold on much longer.")
        print_pause("The Guardians of Hyrule wish to help, but they are all"
                    " spread thin defending again Ganon's forces.")
        print_pause("Perhaps if you help the Guardians they can in turn"
                    " help you, but I don't know if the Princess can wait"
                    " that long.")
        print_pause("I don't know what the best path is for you to take,"
                    " but I do know you can't take it empty handed.")
        print_pause("The old man hands you green tunic armor, a bow with"
                    " arrows, and the legendary Master Sword.")
        print_pause("Please Master " + name + ", do what you can to save"
                    " Hyrule before it's too late!")
    destination_choice()

# Below function checks if user has gotten Master Sword from old
# man before venturing out.


def sword_check():
    if "master_sword" not in recruit:
        print_pause("As you are about to venture off, you realize it may"
                    " be wise to arm yourself first.")
        print_pause("Otherwise you may not last very long in Hyrule"
                    " at all.")
        destination_choice()


# Below function defines what occurs should user chose to retreat
# from a battle.


def retreat():
    print_pause("You feel ill prepared for this battle and decide to"
                " return when you can be better help.")


# Below function defines interactions at Rito Village.


def rito_village():
    sword_check()
    if "revali" in recruit:
        print_pause("You consider returning to Rito Village, but Revali"
                    " assures you the villagers will be safe for now.")
    else:
        print_pause("You approach Rito Village and realize the area is"
                    " swarming with Moblins.")
        print_pause("The Rito Tribe are doing their best to fight off"
                    " the Moblins but are being overrun.")
        print_pause("Flying in the sky you see the Guardian Revali raining"
                    " arrows upon the Moblins with his trusty bow.")
        print_pause("Suddenly a Great Moblin tosses a spear at Revali and"
                    " clips his wing.")
        print_pause("As Revali falls to the ground, the Great Moblin"
                    " stands before him, ready to strike again.")
        while True:
            choice = input(
                "What do you wish to do?\n"
                "1. Attack\n"
                "2. Retreat\n")
            if choice == "1":
                roll = random.randint(5, 10)
                if roll >= 6:
                    recruit.append("revali")
                    print_pause("You draw the Master Sword and leap forward."
                                " The Great Moblin raises his club to"
                                " strike Revali")
                    print_pause("But before he could finish his strike, "
                                "you pierce The Great Moblin in the back, "
                                " bringing him down.")
                    print_pause("With a look of gratefulness, Revali leaps"
                                " to his feet. Together you take down the"
                                " remaining Moblins.")
                    print_pause("Rito village is safe for now. Revail agrees"
                                " to joins you in your quest to stop Ganon.")
                else:
                    print_pause("You try to save Revali, but it's too late."
                                " The Great Moblin turns his attention"
                                " to you.")
                    print_pause("You dodge his first strike but suddenly a"
                                " large group of Moblins are surrounding you.")
                    print_pause("There are too many for even you to take on."
                                " Sadly they strike you down.")
                    print_pause("Sadly Hyrule won't be save this day.")
                    game_over()
                break
            elif choice == "2":
                retreat()
                break
            else:
                print_pause("That is not an option at this time")
    destination_choice()

# Below function defines interactions at Gerudo Desert.


def gerudo_desert():
    sword_check()
    if "urbosa" in recruit:
        print_pause("You consider returning to Gerudo Town, but Urbosa"
                    " assures you the villagers will be safe for now.")
    else:
        print_pause("You make your way into the desert and head towards"
                    " Gerudo Town.")
        print_pause("As you are getting close, you see Guardian Urbosa"
                    " entrenched in a heavy fight with several Lizalfos.")
        print_pause("Urbosa is taking them down with ease, but a few"
                    " meters away is a sand worm Molduga"
                    " fastly approaching.")
        print_pause("Urbosa does not see the beast coming and does not"
                    " realize she is in imminent danger.")
        while True:
            choice = input(
                "What do you wish to do?\n"
                "1. Attack\n"
                "2. Retreat\n")
            if choice == "1":
                if "revali" in recruit:
                    recruit.append("urbosa")
                    print_pause("You draw your sword and rush forward."
                                " You shout at Urbosa to look out.")
                    print_pause("The Molduga is inching closer to Urbosa"
                                " and is about to strike.")
                    print_pause("Suddenly Revali flies into the sky while"
                                " drawing his bow.")
                    print_pause("He rapidly shoots several arrows down"
                                " at the Molduga.")
                    print_pause("Inches away from Urbosa, The Molduga"
                                " rises from the sand and crashes.")
                    print_pause("It lands on and crushes the group of"
                                " Lizalfos that Urbosa was fighting.")
                    print_pause("Urbosa is grateful to see old friends."
                                " She agrees to help you on your journey.")
                    break
                else:
                    roll = random.randint(3, 10)
                    if roll >= 6:
                        recruit.append("urbosa")
                        print_pause("you rush forward while shouting at"
                                    " Urbosa to look out.")
                        print_pause("Having warned her, she manages to dodge"
                                    " back just as the Molduga is rising.")
                        print_pause("As luck would have it, the Molduga"
                                    " swallows the nearby Lizalfos.")
                        print_pause("With your sword drawn, you leap atop the"
                                    " Molduga and begin to strike.")
                        print_pause("Urbosa joins you, and in time the"
                                    " Molduga falls to the ground.")
                        print_pause("Urbosa thanks you for your perfect"
                                    " timing. She agrees to join you.")
                    else:
                        print_pause("You shout at Urbosa trying to warn her,"
                                    " but it's too late.")
                        print_pause("Suddenly the Molduga rises from the"
                                    " sand and swallows her whole.")
                        print_pause("In your effort to save her, you did not"
                                    " realize the several Lizalfos"
                                    " behind you.")
                        print_pause("While watching Urbosa's defeat in horror,"
                                    " you are struck down.")
                        game_over()
                    break
            elif choice == "2":
                retreat()
                break
            else:
                print_pause("That is not an option at this time.")
    destination_choice()

# Below function defines interactions at Lake Hylia.


def lake_hylia():
    sword_check()
    if "mipha" in recruit:
        print_pause("You consider returning to Zora's Domain, but Mipha"
                    " assures you her tribe will be safe for now.")
    else:
        print_pause("You cross the Bridge of Hylia and begin making your way"
                    " to Zora's Domain.")
        print_pause("As you approach, you see most of the members of the Zora"
                    " tribe shielding themselves.")
        print_pause("A massive group of Water Octoroks have appeared, and are"
                    " shooting rocks at the Zoras at a fast pace.")
        print_pause("You see Princess Mipha among the tribe. She appears to be"
                    " injured.")
        while True:
            choice = input(
                "What do you wish to do?\n"
                "1. Attack\n"
                "2. Retreat\n")
            if choice == "1":
                if "urbosa" in recruit:
                    recruit.append("mipha")
                    print_pause("Urbosa draws her scimitar and begins charging"
                                " her lightning energy.")
                    print_pause("She strikes the surface of the surrounding"
                                " water, causing a massive charge"
                                " to flow through")
                    print_pause("Almost instantly all the Octoroks are"
                                " shocked and destroyed.")
                    print_pause("You rush to Mipha's side. Fortunately her"
                                " wounds are minor.")
                    print_pause("She uses her healing ability and is better"
                                " in an instant.")
                    print_pause("She knows Ganon is causing much chaos and"
                                " agrees to join you.")
                    break
                else:
                    roll = random.randint(3, 10)
                    if roll >= 6:
                        recruit.append("mipha")
                        print_pause("You draw your bow and begin shooting"
                                    " the Octoroks one by one.")
                        print_pause("As you thin their numbers out, The Zora"
                                    " tribe members are able to move.")
                        print_pause("The tribe members help you eliminate"
                                    " the remaining Octoroks.")
                        print_pause("You rush to Mipha's side. Fortunately"
                                    " her wounds are minor.")
                        print_pause("She uses her healing ability and is"
                                    " better in an instant.")
                        print_pause("She knows Ganon is causing much chaos"
                                    " and agrees to join you.")
                    else:
                        print_pause("You draw your bow and begin to shoot"
                                    " several Octoroks.")
                        print_pause("Sadly there are too many and in time"
                                    " they begin shooting back at you.")
                        print_pause("You take a blow to the head and"
                                    " fall unconscious.")
                        game_over()
                    break
            elif choice == "2":
                retreat()
                break
            else:
                print_pause("That is not an option at this time.")
    destination_choice()

# Below function defines interaction at Death Mountain.


def death_mountain():
    sword_check()
    if "daruk" in recruit:
        print_pause("You consider returning to Goron City, but Daruk"
                    " assures you the Gorons will be safe for now.")
    else:
        print_pause("You slowly begin to climb your way up"
                    " Death Mountain.")
        print_pause("This is no simple task as there is lava"
                    " surrounding nearly everywhere.")
        print_pause("In the distance you see Goron City, which is"
                    " being swarmed by Bokoblins.")
        print_pause("The Goron are holding their ground, but there"
                    " seems no end in sight to the number of"
                    " Bokoblins.")
        print_pause("You see Guardian Daruk grabbing Bokoblins by"
                    " the feet and tossing them into lava with ease.")
        while True:
            choice = input(
                "What do you wish to do?\n"
                "1. Attack\n"
                "2. Retreat\n")
            if choice == "1":
                if "mipha" in recruit:
                    recruit.append("daruk")
                    print_pause("You try to sprint foward, but much"
                                " lava is still in your way.")
                    print_pause("Mipha uses her water magic to cool"
                                " off the lava nearby, allowing you"
                                " to move forward.")
                    print_pause("Daruk sees you and begins tossing"
                                " Bokoblins your way.")
                    print_pause("You leap to the air and chop down"
                                " each Bokoblin tossed towards you.")
                    print_pause("In time the Bokoblins are taken"
                                " down, and Goron City is safe.")
                    print_pause("Daruk greets you with a giant"
                                " pat on the back.")
                    print_pause("He agrees to join you in"
                                " defeating Ganon.")
                    break
                else:
                    roll = random.randint(3, 10)
                    if roll >= 6:
                        recruit.append("daruk")
                        print_pause("You race towards Goron City"
                                    " which provides difficult due"
                                    " to the lava.")
                        print_pause("Daruk is taking down the"
                                    " Bokoblins with ease, but"
                                    " there are still too many to count.")
                        print_pause("Finally you make it past the lava and"
                                    " strike down Bokoblin after Bokoblin.")
                        print_pause("You turn around and see a large swarm"
                                    " of Bokoblins rushing you.")
                        print_pause("Daruk screams at you to move aside,"
                                    " which you quickly do.")
                        print_pause("Daruk shapes his body into a giant"
                                    " boulder and rolls towards the"
                                    " Bokoblins.")
                        print_pause("He takes them all down like a perfect"
                                    " strike in bowling.")
                        print_pause("The area is now safe. Daruk greets you"
                                    " with a giant slap on the back.")
                        print_pause("He agrees to join you in defeating"
                                    " Ganon.")
                    else:
                        print_pause("You try to race towards Goron City, but"
                                    " lava stands in your way.")
                        print_pause("Suddenly even more Bokoblins arrive and"
                                    " the Goron become overwhelmed.")
                        print_pause("In rushing to help you have a misstep,"
                                    " causing you to slip and fall"
                                    " into the lava.")
                        game_over()
                    break
            elif choice == "2":
                retreat()
                break
            else:
                print_pause("That is not an option at this time.")
    destination_choice()

# Below function defines final battle.


def fight_ganon():
    while True:
        if len(recruit) == 5:
            roll = random.randint(5, 10)
            print_pause("You race towards Hyrule Castle with your companions,"
                        " hoping it's not too late.")
            print_pause("Upon entering you find Princess Zelda on the ground."
                        " Her energy depleted.")
            print_pause("Ganon is standing there, having morphed into his"
                        " most demonic form.")
            if roll >= 6:
                print_pause("Ganon roars and shoots fireballs, forcing the"
                            " Guardians to dodge.")
                print_pause("The Guardians then rush in. Striking Ganon from"
                            " all angles.")
                print_pause("They manage to force Ganon to trip to the ground,"
                            " leaving him vulnerable.")
                print_pause("With Master Sword in hand, you rush foward and"
                            " pierce Ganon in the heart.")
                print_pause("Everyone heads towards Zelda. Though weak, she"
                            " is relieved to see your face.")
                print_pause("Hyrule is safe. though a time for rebuilding"
                            " must begin.")
                break
            else:
                print_pause("You and the Guardians try your best to take"
                            " him down, but his power is too great.")
                print_pause("One by one you are all struck down. Ganon"
                            " has won. Hyrule belongs to him.")
                break
        elif len(recruit) == 4:
            roll = random.randint(4, 10)
            print_pause("You arrive at Hyrule Castle with "
                        + recruit[1].capitalize() +
                        ", " + recruit[2].capitalize() + ", and " +
                        recruit[3].capitalize() + " by your side.")
            print_pause("You have a good amount of help, but victory is"
                        " never guaranteed.")
            if roll >= 6:
                print_pause("Ganon stands before you looking more powerful"
                            " than ever.")
                print_pause("Princess Zelda is laying nearby you; Her"
                            " energy depleted.")
                print_pause("Ganon begins attacking agressively. The"
                            " Guardians spread out to avoid his attacks.")
                print_pause("Despite his strengh, Ganon finds it difficult"
                            " to hit so many targets.")
                print_pause("Zelda stands. Using her last bit of strengh,"
                            " she conjures a magic bow and strikes Ganon.")
                print_pause("The strengh of the blow brings Ganon to the"
                            " ground. He is defeated.")
                print_pause("Zelda falls to the ground unconscious."
                            " You rush to her side.")
                print_pause("Hyrule is safe, but whether Zelda will"
                            " recover remains to be seen.")
                break
            else:
                print_pause("Ganon stands before you holding the body of"
                            " Princess Zelda.")
                print_pause("With little time to react, Ganon tosses Zelda's"
                            " body towards " + recruit[3].capitalize() +
                            " and " + recruit[1].capitalize() + ".")
                print_pause("The force of her body smashes them again"
                            " the wall, forcing them unconscious.")
                print_pause("You rush forward to strike Ganon but miss.")
                print_pause("Ganon strikes you from behind to the back"
                            " of the head.")
                print_pause("You fall to the ground. Leaving "
                            + recruit[2].capitalize() +
                            " alone to face Ganon.")
                print_pause("You won't live to know if Hyrule is saved.")
                break
        elif len(recruit) == 3:
            roll = random.randint(2, 10)
            print_pause("You arrive at Hyrule Castle with "
                        + recruit[1].capitalize() + ", and "
                        + recruit[2].capitalize() + " by your side.")
            print_pause("You welcome their help, but fear this may"
                        " not be enough to defeat Ganon.")
            if roll >= 6:
                print_pause(recruit[1].capitalize() +
                            " and " + recruit[2].capitalize() +
                            " rush to Ganon's side and strike him"
                            " in the legs.")
                print_pause("Ganon slips to the ground, giving you a chance"
                            " to strike.")
                print_pause("With your sword drawn, you leap up and"
                            " pierce Ganon through the head.")
                print_pause("Ganon is defeated. You can rest"
                            " easy. For now.....")
                break
            else:
                print_pause("It would seem your intuition is correct."
                            " Upon entering " + recruit[2].capitalize() +
                            " is struck down by Ganon.")
                print_pause(recruit[1].capitalize() + " rushes "
                            "to attack Ganon from the side.")
                print_pause("Ganon performs a sweep move which takes "
                            + recruit[1].capitalize() + " down at once.")
                print_pause("You attempt to take Ganon on alone, but"
                            " his strengh is too great.")
                print_pause("Despite your efforts Ganon manages to"
                            " sweep you to the ground and pummel you.")
                break
        elif len(recruit) == 2:
            roll = random.randint(1, 7)
            print_pause("You rush to Hyrule Castle hoping you're"
                        " in time to help Princess Zelda.")
            print_pause("With only " + recruit[1].capitalize() +
                        " by your side, you hope this is enough"
                        " to defeat Ganon.")
            if roll >= 6:
                print_pause(recruit[1].capitalize() + " begins"
                            " running around Ganon, focusing his"
                            " attention.")
                print_pause("You swiftly pierce Ganon then run"
                            " around diverting his attention.")
                print_pause("This tactic between you and "
                            + recruit[1].capitalize() + " works well"
                            " enough to get in multiple strikes.")
                print_pause("Though it takes time, eventually Ganon"
                            " is overwhelmed and falls from his wounds.")
                print_pause("Despite slim odds, you managed to"
                            " save Hyrule. For now.....")
                break
            else:
                print_pause("Immediately you realize that you are"
                            " ill prepared.")
                print_pause("Ganon shoots massive bolts of energy"
                            " at you and " + recruit[1].capitalize() + ".")
                print_pause("You are both shot down before you even had"
                            " a chance.")
                break
        elif len(recruit) == 1:
            roll = random.randint(1, 6)
            print_pause("You rush to Hyrule castle alone to help"
                        " Princess Zelda.")
            print_pause("There is no one to help you.")
            if roll >= 6:
                print_pause("Zelda is laying on the ground unconscious.")
                print_pause("Ganon stands before you stronger than ever.")
                print_pause("You try your best to block and dodge his"
                            " constant attacks.")
                print_pause("He manages to strike you to the ground.")
                print_pause("Just as he raises his hand for a final blow,"
                            " you see an opening.")
                print_pause("You quickly raises the Master Sword and"
                            " pierce Ganon's chest.")
                print_pause("It was a lucky hit that brings him to"
                            " the ground.")
                print_pause("Hyrule is safe, but only by a miracle chance.")
                break
            else:
                print_pause("Ganon immediately strikes you down upon"
                            " stepping foot into the castle.")
                print_pause("You strike Ganon with the Master Sword"
                            " but the attack does nothing.")
                print_pause("Ganon crushes you where you stand.")
                break
        else:
            roll = random.randint(1, 5)
            print_pause("You arrive to Hyrule Castle with nothing.")
            print_pause("Ganon crushes you within seconds of you"
                        " stepping into the castle.")
            print_pause("Arriving ill equipped was futile. Hyrule is ruined.")
            break
    game_over()


def destination_choice():
    choice = input(
        "What do you wish to do?\n"
        "1. Walk towards the old man nearby a giant tree.\n"
        "2. Head towards Rito village in Western Hyrule.\n"
        "3. Head towards Gerudo Desert.\n"
        "4. Head towards Lake Hylia.\n"
        "5. Head towards Death Mountain.\n"
        "6. Head towards Hyrule Castle to fight Ganon.\n")
    if choice == "1":
        old_man()
    elif choice == "2":
        rito_village()
    elif choice == "3":
        gerudo_desert()
    elif choice == "4":
        lake_hylia()
    elif choice == "5":
        death_mountain()
    elif choice == "6":
        fight_ganon()
    else:
        print_pause("That is not an option at this time.")
        destination_choice()


game_intro()

destination_choice()

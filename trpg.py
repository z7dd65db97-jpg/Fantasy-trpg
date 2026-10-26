import random
def start_game():
    php=random.randint(65,100)
    pdm=random.randint(20,100)
    luc=random.randint(1,100)
    Menu=print("HP:",php,"Damage",pdm,"Money",luc)
    stage=1
    print("THE JOURNEY STARTS NOWWW",php,"is your health,",pdm,"is your damage!Also type Menu when u want to see your stats.")
    if stage==1:
        print("----------A quiet road-----------")
        print("1.Go straight")
        print("2.Hide")
        print("3.Go into the forest")
        choice1=input("what will you do?(1/2/3):")
        if choice1=="1":
            print("you go straight and find a wolf.")
            print("1.fight")
            print("2.run away")
            choice2=input("choose if you do not want to die(1/2)")
            if choice2=="1":
                if pdm+luc>85:
                    print("You won the fight!")
                    stage=2
                else:
                    print("You're neck was bitten by a wolf.")
                    php-=30
                    stage=2
            if choice2=="2":
                if php+luc>70:
                    print("Sucessful runaway. Coward")
                    stage=2
                else:
                    print("U got bitten by a hungry wolf.")
                    php-=20
                    stage=2
        if choice1=="2":
            print("You accidently destroy a bug's nest.")
            print("1.Ignore it.")
            print("2.Fight the bug!")
            choice3=input("What are u goin to do?(1/2)")
            if choice3=="1":
                if luc>30:
                    print("The bugs didn't do a lot of damage.")
                    php-=1
                    stage=2
                else:
                    print("The bugs had poison!")
                    php-=30
                    stage=2
            else:
                if pdm+luc>85:
                    print("The bugs were easy to kill!")
                    pdm+=10
                    stage=2
                else:
                    print("How did the bug learn kung fu??")
                    php-=10
                    stage=2
        if choice1=="3":
            print("Whopps! You stepped on a man-eating plant!")
            php-=40
            stage=2
        elif stage==2:
            print("There is a lamp. What should we do?")
            choice4=input("Choooooose(1/2)")
            if choice4==1:
                if luc>50:
                    print("A genie!! Gotta do 3 wish!")
                    choice5=input("What r u going to wish for? 1. power 2.Health 3.Earn more money(1/2/3)")

start_game()



print("What do you choose?")
choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors."))
rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''
paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''
scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
rockPaperScissor = [rock, paper, scissors]

if choice == 0:
    print(rockPaperScissor[0])
elif choice == 1:
    print(rockPaperScissor[1])
elif choice == 2:
    print(rockPaperScissor[2])

number = random.randint(0, 2)
computer_choice = rockPaperScissor[number]

print(f"Computer chose:\n {computer_choice}")

if choice >= 3:
    print("You typed an invalid number, you lose!")
if choice == 0:
    if computer_choice == rock:
        print("It's a draw")
    elif computer_choice == paper:
        print("You lose")
    elif computer_choice == scissors:
        print("You win")
elif choice == 1:
    if computer_choice == rock:
        print("You win")
    elif computer_choice == paper:
        print("It's a draw")
    elif computer_choice == scissors:
        print("You lose")
elif choice == 2:
    if computer_choice == rock:
        print("You lose")
    elif computer_choice == paper:
        print("You win")
    elif computer_choice == scissors:
        print("It's a draw")
def hop_strtegy(user_input, hop_number, counter):
        game_strategy = True;
        error_massage = "GameOver!!! hop logic is invalid!";

        if user_input != "hop":
             number = int(user_input)
             if number != counter:
                print(error_massage)
                game_strategy = False
             elif counter % hop_number == 0:
                print(error_massage)
                game_strategy = False
        else:
             if counter % hop_number != 0:
                print(error_massage)
                game_strategy = False
        return game_strategy


def start_hop(hop_number):
        print("-----------------------------------")
        print("\"Let's play Hop from number 1 :)\"")
        counter = 1
        while counter <= 100:
             user_input = input("type your number\n")
             if hop_strtegy(user_input, hop_number, counter) == False:
                start_hop(hop_number)
             counter += 1

hop_number =int(input("Choose the hop number\n"))
start_hop(hop_number);

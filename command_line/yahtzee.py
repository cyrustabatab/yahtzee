


class Yahtzee:


    def __init__(self):
        self.intro_message()
        self.player_1 = self._get_name(1)
        self.player_2 = self._get_name(2)
        self._initialize_scores()
        self.print_table()

    

    def _initialize_scores(self):
        headers = ['Ones','Twos','Threes','Fours','Fives','Sixes','SUM','BONUS','Three of a kind','Four of a kind','Full House','Small straight','Large straight','Chance','YAHTZEE','TOTAL SCORE']


        self.scores = {value:[0,0] if (value.isupper() and value[0] != 'Y') else [None,None]  for value in headers}
        self.map_integer_to_value = {i:value for i,value in enumerate(headers,1) if not (value.isupper() and value[0] != 'Y')}
        print(self.map_integer_to_value)



    def intro_message(self):
        print("Welcome to Yahtzee!")


    def _get_name(self,number):


        name = input(f"Player {number} Name: ")

        return name

    
    
    def print_table(self):
        max_length = max(len(value) for value in self.scores.keys())
        player_1_length = max(4,len(self.player_1))
        player_2_length = max(4,len(self.player_2))
        print(' ' * (max_length + 4) + f'| {self.player_1:^{player_1_length}} | {self.player_2:^{player_2_length}}')
        
        
        for i,(header,scores) in enumerate(self.scores.items(),1):
            print(f"{i:>2}. {header:>{max_length}}| {scores[0] if scores[0] is not None else '':^{player_1_length}} | {scores[1] if scores[1] is not None else '':^{player_2_length}}")



"""The main module"""
class TicTac:
    """The main class."""
    def __init__(self):
        self.board = list(range(1, 10))

    def show_board(self):
        """This function shows board in console"""
        print("----------")
        for i in range(3):
            print(self.board[0+i*3], '|', self.board[1+i*3], '|', self.board[2+i*3])
        print("----------")

    def validate_input(self, user_input):
        """This function validates user's input"""
        try:
            user_input = int(user_input)
            if 1 <= user_input <= 9:
                if self.board[user_input-1] != 'X' and self.board[user_input-1] != 'O':
                    return False
                print('Данная клетка уже занята. Пожалуйста, выберите другую')
                return True
            print('Вы ввели слишком большое или слишком маленькое число. '
                  'Пожалуйста, ведите число из отрезка [1, 9]')
            return True
        except (ValueError, TypeError):
            print('Вы ввели посторонние символы. '
                  'Пожалуйста, введите натуральное число из отрезка [1, 9]')
            return True

    def start_game(self):
        """This function starts the tic_tac_toe game"""
        game_cycle_flag = False
        # game_cycle_flag is a variable which is used to loop the game and to show winner in the end
        step_cnt = 0
        while not game_cycle_flag:
            if step_cnt % 2 == 0:
                player_token = 'X'
            else:
                player_token = 'O'
            print('Введите число из отрезка [1, 9], чтобы поставить',
                  player_token,
                  'в соответствующую клетку')
            self.show_board()
            user_input = input()
            while self.validate_input(user_input):
                user_input = input()
            step_cnt += 1
            self.board[int(user_input)-1] = player_token
            game_cycle_flag = self.check_winner()
        self.show_board()
        if game_cycle_flag == 1:
            return 0
        print('Победил', game_cycle_flag)

    def check_winner(self):
        """This function checks winner"""
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in win_coord:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]]:
                return self.board[i[0]]
        draw_flag = 0
        for i in self.board:
            if i not in ('O', 'X'):
                draw_flag = 1
                break
        if draw_flag == 0:
            print('Игра окончена - ничья!')
            return True
        return False


if __name__ == "__main__":
    GAME = TicTac()
    GAME.start_game()

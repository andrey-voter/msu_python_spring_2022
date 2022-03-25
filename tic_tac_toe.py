class TicTac:

    board = list(range(1, 10))

    def show_board(self):
        print("----------")
        for i in range(3):
            print(self.board[0+i*3], '|', self.board[1+i*3], '|', self.board[2+i*3])
        print("----------")

    def validate_input(self, x):
        if not x.isnumeric():
            print('Вы ввели посторонние символы. Пожалуйста, введите натуральное число из отрезка [1, 9]')
            return 1
        if int(x) >= 1 and int(x) <= 9:
            if self.board[int(x)-1] != 'X' and self.board[int(x)-1] != 'O':
                return 0
            else:
                print('Данная клетка уже занята. Пожалуйста, выберите другую')
                return 1
        else:
            print('Вы ввели слишком большое или слишком маленькое число. Пожалуйста, ведите число из отрезка [1, 9]')
            return 1

    def start_game(self):
        flag = False
        step_cnt = 0
        while not flag:
            if step_cnt % 2 == 0:
                player_token = 'X'
            else:
                player_token = 'O'
            print('Введите число из отрезка [1, 9], чтобы поставить' + ' ' + player_token + ' ' + 'в соответствующую клетку')
            self.show_board()
            x = input()
            while (self.validate_input(x)):
                x = input()
            step_cnt += 1
            self.board[int(x)-1] = player_token
            flag = self.check_winner()
        self.show_board()
        if flag == 1:
            exit(0)
        print('Победил', flag)

    def check_winner(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in win_coord:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]]:
                return self.board[i[0]]
        draw_flag = 0
        for i in self.board:
            if i != 'X' and i != 'O':
                draw_flag = 1
                break
        if draw_flag == 0:
            print('Игра окончена - ничья!')
            return 1
        return False


if __name__ == "__main__":
    game = TicTac()
    game.start_game()

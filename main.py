def main():
    board = [
        ["# ", "# ", "# ", "# ", "# ", "# ", "# ", "# "],
        ["# ", "# ", "# ", "# ", "# ", "# ", "# ", "# "],
        ["# ", "# ", "# ", "# ", "# ", "# ", "# ", "# "],
        ["# ", "# ", "# ", "# ", "# ", "# ", "# ", "# "],
        ["# ", "# ", "# ", "# ", "# ", "# ", "# ", "# "],
        ["# ", "# ", "# ", "# ", "# ", "# ", "# ", "# "],
        ["# ", "# ", "# ", "# ", "# ", "# ", "# ", "# "],
        ["# ", "# ", "# ", "# ", "# ", "# ", "# ", "# "],
    ]
    x_coordinates = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    available_pieces = {
        "pawn": "P ",
        "bishop": "B ",
        "knight": "K ",
        "rook": "R ",
        "queen": "Q ",
        "king": "Ki",
    }

    white_piece(board, x_coordinates)
    black_piece(board, x_coordinates, available_pieces)
    knight_moves(board, available_pieces)
    pawn_moves(board, available_pieces)


def print_map(board):
    for _ in board:
        for i in _:
            print(i, end=" ")
        print()


def white_piece(board, x_coordinates):
    white = ""
    while "knight".casefold() not in white and "pawn".casefold() not in white:
        white = input("Pick a white piece (pawn/knight) and its position: ").casefold()
        x = white[-2:-1]
        for letter, index in x_coordinates.items():
            if x == letter:
                y = 8 - int(white[-1])
                if "knight".casefold() in white:
                    board[y][index] = "WK"
                    print_map(board)
                    break
                elif "pawn".casefold() in white:
                    board[y][index] = "WP"
                    print_map(board)
                    break
                else:
                    print("Wrong piece! Try again.")
                    continue


def black_piece(board, x_coordinates, available_pieces):
    count = 0
    while count < 16:
        black = input("Input a black piece and its position: ").casefold()
        if "done".casefold() not in black:
            x = black[-2:-1]
            y = 8 - int(black[-1])
            for letter, index in x_coordinates.items():
                if x == letter:
                    if board[y][index] == "# ":
                        for piece, acronym in available_pieces.items():
                            if piece in black:
                                count += 1
                                board[y][index] = acronym
                                print_map(board)
                                print("You have added a piece.")
                                break
                        else:
                            print("Incorrect piece.")
                    else:
                        print("This spot is taken! Please try again.")
        elif count >= 1 and "done".casefold() in black:
            print("Black has made its moves.")
            break
        else:
            print("You must add at least one black piece.")


def knight_moves(board, available_pieces):
    if any("WK" in sublist for sublist in board):
        for i, x in enumerate(board):
            if "WK" in x:
                y_knight = i
                x_knight = x.index("WK")

                knight_moves_list = [
                    board[y_knight - 1][x_knight - 2]
                    if y_knight - 1 >= 0 and x_knight - 2 >= 0
                    else None,
                    board[y_knight - 2][x_knight - 1]
                    if y_knight - 2 >= 0 and x_knight - 1 >= 0
                    else None,
                    board[y_knight - 2][x_knight + 1]
                    if y_knight - 2 >= 0 and x_knight + 1 <= 7
                    else None,
                    board[y_knight - 1][x_knight + 2]
                    if y_knight - 1 >= 0 and x_knight + 2 <= 7
                    else None,
                    board[y_knight + 1][x_knight + 2]
                    if y_knight + 1 <= 7 and x_knight + 2 <= 7
                    else None,
                    board[y_knight + 2][x_knight + 1]
                    if y_knight + 2 <= 7 and x_knight + 1 <= 7
                    else None,
                    board[y_knight + 2][x_knight - 1]
                    if y_knight + 2 <= 7 and x_knight - 1 >= 0
                    else None,
                    board[y_knight + 1][x_knight - 2]
                    if y_knight + 1 <= 7 and x_knight - 2 >= 0
                    else None,
                ]
                success_count = 0
                for piece, acronym in available_pieces.items():
                    if acronym in knight_moves_list:
                        success_count += 1
                        type_count = knight_moves_list.count(acronym)
                        print(f"A black {piece} is available to take.\n" * type_count)

                if success_count == 0:
                    print("No moves available.")


def pawn_moves(board, available_pieces):
    if any("WP" in sublist for sublist in board):
        for i, x in enumerate(board):
            if "WP" in x:
                y_pawn = i
                x_pawn = x.index("WP")
                pawn_moves_list = [
                    board[y_pawn - 1][x_pawn - 1]
                    if y_pawn - 1 >= 0 and x_pawn - 1 >= 0
                    else None,
                    board[y_pawn - 1][x_pawn + 1]
                    if y_pawn - 1 >= 0 and x_pawn + 1 <= 7
                    else None,
                ]
                success_count = 0
                for piece, acronym in available_pieces.items():
                    if acronym in pawn_moves_list:
                        success_count += 1
                        type_count = pawn_moves_list.count(acronym)
                        print(f"A black {piece} is available to take.\n" * type_count)

                if success_count == 0:
                    print("No moves available.")

if __name__ == "__main__":
    main()

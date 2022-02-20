import shogi.KIF

path = "/app/kifu3221.kif"

kif = shogi.KIF.Parser.parse_file(path)[0]

print(kif)
print(kif['names'][shogi.BLACK])
print(kif['names'][shogi.WHITE])
print(kif['moves'])

board = shogi.Board()
for move in kif['moves']:
    print(board.push_usi(move))
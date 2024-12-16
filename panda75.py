def count_flips(board, stone, x, y):
    """
    指定された位置に石を置いた場合にひっくり返せる石の数を計算する。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    x, y: 石を置く位置
    return: ひっくり返せる石の数
    """
    if board[y][x] != 0:
        return 0  # 石が既にある場所には置けない

    opponent = 3 - stone  # 相手の石
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total_flips = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        flips = 0

        # 指定方向で相手の石を数える
        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            flips += 1

        # 最後に自分の石で挟めているか確認
        if flips > 0 and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            total_flips += flips

    return total_flips

def best_place(board, stone):
    """
    現在のボード状態で、最も多くひっくり返せる場所を選ぶ。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    return: 最適な座標 (x, y) または None
    """
    max_flips = 0
    best_move = None

    for y in range(len(board)):
        for x in range(len(board[0])):
            flips = count_flips(board, stone, x, y)
            if flips > max_flips:
                max_flips = flips
                best_move = (x, y)

    return best_move

class EagerAI(object):
    """
    最も多くの石をひっくり返せる場所を選ぶAI。
    """

    def face(self):
        return "😎"

    def place(self, board, stone):
        move = best_place(board, stone)
        if move:
            return move
        else:
            raise ValueError("石を置ける場所がありません")

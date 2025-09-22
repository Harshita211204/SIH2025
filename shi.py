# Assuming constants and helper functions are defined elsewhere in the Python equivalent
# of the JavaScript code.

# BOARD_SIZE, PIECE_TYPES, PLAYERS, board, currentPlayerIndex, logMessage
# isValidSquare, isValidAndEmptyOrEnemy, isAlly

def player_has_movable_piece(movable_type):
    """
    Checks if the current player has any valid move for the piece type rolled.
    :param movable_type: The type of piece that can be moved (e.g., 'king', 'pawn').
    :return: True if a valid move exists, False otherwise.
    """
    player = PLAYERS[currentPlayerIndex]['id']
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            piece = board[r][c]
            if piece and piece['player'] == player:
                if piece['type'] == movable_type or (movable_type == PIECE_TYPES['KING']['name'] and piece['type'] == PIECE_TYPES['PAWN']['name']):
                    if len(calculate_valid_moves(r, c, piece)) > 0:
                        return True
    return False

def check_for_pawn_promotion(r, c, piece):
    """
    Checks if a pawn has reached a promotion square and promotes it.
    :param r: The row of the piece.
    :param c: The column of the piece.
    :param piece: The piece object.
    """
    if piece['type'] != PIECE_TYPES['PAWN']['name']:
        return

    promotion_rank = False
    if piece['player'] == 'red' and r == 7:
        promotion_rank = True
    elif piece['player'] == 'black' and r == 0:
        promotion_rank = True
    elif piece['player'] == 'yellow' and c == 0:
        promotion_rank = True
    elif piece['player'] == 'white' and c == 7:
        promotion_rank = True

    if promotion_rank:
        # In this version, pawns promote to Boats.
        board[r][c]['type'] = PIECE_TYPES['BOAT']['name']
        logMessage(f"{piece['player']}'s Pawn was promoted to a Boat!")

def check_for_game_over():
    """
    Checks if the game-over condition (a team losing all its kings) is met.
    :return: True if the game is over, False otherwise.
    """
    king_counts = {1: 0, 2: 0}
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            piece = board[r][c]
            if piece and piece['type'] == PIECE_TYPES['KING']['name']:
                # Assuming PLAYERS is a list of dictionaries with 'id' and 'alliance' keys.
                player = next((p for p in PLAYERS if p['id'] == piece['player']), None)
                if player:
                    king_counts[player['alliance']] += 1
    # If either team has 0 kings, the game is over.
    return king_counts[1] == 0 or king_counts[2] == 0

# --- Piece-Specific Move Logic ---

def calculate_valid_moves(r, c, piece):
    """
    Calculates all valid moves for a given piece at a specific position.
    :param r: The row of the piece.
    :param c: The column of the piece.
    :param piece: The piece object.
    :return: A list of valid moves.
    """
    piece_type = piece['type']
    if piece_type == PIECE_TYPES['KING']['name']:
        return get_king_moves(r, c, piece['player'])
    elif piece_type == PIECE_TYPES['ELEPHANT']['name']:
        return get_elephant_moves(r, c, piece['player'])
    elif piece_type == PIECE_TYPES['HORSE']['name']:
        return get_horse_moves(r, c, piece['player'])
    elif piece_type == PIECE_TYPES['BOAT']['name']:
        return get_boat_moves(r, c, piece['player'])
    elif piece_type == PIECE_TYPES['PAWN']['name']:
        return get_pawn_moves(r, c, piece['player'])
    return []

def get_king_moves(r, c, player):
    """
    Calculates valid moves for a King.
    :param r: The row of the piece.
    :param c: The column of the piece.
    :param player: The player ID.
    :return: A list of valid moves.
    """
    moves = []
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            new_r, new_c = r + dr, c + dc
            if isValidAndEmptyOrEnemy(new_r, new_c, player):
                moves.append({'r': new_r, 'c': new_c})
    return moves

def get_elephant_moves(r, c, player):
    """
    Calculates valid moves for an Elephant.
    :param r: The row of the piece.
    :param c: The column of the piece.
    :param player: The player ID.
    :return: A list of valid moves.
    """
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    return get_sliding_moves(r, c, player, directions)

def get_horse_moves(r, c, player):
    """
    Calculates valid moves for a Horse.
    :param r: The row of the piece.
    :param c: The column of the piece.
    :param player: The player ID.
    :return: A list of valid moves.
    """
    moves = []
    offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for dr, dc in offsets:
        new_r, new_c = r + dr, c + dc
        if isValidAndEmptyOrEnemy(new_r, new_c, player):
            moves.append({'r': new_r, 'c': new_c})
    return moves

def get_boat_moves(r, c, player):
    """
    Calculates valid moves for a Boat.
    :param r: The row of the piece.
    :param c: The column of the piece.
    :param player: The player ID.
    :return: A list of valid moves.
    """
    moves = []
    offsets = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
    for dr, dc in offsets:
        new_r, new_c = r + dr, c + dc
        if isValidAndEmptyOrEnemy(new_r, new_c, player):
            moves.append({'r': new_r, 'c': new_c})
    return moves

def get_pawn_moves(r, c, player):
    """
    Calculates valid moves for a Pawn.
    :param r: The row of the piece.
    :param c: The column of the piece.
    :param player: The player ID.
    :return: A list of valid moves.
    """
    moves = []
    forward_r, forward_c = 0, 0
    capture_offsets = []

    # Define movement direction based on player
    if player == 'red':
        forward_r, forward_c = 1, 0
        capture_offsets = [(1, -1), (1, 1)]
    elif player == 'black':
        forward_r, forward_c = -1, 0
        capture_offsets = [(-1, -1), (-1, 1)]
    elif player == 'yellow':
        forward_r, forward_c = 0, -1
        capture_offsets = [(-1, -1), (1, -1)]
    elif player == 'white':
        forward_r, forward_c = 0, 1
        capture_offsets = [(-1, 1), (1, 1)]

    # Forward move (1 square)
    new_r, new_c = r + forward_r, c + forward_c
    if isValidSquare(new_r, new_c) and not board[new_r][new_c]:
        moves.append({'r': new_r, 'c': new_c})

    # Capture moves (1 square diagonally)
    for dr, dc in capture_offsets:
        cap_r, cap_c = r + dr, c + dc
        if isValidSquare(cap_r, cap_c):
            target_piece = board[cap_r][cap_c]
            if target_piece and not isAlly(player, target_piece['player']):
                moves.append({'r': cap_r, 'c': cap_c})
    return moves

def get_sliding_moves(r, c, player, directions):
    """
    Generic function for calculating moves for sliding pieces (e.g., Elephant).
    :param r: The row of the piece.
    :param c: The column of the piece.
    :param player: The player ID.
    :param directions: A list of directional tuples (e.g., [[-1, 0], [1, 0]]).
    :return: A list of valid moves.
    """
    moves = []
    for dr, dc in directions:
        for i in range(1, BOARD_SIZE):
            new_r, new_c = r + dr * i, c + dc * i
            if not isValidSquare(new_r, new_c):
                break
            target_piece = board[new_r][new_c]
            if target_piece:
                if not isAlly(player, target_piece['player']):
                    moves.append({'r': new_r, 'c': new_c})
                break  # Path is blocked by a piece
            moves.append({'r': new_r, 'c': new_c})
    return moves
N = TEAM1 = 1
W = TEAM2 = -1
O = BLANK = 0

FILE = "87654321"
RANK = "abcdefgh"


def tuple_to_location(tup):
    print(tup)
    return RANK[tup[0]] + FILE[tup[1]]


def name_move(before, after, team):
    """
    presuming piece moves out and leaves a blank spot
    * TODO doesn't work in castling.
    """
    ranks = len(before)
    heights  = len(before[0])

    origin = ''
    destination = ''

    for file_ in range(0, ranks):
        for rank in range(0, heights):
            if before[file_][rank] != after[file_][rank]:
                if after[file_][rank] == BLANK:
                    origin = (rank, file_)
                else:
                    destination = (rank, file_)


    return tuple_to_location(origin), tuple_to_location(destination)

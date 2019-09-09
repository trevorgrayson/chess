from pytest import fixture
import copy
from algebraic_notation import *


class Test:

    @fixture
    def fresh_board(self):
        return copy.deepcopy([[0]*8]*8)
        

    def test_pawn_advance_new(self):
        board1 =  [ [TEAM1] * 8,
                    [TEAM1] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [TEAM2] * 8,
                    [TEAM2] * 8
        ]

        board2 =  [ [TEAM1] * 8,
                    [TEAM1] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [0,0,0,0,0,W,0,0], # 4
                    [BLANK] * 8,       # 3
                    [W,W,W,W,W,0,W,W], # 2
                    [TEAM2] * 8        # 1

                    #a b c d e f g h
        ]

        assert name_move(board1, board2, W) == ('f2','f4')


    def test_takes_piece_ahead(self):
        board1 =  [ [TEAM1] * 8,
                    [TEAM1] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [TEAM2] * 8,
                    [TEAM2] * 8
        ]

        board2 =  [ [TEAM1] * 8,
                    [N,N,N,N,N,W,N,N],
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [W,W,W,W,W,0,W,W],
                    [TEAM2] * 8
        ]

        assert name_move(board1, board2, W) == ('f2','f7')


    def test_moves_east(self):
        board1 =  [ [TEAM1] * 8,
                    [N,N,N,N,N,W,N,N],
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [W,W,W,W,W,0,W,W],
                    [TEAM2] * 8
        ]

        board2 =  [ [TEAM1] * 8,
                    [N,N,N,N,N,W,N,N],
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [W,0,W,W,W,W,W,W],
                    [TEAM2] * 8
        ]

        assert name_move(board1, board2, W) == ('b2','f2')


    def test_moves_diagonal(self):
        board1 =  [ [TEAM1] * 8,
                    [N,N,N,N,N,N,N,N],
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [W,W,W,W,W,W,W,W],
                    [TEAM2] * 8
        ]
        board2 =  [ [TEAM1] * 8,
                    [W,N,N,N,N,N,N,N],
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [BLANK] * 8,
                    [W,W,W,W,W,0,W,W],
                    [TEAM2] * 8
        ]


        assert name_move(board1, board2, W) == ('f2','a7')

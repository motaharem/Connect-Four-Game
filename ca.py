# 1066 Fall 2014 Project 2: Games
# Name: <Motahare Mounesan, Sepide Bod>
# Email: <cststm@gmail.com>

from util import INFINITY


### 1. Connect Four
from connectfour import *
from basicplayer import *
from util import *

## This section will contain occasional lines that you can uncomment to play
## the game interactively. Be sure to re-comment them when you're done with
## them.  Please don't turn in a problem set that sits there asking the
## grader-bot to play a game!
## 
## Uncomment this line to play a game as white:
#run_game(human_player, basic_player)

## Uncomment this line to play a game as black:
#run_game(basic_player, human_player)

## Or watch the computer play against itself:
#run_game(basic_player, basic_player)

## Change this evaluation function so that it tries to win as soon as possible,
## or lose as late as possible, when it decides that one side is certain to win.
## You don't have to change how it evaluates non-winning positions.

def focused_evaluate(board):
    """
    Given a board, return a numeric rating of how good
    that board is for the current player.
    A return value >= 1000 means that the current player has won;
    a return value <= -1000 means that the current player has lost
    """
    score = 0
    #print(board)
    if board.is_game_over():
        if(board.is_win()==board.get_current_player_id()):
            return +1000
        if(board.is_win()==board.get_other_player_id()):
            return -1000
    else:    
        set = board.chain_cells(board.get_current_player_id())
    
        while(len(set)!=0):
            temp = set.pop()
            length = len(temp)
            if(length==3):# for chain with length 3 \
                score += 80
            elif(length==2):# for chain with length 2 \
                score += 40
            elif(length==1):# for chain with length 1 \
                score -= abs(3-temp[0][1])            
        for row in range(6):
            for col in range(7):
                if board.get_cell(row, col) == board.get_other_player_id():
                    score += abs(3-col)
    return score


##Create a "player" function that uses the focused_evaluate function
#quick_to_win_player = lambda board: minimax(board, depth=4, eval_fn=focused_evaluate)

## You can try out your new evaluation function by uncommenting thi#s line:
#run_game(basic_player,quick_to_win_player)##### in basic player bud avalesh 

## Write an alpha-beta-search procedure that acts like the minimax-search
## procedure, but uses alpha-beta pruning to avoid searching bad ideas
## that can't improve the result. The tester will check your pruning by
## counting the number of static evaluations you make.
##
## You can use minimax() in basicplayer.py as an example.

def alpha_beta_search(board, depth=4, eval_fn=basic_evaluate,
                      get_next_moves_fn=get_all_next_moves,
		      is_terminal_fn=is_terminal, verbose = True):
    
    v = NEG_INFINITY
    alpha = NEG_INFINITY
    beta = INFINITY
    best_val= None

    print("inja k miay ishala !??")
    for move, new_board in get_next_moves_fn(board):
        v = max(v, Min_Val(new_board, depth, alpha, beta, eval_fn, get_next_moves_fn, is_terminal_fn))
        #if (v >= beta):
        #    return (v, move, new_board)
        #if (v >= best_val):   
        #    return (v, move, new_board)
        alpha = max(alpha,v)
        if best_val == None or v > best_val[0]:
            best_val = (v, move, new_board)
            
    if verbose:
        print "ALPHA_BETA: Decided on column %d with rating %d" % (best_val[1], best_val[0],board)

    return best_val[1]



def Min_Val(board , depth , alpha , beta,
                eval_fn = basic_evaluate ,
                get_next_moves_fn = get_all_next_moves ,
		is_terminal_fn = is_terminal ):

    print("minval")
    if is_terminal_fn(depth,board):
        return eval_fn(board)
    
    best_val = None
    v = INFINITY
    for move, new_board in get_next_moves_fn(board):
        v = min(v, Max_Val(new_board, alpha, beta, depth, basic_evaluate, get_all_next_moves, is_terminal))
        if(v <= alpha):
            return v
        beta = min(beta, v)    
        if best_val == None or v > best_val:
            best_val = v

    return best_val

def Max_Val(board, depth, alpha, beta,
                eval_fn=basic_evaluate,
                get_next_moves_fn=get_all_next_moves,
		is_terminal_fn=is_terminal):
    print("maxval")
    if is_terminal_fn(depth, board):
        return eval_fn(board)

    best_val = None
    v = NEG_INFINITY
    
    for move, new_board in get_next_moves_fn(board):
        v = max(v,Min_Val(new_board, depth, alpha, beta,basic_evaluate, get_all_next_moves, is_terminal))
        if (v >= beta):
            print("inja ^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return v
        alpha = max(alpha, v)
        if best_val == None or v > best_val:
            best_val = v
    return best_val



## Now you should be able to search twice as deep in the same amount of time.
## (Of course, this alpha-beta-player won't work until you've defined
## alpha-beta-search.)
#alphabeta_player = lambda board: alpha_beta_search(board,
                                                  # depth=4,
                                                   #eval_fn=basic_evaluate)

## This player uses progressive deepening, so it can kick your ass while
## making efficient use of time:
ab_iterative_player = lambda board: \
    run_search_function(board,
                        search_fn=alpha_beta_search,
                        eval_fn=better_evaluate, timeout=5)
#run_game(human_player, alphabeta_player)

## Finally, come up with a better evaluation function than focused-evaluate.
## By providing a different function, you should be able to beat
## simple-evaluate (or focused-evaluate) while searching to the
## same depth.

def better_evaluate(board):
    score = 0
    
    if board.is_game_over():
        if(board.is_win() == board.get_current_player_id()):
            #print(":________",board.is_win(),board.get_current_player_id())
            return +1000
        #print(":________",board.is_win(),board.get_other_player_id())

        if(board.is_win()==board.get_other_player_id()):
            #print(":________",board.is_win(),board.get_current_player_id())
            return -1000
    else:
        set = board.usefull_chain_cells(board.get_current_player_id()) 
        #print(board)
        #print(set)
        while(len(set)!=0):
            temp = set.pop()
            #print(len(temp),temp)
            length = len(temp)
            if(length==3):# for chain with length 3 \
                score += 120
                #for i in range(3):
                #    score -= abs(3-temp[i][1])
                #print("setayia",score)
            elif(length==2):# for chain with length 2 \
                score += 40
                #for i in range(2):
                #    score -= abs(3-temp[i][1])
                #print("dotayia",score)
            elif(length==1):# for chain with length 1 \
                score -= abs(3-temp[0][1])
                #print(":D")

        #print("khod",score)
        for row in range(6):
            for col in range(7):
                if board.get_cell(row, col) == board.get_other_player_id():
                    #print("chand bar miay inja !??",col)
                    score += abs(3-col)
        #print("_____________",score)
    return score
#Comment this line after you've fully implemented better_evaluate
#better_evaluate = memoize(basic_evaluate)

#khodam neveshtamOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO############################################ in vase alpha beta ba better ####
#quick_to_win_player = lambda board: alpha_beta_search(board, depth=4, eval_fn=better_evaluate)
#run_game(basic_player,quick_to_win_player)

# Uncomment this line to make your better_evaluate run faster.
better_evaluate = memoize(better_evaluate)

# For debugging: Change this if-guard to True, to unit-test
# your better_evaluate function.
if False:
    board_tuples = (( 0,0,0,0,0,0,0 ),
                    ( 0,0,0,0,0,0,0 ),
                    ( 0,0,0,0,0,0,0 ),
                    ( 0,2,2,1,1,2,0 ),
                    ( 0,2,1,2,1,2,0 ),
                    ( 2,1,2,1,1,1,0 ),
                    )
    test_board_1 = ConnectFourBoard(board_array = board_tuples,
                                    current_player = 1)
    test_board_2 = ConnectFourBoard(board_array = board_tuples,
                                    current_player = 2)
    # better evaluate from player 1
    print "%s => %s" %(test_board_1, better_evaluate(test_board_1))
    # better evaluate from player 2
    print "%s => %s" %(test_board_2, better_evaluate(test_board_2))
    
############################################################################################## in vase better evaluate #####
quick_to_win_player = lambda board: minimax(board, depth=4,
                                        eval_fn=focused_evaluate)
run_game(basic_player, quick_to_win_player)
#run_game(human_player,quick_to_win_player)

## A player that uses alpha-beta and better_evaluate:
#"""your_player = lambda board: run_search_function(board,
#                                                search_fn=alpha_beta_search,
#                                                eval_fn=better_evaluate,
#                                                timeout=5)"""

#your_player = lambda board: alpha_beta_search(board, depth=4,
#                                              eval_fn=better_evaluate)

## Uncomment to watch your player play a game:
#run_game(your_player, your_player)

## Uncomment this (or run it in the command window) to see how you do
#on the tournament that will be graded.

### ALPHA BETA WITH BASIC #########
#run_game(your_player, basic_player)

## These three functions are used by the tester; please don't modify them!
def run_test_game(player1, player2, board):
    assert isinstance(globals()[board], ConnectFourBoard), "Error: can't run a game using a non-Board object!"
    return run_game(globals()[player1], globals()[player2], globals()[board])
    
def run_test_search(search, board, depth, eval_fn):
    assert isinstance(globals()[board], ConnectFourBoard), "Error: can't run a game using a non-Board object!"
    return globals()[search](globals()[board], depth=depth,
                             eval_fn=globals()[eval_fn])

## This function runs your alpha-beta implementation using a tree as the search
## rather than a live connect four game.   This will be easier to debug.
def run_test_tree_search(search, board, depth):
    return globals()[search](globals()[board], depth=depth,
                             eval_fn=tree_searcher.tree_eval,
                             get_next_moves_fn=tree_searcher.tree_get_next_move,
                             is_terminal_fn=tree_searcher.is_leaf)

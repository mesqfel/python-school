from __future__ import print_function
import os
import random


def display_board(board):
	os.system('clear')
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

def player_input():
	marker = ''
	while not (marker == 'O' or marker == 'X'):
		marker = raw_input('Do you want to be X or O? ').upper()

		if (marker != 'X' and marker != 'O'):
			print('Chose X or O')

	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')
	

def place_marker(board, marker, position):
	board[position] = marker

def win_check(board, mark):

	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
		(board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
		(board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
		(board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
		(board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
		(board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
		(board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
		(board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
	players = ['X', 'O']
	return players[random.randint(0,1)]

def space_check(board, position):
	return board[position] != 'X' and board[position] != 'O'

def full_board_check(board):

	for x in xrange(1,10):
		if (board[x] != 'X' and board[x] != 'O'):
			return False

	return True

def player_choice(board):
	available = False
	
	while not (available):
		position = input('Chose a position from 1-9 to place your marker? ')
		available = space_check(board, position)
		if not available:
			print('Position not available.')

	return position

def replay():
	replay = ''
	while not (replay == 'Y' or replay == 'N'):
		replay = raw_input('Do you want to play again? (Y/n) ').upper()

		if (replay != 'Y' and replay != 'N'):
			print('Chose Y or n')

	if(replay == 'Y'):
		return True

	return False

def change_player(marker):
	if(marker == 'X'):
		return 'O'

	return 'X'

def print_player_turn(marker):
	print('Player '+marker+' turn.')

gameOn = True

while (gameOn):
	board = ['', ' ',' ',' ',' ',' ',' ',' ',' ',' ']
	display_board(board)
	players = player_input()
	currPlayer = choose_first()
	print_player_turn(currPlayer)
	position = player_choice(board)
	place_marker(board, currPlayer, position)
	display_board(board)

	playerWin = False
	while ((not playerWin) and (not full_board_check(board))):
		currPlayer = change_player(currPlayer)
		print_player_turn(currPlayer)
		position = player_choice(board)
		place_marker(board, currPlayer, position)
		display_board(board)
		playerWin = win_check(board, currPlayer)

	if (not playerWin):
		print('+++++ DRAW +++++')
	else:
		print('+++++ Player '+currPlayer+' WON +++++')

	gameOn = replay()

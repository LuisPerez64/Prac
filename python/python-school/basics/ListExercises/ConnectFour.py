'''
Implementing the game connect four. Further list comprehension, and use some 
of the built in tools to make the game funner. No AI as of yet, implies two players.
Will extend, and place in random ones once AI is set. Basically tic tac toe, which will be built
as well. Dimensions of the board are 7 across by 6 wide
'''
import re
def printGrid(grid):
    for x in grid:
        for y in x:
            print('{:^3}'.format(y), end=' ')
        print('\n')
    
def playerTurn(grid,symbol, slot):
    # Don't allow if at top, and there's something there already
    if grid[0][slot] != '*':
            slot=int(input('Can\'t fit in that slot. It\'s filled. Pick another.'))
            playerTurn(grid, symbol, slot)
            return
        
    for ind,inp in enumerate(grid[:-1]): 
        # if next drop is an asterisk, fall through
        if grid[ind+1][slot] == '*' and ind+2 != len(grid):
            continue            
        print('Boo')
        # have to go +1 else it'll be overlapping the last played symbol.
        if grid[ind+1][slot] == '*':
            grid[ind+1][slot]=symbol
        else:
            grid[ind][slot]=symbol
        printGrid(grid)
        break

# No shortcuts, just brute force check... Will change if moved to randomOnes
# Not as simple as tic-tac-toe... Finite space in that
# better manner of handling is not treating it as the grid being placed, but a matrix itself.
# Holds a list of two possibilities. One X one O. if contiguos along either the x or y, when sorted
# then that's a win. The diagnal check would be hellish...
def checkWinner(grid, symbol):
    winner=None
    
    # Pythonic Way
    # Convert the vertical slices to a list of lists. Easier to manipulate
    # Look into this rotation... Not sure why it's working and it's logic makes weird sense.
    vertGrid=[[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]
    for i in vertGrid:
        # Take the lists individually, convert to a string, try and find 4 in a row
        inp=''.join(i).find(symbol*4)
        if inp != -1:
            winner=True

    # Brute force
    for hori in grid:
        horiFirst=hori[0]
        horiCount=0
        for x in hori[1:]:
            if x == horiFirst and x is not '*':
                horiCount+=1
            else:
                horiCount=0
                horiFirst=x
            if horiCount == 3:
                winner=True
                indCount=0
                break
        if winner:
            break
    return winner


def main():
    player=0
    pieces=['O','X']
    grid=[['*' for x in range(7)] for x in range(6)]
    print('''Welcome to connect four.  
All you have to do is pick a slot to drop the piece in. Simple right?''')
    while True:
        slot=int(input('Player {0} place your {1} Pick a slot:'.format(player+1, pieces[player])))
        playerTurn(grid,pieces[player],slot)
        
        winner=checkWinner(grid, pieces[player])
        if winner:
            print('Congratulations player {0}. You\'ve won.'.format(player+1))
            break
        player=(player+1)%2
if __name__ == '__main__':
    main()

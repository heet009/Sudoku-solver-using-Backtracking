import pygame
import sys

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_SIZE = (540, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Solver")

# Define the font
font = pygame.font.SysFont(None, 40)

# Sudoku board
board = [
    [6, 0, 8, 0, 0, 3, 0, 2, 4],
    [4, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 8, 0],
    [8, 6, 0, 4, 7, 0, 0, 3, 0],
    [0, 7, 4, 1, 6, 2, 8, 9, 5],
    [1, 0, 0, 5, 0, 0, 0, 0, 7],
    [2, 0, 6, 0, 4, 0, 1, 0, 0],
    [0, 4, 3, 8, 0, 0, 6, 0, 0],
    [0, 8, 0, 7, 2, 6, 9, 0, 0]
]

# Function to draw the board
def draw_board():
    screen.fill(WHITE)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                pygame.draw.rect(screen, GRAY, (j * 60, i * 60, 60, 60))
                text = font.render(str(board[i][j]), True, BLACK)
                screen.blit(text, (j * 60 + 20, i * 60 + 20))
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, (0, i * 60), (540, i * 60), 3)
            pygame.draw.line(screen, BLACK, (i * 60, 0), (i * 60, 540), 3)
        else:
            pygame.draw.line(screen, GRAY, (0, i * 60), (540, i * 60))
            pygame.draw.line(screen, GRAY, (i * 60, 0), (i * 60, 540))

# Function to solve Sudoku
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            draw_board()
            pygame.display.update()
            pygame.time.delay(100)  # Add a small delay to visualize each move

            if solve(bo):
                return True

            bo[row][col] = 0
            draw_board()
            pygame.display.update()
            pygame.time.delay(100)  # Add a small delay to visualize each move

    return False

# Function to check if a move is valid
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

# Function to find an empty cell
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

# Main loop
def main():
    draw_board()
    pygame.display.update()
    solve(board)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()

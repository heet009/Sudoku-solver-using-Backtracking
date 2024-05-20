import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_SIZE = (600, 680)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Solver")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

# Define the font
font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

# Sudoku board
#board = [
#    [7, 8, 0, 4, 0, 0, 1, 2, 0],
#    [6, 0, 0, 0, 7, 5, 0, 0, 9],
#    [0, 0, 0, 6, 0, 1, 0, 7, 8],
#    [0, 0, 7, 0, 4, 0, 2, 6, 0],
#    [0, 0, 1, 0, 5, 0, 9, 3, 0],
#    [9, 0, 4, 0, 6, 0, 0, 0, 5],
#    [0, 7, 0, 3, 0, 0, 0, 1, 2],
#    [1, 2, 0, 0, 0, 7, 4, 0, 0],
#    [0, 4, 9, 2, 0, 6, 0, 0, 7]
#]

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
    # Calculate the position to center the Sudoku board
    sudoku_width = 9 * 60
    sudoku_height = 9 * 60
    x_pos = (WINDOW_SIZE[0] - sudoku_width) // 2
    y_pos = (WINDOW_SIZE[1] - sudoku_height) // 2
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                if board[i][j] == original_board[i][j]:
                    pygame.draw.rect(screen, BLUE, (x_pos + j * 60 + 5, y_pos + i * 60 + 5, 50, 50))
                else:
                    pygame.draw.rect(screen, GRAY, (x_pos + j * 60 + 5, y_pos + i * 60 + 5, 50, 50))
                text = font.render(str(board[i][j]), True, WHITE)
                text_rect = text.get_rect(center=(x_pos + j * 60 + 30, y_pos + i * 60 + 30))
                screen.blit(text, text_rect)
    for i in range(10):
        line_color = BLACK if i % 3 == 0 else GRAY
        pygame.draw.line(screen, line_color, (x_pos, y_pos + i * 60), (x_pos + sudoku_width, y_pos + i * 60), 3)
        pygame.draw.line(screen, line_color, (x_pos + i * 60, y_pos), (x_pos + i * 60, y_pos + sudoku_height), 3)

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
            display_time()
            pygame.display.update()
            pygame.time.delay(100)  # Add a small delay to visualize each move

            if solve(bo):
                return True

            bo[row][col] = 0
            draw_board()
            display_time()
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

# Function to display elapsed time
def display_time():
    current_time = time.time() - start_time
    text = small_font.render("Time: " + format_time(current_time), True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, 580))
    text_rect.y += 50
    screen.blit(text, text_rect)

# Function to format time as minutes and seconds
def format_time(secs):
    sec = int(secs % 60)
    minutes = int(secs // 60)
    return "{:02}:{:02}".format(minutes, sec)

# Make a copy of the original board
original_board = [row[:] for row in board]

button_font = pygame.font.SysFont(None, 30)
button_text = button_font.render("Solve Puzzle", True, BLACK)
button_rect = button_text.get_rect(center=(WINDOW_SIZE[0] // 2, 580))
button_rect.y += 80

# Main loop
def main():
    global start_time
    start_time = None
    draw_board()
    pygame.display.update()

    solving = False

    #solve(board)

    # Event loop to keep the window open
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    solving = True
                    start_time = time.time()
                    solve(board)

        screen.blit(button_text, button_rect)

        #if solving:
            #display_time()

        pygame.display.update()

if __name__ == "__main__":
    main()

import pygame
import sys

# initialize pygame module
pygame.init()

# top display of the grid board
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku 3x3")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# fonts
font = pygame.font.Font(None, 60)

# creating a 3x3 grid with pre-filled numbers (0 means empty and needs to be filled)
grid = [
    [0, 2, 0],
    [0, 0, 3],
    [1, 0, 0]
]

# solution grid to check for correct completion
solution_grid = [
    [3, 2, 1],
    [1, 3, 2],
    [1, 3, 2]
]

# function to draw the grid
def draw_grid():
    screen.fill(WHITE)

    # drawing horizontal and vertical lines to create a 3x3 grid
    for x in range(1, 3):
        pygame.draw.line(screen, BLACK, (x * 100, 0), (x * 100, 300), 2)
        pygame.draw.line(screen, BLACK, (0, x * 100), (300, x * 100), 2)

    # drawing numbers
    for row in range(3):
        for col in range(3):
            if grid[row][col] != 0:
                text = font.render(str(grid[row][col]), True, BLACK)  # rendering the number as text needed in pygame
                screen.blit(text, (col, row))

# function to insert numbers into the grid
def insert_number(row, col, num):
    if grid[row][col] == 0:  # Allow insertion only if the cell is empty
        grid[row][col] = num
        
# function to check if the grid matches the solution
def check_solution():
    for row in range(3):
        for col in range(3):
            if grid[row][col] != solution_grid[row][col]:
                return False
    return True

# creating a flag to indicate if the puzzle is solved
puzzle_solved = False

# game loop
running = True
while running:
    draw_grid()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // 100, x // 100
            print(f"Clicked row {row}, col {col}")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                insert_number(row, col, 1)
            if event.key == pygame.K_2:
                insert_number(row, col, 2)
            if event.key == pygame.K_3:
                insert_number(row, col, 3)

            if not puzzle_solved and check_solution():
            print("Congratulations! The puzzle is correct.")
            puzzle_solved = True  # Set to True to prevent further checks

import pygame
from collections import deque

# Constants
GRID_SIZE = 20
CELL_SIZE = 30
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BFS Pathfinding")

# Create a grid
grid = [
    [0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)
]  # 0 = walkable, 1 = obstacle
start = None
end = None


# BFS function
def bfs(start, end):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Return reversed path

        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            neighbor = (x + dx, y + dy)
            if (
                0 <= neighbor[0] < GRID_SIZE
                and 0 <= neighbor[1] < GRID_SIZE
                and neighbor not in visited
                and grid[neighbor[0]][neighbor[1]] == 0
            ):  # If walkable
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current
    return []  # Return empty if no path found


# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw the grid
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            color = WHITE if grid[x][y] == 0 else BLACK
            pygame.draw.rect(
                screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0
            )
            pygame.draw.rect(
                screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
            )

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            grid_x, grid_y = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE

            if not start:
                start = (grid_x, grid_y)  # Set starting point
            elif not end:
                end = (grid_x, grid_y)  # Set ending point
            else:
                grid[grid_x][grid_y] = (
                    1 if grid[grid_x][grid_y] == 0 else 0
                )  # Toggle obstacle
            if start and end:
                path = bfs(start, end)  # Find path

    # Draw the start and end points
    if start:
        pygame.draw.rect(
            screen,
            GREEN,
            (start[0] * CELL_SIZE, start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            0,
        )
    if end:
        pygame.draw.rect(
            screen,
            RED,
            (end[0] * CELL_SIZE, end[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            0,
        )

    # Draw the path
    if start and end and "path" in locals() and path:
        for x, y in path:
            pygame.draw.rect(
                screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0
            )

    pygame.display.flip()

pygame.quit()

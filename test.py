import pygame
import random
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
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BFS Pathfinding with Obstacles")

# Create a grid
grid = [
    [0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)
]  # 0 = walkable, 1 = obstacle
start = None
end = None
moving_obstacles = []
path = []
obstacle_move_frequency = 100  # Move obstacles every 100 frames
frame_count = 0
score = 0


# BFS function with visualization
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
                # Visualize BFS expansion
                pygame.draw.rect(
                    screen,
                    YELLOW,
                    (
                        neighbor[0] * CELL_SIZE,
                        neighbor[1] * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE,
                    ),
                )
                pygame.display.flip()
                pygame.time.delay(30)  # Delay for visualization

    return []  # Return empty if no path found


# Move obstacles randomly
def move_obstacles():
    global moving_obstacles
    for i, obstacle in enumerate(moving_obstacles):
        new_position = get_random_position()
        if is_valid_position(new_position):
            grid[obstacle[0]][obstacle[1]] = 0  # Clear old position
            grid[new_position[0]][new_position[1]] = 1  # Set new position
            moving_obstacles[i] = new_position  # Update obstacle position


# Get a random valid position
def get_random_position():
    return (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))


# Check if a position is valid
def is_valid_position(pos):
    x, y = pos
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and grid[x][y] == 0


# Add some random moving obstacles
for _ in range(5):  # Adjust number of obstacles
    pos = get_random_position()
    if grid[pos[0]][pos[1]] == 0:
        grid[pos[0]][pos[1]] = 1
        moving_obstacles.append(pos)

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
                if path:
                    score = len(path)  # Score based on path length

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
    if start and end and path:
        for x, y in path:
            pygame.draw.rect(
                screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0
            )

    # Display the score
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Move obstacles periodically
    frame_count += 1
    if frame_count % obstacle_move_frequency == 0:
        move_obstacles()

    pygame.display.flip()

pygame.quit()

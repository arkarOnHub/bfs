import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Load sprite sheet and set up frames
sprite_sheet = pygame.image.load("dia1.png").convert_alpha()
sprite_width, sprite_height = 64, 64  # Size of each frame
frames = [
    sprite_sheet.subsurface((i * sprite_width, 0, sprite_width, sprite_height))
    for i in range(4)
]

# Animation variables
current_frame = 0
frame_speed = 0.1  # Adjust speed
last_update = pygame.time.get_ticks()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update animation
    now = pygame.time.get_ticks()
    if now - last_update > 100:  # Update every 100 ms
        current_frame = (current_frame + 1) % len(frames)
        last_update = now

    # Draw the current frame
    screen.fill((255, 255, 255))  # Clear screen with white
    screen.blit(
        frames[current_frame], (width // 2, height // 2)
    )  # Draw sprite in the center
    pygame.display.flip()  # Update display

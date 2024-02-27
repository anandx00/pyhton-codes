import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
WINDOW_TITLE = 'Clock and Timer'
WINDOW_BG_COLOR = (255, 255, 255)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Fonts
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Colors
BLACK = (0, 0, 0)

# Clock variables
clock = pygame.time.Clock()
running = True

# Timer variables
timer_running = False
start_time = None
timer_duration = 0
time_left = 0

def draw_clock():
    current_time = time.strftime("%H:%M:%S %p")
    text_surface = font.render(current_time, True, BLACK)
    window.blit(text_surface, (50, 50))

def draw_timer():
    global time_left
    if timer_running:
        time_left = timer_duration - (time.time() - start_time)
        if time_left <= 0:
            time_left = 0
            stop_timer()
    minutes, seconds = divmod(int(time_left), 60)
    timer_text = f"Timer: {minutes:02d}:{seconds:02d}"
    text_surface = font.render(timer_text, True, BLACK)
    window.blit(text_surface, (50, 150))

def start_timer(duration):
    global timer_running, start_time, timer_duration
    timer_running = True
    start_time = time.time()
    timer_duration = duration

def stop_timer():
    global timer_running
    timer_running = False

# Main loop
while running:
    window.fill(WINDOW_BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_t:
                start_timer(60)  # Start timer for 60 seconds

    draw_clock()
    draw_timer()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

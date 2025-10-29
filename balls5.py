import pygame

# Define some colors
BACKGROUND_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.radius = 10
        self.color = PLAYER_COLOR
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        # Constrain position within the screen bounds
        self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Player Movement")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create the player
    player = Player()

    # Loop until the user clicks the close button or ESC.
    done = False
    while not done:
        # Limit number of frames per second
        clock.tick(60)

        # Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        # Get pressed keys
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        # Draw the player
        pygame.draw.circle(screen, player.color, (player.x, player.y), player.radius)

        # Update the screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()

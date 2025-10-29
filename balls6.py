import pygame, random

# Define some colors
BACKGROUND_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.randomize()

    def randomize(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Generate a random color
        self.dx = random.randint(-3,3)
        self.dy = random.randint(-3,3)
        while self.dx == 0 and self.dy == 0: # Ensure the ball moves
            self.dx = random.randint(-3,3)
            self.dy = random.randint(-3,3)

    def move(self):
        # Update position
        self.x += self.dx
        self.y += self.dy

        # Check for collisions with walls
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.dx *= -1  # Reverse horizontal direction
        if self.y - self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:
            self.dy *= -1  # Reverse vertical direction

        # Constrain position (to prevent getting stuck outside bounds)
        self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))

class Player(Ball):
    def __init__(self):
        super().__init__(SCREEN_WIDTH // 2, SCREEN_WIDTH // 2, 10)
        self.color = PLAYER_COLOR
        self.speed = 5

    def move(self, keys):
        self.dx = self.dy = 0 # Reset movement
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
    pygame.display.set_caption("Ball Game")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    balls = [Ball(100 * i, 100 * i, 10 * i) for i in range(1, 5)]
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
                elif event.key == pygame.K_r:
                    for ball in balls:
                        ball.randomize()
                elif event.key == pygame.K_PLUS:
                    balls.append(Ball(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50), random.randint(10, 20)))

        # Get pressed keys
        keys = pygame.key.get_pressed()

        # Move all balls and the player
        for ball in balls:
            ball.move()
        player.move(keys)
        
        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        for ball in balls:
            pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)
            
        # Draw the player
        pygame.draw.circle(screen, player.color, (player.x, player.y), player.radius)

        # Update the screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()

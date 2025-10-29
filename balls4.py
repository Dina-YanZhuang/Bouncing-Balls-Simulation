import pygame,random


# Define some colors
BACKGROUND_COLOR = (255, 255, 255)


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

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Balls")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    balls = []
    for i in range(1, 5):
        balls.append(Ball(100*i, 100*i, 10*i))
        #balls.append(Ball(100*i*random.randint(1,2), 100*i))


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

        # Ball Movement and Wall Collision
        for ball in balls:
            # Update position
            ball.x += ball.dx
            ball.y += ball.dy

            # Check for collisions with walls
            if ball.x - ball.radius <= 0 or ball.x + ball.radius >= SCREEN_WIDTH:
                ball.dx *= -1  # Reverse horizontal direction
            if ball.y - ball.radius <= 0 or ball.y + ball.radius >= SCREEN_HEIGHT:
                ball.dy *= -1  # Reverse vertical direction

            # Constrain position (to prevent getting stuck outside bounds)
            ball.x = max(ball.radius, min(SCREEN_WIDTH - ball.radius, ball.x))
            ball.y = max(ball.radius, min(SCREEN_HEIGHT - ball.radius, ball.y))
        # Draw everything
        screen.fill(BACKGROUND_COLOR)

        for ball in balls:
            pygame.draw.circle(screen, ball.color,
                               (ball.x, ball.y), ball.radius)

        # Update the screen
        pygame.display.flip()

    # Close everything down
    pygame.quit()


def constrain(small, value, big):
    """Return a new value which isn't smaller than small or larger than big"""
    # TODO: Should use "small" as well.
    return min(value, big)


if __name__ == "__main__":
    main()

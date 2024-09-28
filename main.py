import pygame
import math 

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pi In Collisions")

class Block:
    def __init__(self, x, mass, velocity, color, size_scaling = 1):
        self.x = x
        self.mass = mass
        self.velocity = velocity
        self.size = mass * size_scaling
        self.color = color

    def move(self):
        self.x += self.velocity

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, HEIGHT - self.size, self.size, self.size))

mass_ratio = 10000
size_scaling = 100

block_one = Block(x = 200, mass = 1, velocity = 0, color = (0, 128, 255), size_scaling = 20)
block_two = Block(x = 500, mass = mass_ratio, velocity = -0.5, color = (255, 0, 0), size_scaling = .005)

def elastic_collision(b1, b2):
    v1 = b1.velocity
    v2 = b2.velocity

    b1.velocity = ((b1.mass - b2.mass) * v1 + 2 * b2.mass * v2) / (b1.mass + b2.mass)
    b2.velocity = ((b2.mass - b1.mass) * v2 + 2 * b1.mass * v1) / (b1.mass + b2.mass)

def wall_collision(block):
    if block.x <= 0:
        block.velocity *= -1
        return True 
    return False
    
collision_count = 0

running = True

while running: 
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    block_one.move()
    block_two.move()

    if block_one.x + block_one.size >= block_two.x:
        elastic_collision(block_one, block_two)
        collision_count += 1
        print(f"Collisions : {collision_count}")

    if wall_collision(block_one):
        collision_count += 1
        print(f"Collisions = {collision_count}")
    
    if wall_collision(block_two):
        collision_count += 1
        print(f"Collisions = {collision_count}")

    block_one.draw()
    block_two.draw()

    pygame.display.update()
    pygame.time.delay(5)

pygame.quit()

        
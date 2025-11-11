# donkey_clone.py
# Clone inspiré de Donkey Kong — version corrigée : saut plus haut + saut variable (press & hold).
# Nécessite pygame (pip install pygame)

import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 640, 720
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# Colors
BG = (20, 20, 40)
PLATFORM_COLOR = (200, 100, 40)
PLAYER_COLOR = (50, 200, 200)
BARREL_COLOR = (170, 90, 30)
LADDER_COLOR = (180, 180, 60)
GOAL_COLOR = (240, 200, 0)

# Physics tuning (modifiables)
GRAVITY = 0.48            # gravité générale (réduite pour plus d'air-time)
JUMP_VELOCITY = -15.0    # vitesse initiale du saut (plus négatif = plus haut)
JUMP_CUT_MULT = 0.45     # multiplicateur appliqué si on relâche la touche rapidement (raccourcit le saut)
MAX_FALL_SPEED = 18.0    # vitesse de chute maximale

# Simple level definition: list of platforms (x,y,w,h), ladders (x,y,w,h)
platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),     # ground
    pygame.Rect(40, 560, 560, 16),              # platform 1
    pygame.Rect(20, 440, 380, 16),              # platform 2
    pygame.Rect(220, 320, 400, 16),             # platform 3
    pygame.Rect(40, 200, 360, 16),              # platform 4 (near top)
]

ladders = [
    pygame.Rect(300, 320, 40, 240),
    pygame.Rect(80, 200, 40, 360),
    pygame.Rect(520, 200, 40, 40),
]

goal_rect = pygame.Rect(WIDTH - 90, 160 - 32, 60, 60)

class Player:
    def __init__(self):
        self.w = 28; self.h = 36
        self.x = 60
        self.y = HEIGHT - 40 - self.h
        self.vx = 0.0
        self.vy = 0.0
        self.on_ground = False
        self.on_ladder = False
        self.lives = 3
        self.score = 0
        self.invuln = 0  # frames invuln
        # pour saut variable
        self.want_jump = False       # si la touche de saut est actuellement pressée
        self.jump_pressed_last = False

    @property
    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.w, self.h)

    def update(self, keys):
        speed = 3.6
        # horizontal movement
        self.vx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = speed

        # ladder detection
        self.on_ladder = False
        for ladder in ladders:
            if self.rect.centerx > ladder.left and self.rect.centerx < ladder.right:
                if (self.rect.bottom > ladder.top and self.rect.top < ladder.bottom):
                    self.on_ladder = True

        jump_key = keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]

        # Ladder behavior: climb without gravity
        if self.on_ladder:
            if jump_key:
                # allow to jump off ladder
                if not self.jump_pressed_last:
                    # initiate small jump from ladder
                    self.vy = JUMP_VELOCITY * 0.8
                    self.on_ground = False
            else:
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.vy = -2.6
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.vy = 2.6
                else:
                    self.vy = 0
        else:
            # gravity
            self.vy += GRAVITY
            # cap fall speed
            if self.vy > MAX_FALL_SPEED:
                self.vy = MAX_FALL_SPEED

            # jump initiation (only if on ground)
            if jump_key and self.on_ground and not self.jump_pressed_last:
                self.vy = JUMP_VELOCITY
                self.on_ground = False
                self.want_jump = True

            # variable jump cut: if player releases jump while still moving upward, shorten jump
            if not jump_key and self.jump_pressed_last:
                # if still going up, cut the upward velocity
                if self.vy < 0:
                    self.vy *= JUMP_CUT_MULT
                self.want_jump = False

        # apply movement
        self.x += self.vx
        self.y += self.vy

        # world bounds
        if self.x < 0: self.x = 0
        if self.x + self.w > WIDTH: self.x = WIDTH - self.w
        if self.y > HEIGHT + 200:
            # fell off
            self.respawn()

        # collisions with platforms
        self.on_ground = False
        r = self.rect
        for p in platforms:
            if r.colliderect(p):
                # coming from top
                if self.vy > 0 and r.bottom - self.vy <= p.top + 6:
                    self.y = p.top - self.h
                    self.vy = 0
                    self.on_ground = True
                    self.want_jump = False
                # hitting head
                elif self.vy < 0 and r.top - self.vy >= p.bottom - 6:
                    self.y = p.bottom
                    self.vy = 0
                else:
                    # simple horizontal push-out
                    if self.vx > 0:
                        self.x = p.left - self.w
                    elif self.vx < 0:
                        self.x = p.right

        if self.invuln > 0:
            self.invuln -= 1

        # update last-press state
        self.jump_pressed_last = jump_key

    def draw(self, surf):
        r = self.rect
        if self.invuln and (self.invuln // 6) % 2 == 0:
            color = (255, 255, 255)
        else:
            color = PLAYER_COLOR
        pygame.draw.rect(surf, color, r)
        eye_color = (10, 10, 30)
        pygame.draw.circle(surf, eye_color, (int(self.x+self.w*0.7), int(self.y+self.h*0.35)), 3)

    def respawn(self):
        self.x = 60
        self.y = HEIGHT - 40 - self.h
        self.vx = 0
        self.vy = 0
        self.lives -= 1
        self.invuln = FPS * 2  # 2 seconds invuln

class Barrel:
    def __init__(self, x, y, direction=1):
        self.r = 16
        self.x = x
        self.y = y
        self.vx = 2.2 * direction
        self.vy = 0
        self.alive = True

    @property
    def rect(self):
        return pygame.Rect(int(self.x - self.r), int(self.y - self.r), self.r*2, self.r*2)

    def update(self):
        # simple rolling physics with gravity and platform collisions
        self.vy += GRAVITY * 0.45
        self.x += self.vx
        self.y += self.vy

        # bounce off world bounds horizontally
        if self.x - self.r < 0:
            self.x = self.r
            self.vx = -self.vx
        if self.x + self.r > WIDTH:
            self.x = WIDTH - self.r
            self.vx = -self.vx

        r = self.rect
        on_platform = False
        for p in platforms:
            if r.colliderect(p):
                # land on top
                if self.vy > 0 and r.bottom - self.vy <= p.top + 6:
                    self.y = p.top - self.r
                    self.vy = 0
                    on_platform = True
                # bumping head
                elif self.vy < 0 and r.top - self.vy >= p.bottom - 6:
                    self.y = p.bottom + self.r
                    self.vy = 0
                else:
                    if self.vx > 0:
                        self.x = p.left - self.r*2
                        self.vx = -abs(self.vx)
                    elif self.vx < 0:
                        self.x = p.right + self.r
                        self.vx = abs(self.vx)
        # if on platform, occasionally change direction
        if on_platform:
            if random.random() < 0.01:
                self.vx *= -1

        if self.y > HEIGHT + 100:
            self.alive = False

    def draw(self, surf):
        pygame.draw.circle(surf, BARREL_COLOR, (int(self.x), int(self.y)), self.r)
        pygame.draw.circle(surf, (120, 50, 10), (int(self.x-5), int(self.y-5)), 6)

def draw_level(surf):
    surf.fill(BG)
    for p in platforms:
        pygame.draw.rect(surf, PLATFORM_COLOR, p)
        pygame.draw.rect(surf, (30,20,10), p, 2)
    for l in ladders:
        pygame.draw.rect(surf, LADDER_COLOR, l)
        rung_h = 8
        step = 20
        for ry in range(l.top, l.bottom, step):
            pygame.draw.rect(surf, (80,60,20), (l.left, ry, l.width, rung_h))
    pygame.draw.rect(surf, GOAL_COLOR, goal_rect)
    pygame.draw.rect(surf, (200,140,0), goal_rect, 2)
    cx, cy = goal_rect.center
    pygame.draw.circle(surf, (255,120,120), (cx, cy), 16)
    pygame.draw.rect(surf, (120,40,40), (cx-6, cy+6, 12, 8))

def main():
    player = Player()
    barrels = []
    barrel_timer = 0
    level_time = 0
    running = True

    announcer_msg = ""
    announcer_timer = 0

    while running:
        dt = clock.tick(FPS)
        level_time += dt
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # spawn barrels periodically (from top-left)
        barrel_timer += dt
        spawn_interval = max(700, 2000 - (player.score * 12))
        if barrel_timer > spawn_interval:
            barrel_timer = 0
            spawn_x = 120
            spawn_y = 160
            direction = random.choice([1, -1])
            b = Barrel(spawn_x, spawn_y, direction=direction)
            barrels.append(b)

        # update
        player.update(keys)
        for b in barrels:
            b.update()

        # barrel-player collisions
        if player.invuln == 0:
            for b in barrels:
                if b.rect.colliderect(player.rect):
                    player.respawn()
                    announcer_msg = "Ouch! Perdu une vie."
                    announcer_timer = FPS * 2
                    break

        # remove dead barrels
        barrels = [b for b in barrels if b.alive]

        # check reaching goal
        if player.rect.colliderect(goal_rect):
            player.score += 500
            announcer_msg = "Niveau terminé ! +500 pts"
            announcer_timer = FPS * 3
            player.x, player.y = 60, HEIGHT - 40 - player.h
            barrels.clear()

        # scoring over time
        if level_time % 1000 < dt:
            player.score += 5

        # draw
        draw_level(screen)
        for b in barrels:
            b.draw(screen)
        player.draw(screen)

        # HUD
        hud_y = 8
        score_surf = font.render(f"Score: {player.score}", True, (240,240,240))
        lives_surf = font.render(f"Vies: {player.lives}", True, (240,240,240))
        screen.blit(score_surf, (10, hud_y))
        screen.blit(lives_surf, (WIDTH - 100, hud_y))

        # announcer
        if announcer_timer > 0:
            announcer_timer -= 1
            msg_surf = font.render(announcer_msg, True, (255, 220, 120))
            screen.blit(msg_surf, (WIDTH//2 - msg_surf.get_width()//2, 40))

        # game over
        if player.lives <= 0:
            over_surf = font.render("GAME OVER - Appuie sur R pour rejouer ou Echap pour quitter", True, (255,180,180))
            screen.blit(over_surf, (WIDTH//2 - over_surf.get_width()//2, HEIGHT//2 - 10))
            pygame.display.flip()
            waiting = True
            while waiting:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        pygame.quit(); sys.exit()
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_r:
                            player = Player()
                            barrels = []
                            barrel_timer = 0
                            level_time = 0
                            announcer_msg = ""
                            announcer_timer = 0
                            waiting = False
                        if ev.key == pygame.K_ESCAPE:
                            pygame.quit(); sys.exit()
                clock.tick(FPS)
            continue

        tip = "Déplacement: ← →  Saut: Espace / ↑ (maintenir pour sauter plus haut). Monter/Descendre: ↑ ↓ sur échelle."
        tip_surf = font.render(tip, True, (200,200,200))
        screen.blit(tip_surf, (10, HEIGHT - 26))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

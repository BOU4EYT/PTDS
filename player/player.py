import pygame as pg
class player:
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.heal_timer = 0
        self.heal_amount = 15
        self.heal_interval = 300
        self.speed = 5

    def move(self, direction):
        if direction == "up":
            pass
        elif direction == "down":
            pass
        elif direction == "left":
            pass
        elif direction == "right":
            pass

    def hotbar(self, item, slot):
        if slot == 1:
            pass
        elif slot == 2:
            pass

    def attack(self, target):
        pass

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        print("Player has died.")

    def heal(self): ##heal over time
        if self.health < 75:
            self.heal_timer += 1
            if self.heal_timer >= self.heal_interval:
                self.health = min(self.health + self.heal_amount, self.max_health)
                self.heal_timer = 0

    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.move("up")
        if keys[pg.K_s]:
            self.move("down")
        if keys[pg.K_a]:
            self.move("left")
        if keys[pg.K_d]:
            self.move("right")
        if keys[pg.K_1]:
            self.hotbar("item1", 1)
        if keys[pg.K_2]:
            self.hotbar("item2", 2)
        if keys[pg.mouse.get_pressed()[0]]:
            self.attack("target")

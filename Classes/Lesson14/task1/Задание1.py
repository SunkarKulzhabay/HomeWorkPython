# Задание 1
class Spaceship:
    def __init__(self, name="", health=10, position=0):
        self.name = name
        self.health = health
        self.position = position

    def moveLeft(self):
        self.position -= 1

    def moveRight(self):
        self.position += 1

    def wasHit(self):
        self.health -= 5
        if self.health <= 0:
            print("Извините, ваш корабль был сбит слишком много раз. Хотите сыграть еще раз?")
        else:
            print(f'У вас осталось {self.health} жизней')


falcon = Spaceship(name="Falcon")
falcon.moveLeft()
falcon.moveLeft()
falcon.moveRight()
print(falcon.position)


# Задание 2
class Fighter(Spaceship):
    def __init__(self, name="", health=10, position=0, weapon="", remainingFirePower=5):
        super().__init__(name, health, position)
        self.weapon = weapon
        self.remainingFirePower = remainingFirePower

    def fire(self):
        if self.remainingFirePower > 0:
            self.remainingFirePower -= 1
            print(f"Выстрел из {self.weapon}! Осталось боеприпасов: {self.remainingFirePower}")
        else:
            print("У вас больше нет оружейной мощности")


destroyer = Fighter(name="Destroyer", weapon="Лазер", remainingFirePower=10)
destroyer.moveRight()
print(destroyer.position)

# print(falcon.weapon)  # Ошибка! У falcon нет атрибута weapon,
# потому что Spaceship родитель и все данные от него вниз уходят по цепочке.


# Задание 3
class ShieldedShip(Fighter):
    def __init__(self, name="", health=10, position=0, weapon="", remainingFirePower=5, shieldStrength=25):
        super().__init__(name, health, position, weapon, remainingFirePower)
        self.shieldStrength = shieldStrength

    def wasHit(self):
        if self.shieldStrength > 0:
            self.shieldStrength -= 5
            print(f"Щит поглотил урон! Осталось прочности щита: {self.shieldStrength}")
        else:
            super().wasHit()


defender = ShieldedShip(name="Defender", weapon="Cannon", remainingFirePower=10)
defender.moveRight()
defender.fire()

defender.wasHit()
print(f"Shield: {defender.shieldStrength}, Health: {defender.health}")

defender.wasHit()
print(f"Shield: {defender.shieldStrength}, Health: {defender.health}")

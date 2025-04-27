class Device:
    def __init__(self, name, brand, model, power, guarantee):
        self.name = name
        self.brand = brand
        self.model = model
        self.power = power
        self.guarantee = guarantee

    def info(self):
        print(f'{self.name} - {self.brand}({self.model}).\n'
              f'Мощность - {self.power} Вт.\nГарантия - {self.guarantee}.')


class CoffeMachine (Device):
    def __init__(self, *args):
        super().__init__('Кофемашина', *args)

    def info(self):
        super().info()
        print('Автоматическая кофемашина DeLonghi ETAM 29.660.SB отличается компактными габаритами,'
               'благодаря чему она не займет много места на кухне.\n')


class Blender (Device):
    def __init__(self, *args):
        super().__init__('Блендер', *args)

    def info(self):
        super().info()
        print('Блендер стационарный Aceline SB-600A в лаконичном черном'
              'корпусе оснащен поворотным регулятором для выбора 1 из 2 скоростей.\n')


class MeatGrinder (Device):
    def __init__(self, *args):
        super().__init__('Мясорубка', *args)

    def info(self):
        super().info()
        print('Мясорубка Polaris PMG 2050 RUS в симпатичном фиолетово-серебристом корпусе' 
        'станет эффективным и неутомимым помощником для кухни,'
        'где любят готовить домашние полуфабрикаты впрок.\n')


DeLonghi = CoffeMachine('"DeLonghi"', 'ETAM 29.660.SB', 1450, '36 мес')
Aceline = Blender('"Aceline"', 'SB-600A', 600, '18 мес')
Polaris = MeatGrinder('"Polaris"', 'PMG 2050', 2000, '24 мес')

DeLonghi.info()
Aceline.info()
Polaris.info()

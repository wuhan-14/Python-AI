class Car:
    def __init__(self, brand, model, color, owner):
        self.brand = brand          
        self.model = model          
        self.color = color          

        self.__owner = owner          

    def start(self): 
        print(f'{self.brand} {self.model} 正在启动...')

    def run(self): 
        print(f'{self.__owner} : {self.brand} {self.model} 正在行驶...')
        self.__control_fuel()

    def stop(self):
        print(f'{self.brand} {self.model} 停止行驶...')

    def __control_fuel(self): 
        print(f'{self.brand} {self.model} 正在控制油门...')

    def get_owner(self):
        return self.__owner[0:1] + "**"


if __name__ == '__main__':
    car = Car('Audi', 'A6', '黑色', '涛哥')
    print(car.brand)
    print(car.model)
    print(car.color)

    print(car._Car__owner)
    car._Car__control_fuel()

    car.start()
    car.run()
    car.stop()
    print(car.get_owner())
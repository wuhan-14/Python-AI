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
class FuelCar(Car):
    pass

class ElectricCar(Car):
    pass

if __name__ == '__main__':
    c1 = FuelCar("BMW", "X5", "黑色", "张三")
    c1.start()
    c1.run()
    c1.stop()
    print(c1.brand)
    print(c1.get_owner())
    print(c1.model)
    print(c1.color)
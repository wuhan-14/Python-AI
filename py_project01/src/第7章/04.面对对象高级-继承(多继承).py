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

    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃料...')

class HuaweiAiDriving:
    def __init__(self, version="V1.0"):
        self.version = version

    def run(self):
        print(f'使用华为AI智能驾驶系统{self.version}正在行驶...')


class WenJieCar(Car, HuaweiAiDriving):
    def __init__(self, brand, model, color, owner, version = "V1.0"):
        Car.__init__(self, brand, model, color, owner)
        HuaweiAiDriving.__init__(self, version)

    def run(self):
        Car.run(self)
        HuaweiAiDriving.run(self)


if __name__ == '__main__':
    c = WenJieCar("BMW", "X5", "黑色", "张三", "V1.1")
    print(c.__dict__)

    print(WenJieCar.__mro__)
    print(WenJieCar.mro())
    print(HuaweiAiDriving.mro())

    c.run()
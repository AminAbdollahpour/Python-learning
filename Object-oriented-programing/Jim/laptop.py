from item import Item


class Laptop(Item):
    cpu_list = ['intel']
    gpu_list = ['gforce']

    def __init__(self, name, price, quantity, cpu: str, gpu: str, weight: float):
        super().__init__(name, price, quantity)
        self.__cpu = cpu
        self.__gpu = gpu
        self.weight = weight
        assert weight > 0, 'Weight of laptop cant be less or equal to zero.'
        assert cpu  in Laptop.cpu_list,'cpu 404'
        assert gpu  in Laptop.gpu_list,'gpu 404'

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        if value in Laptop.cpu_list:
            self.__cpu = value
        else:
            raise Exception(f'CPU {value} not found')

    @property
    def gpu(self):
        return self.__gpu

    @gpu.setter
    def gpu(self, value):
        if value in Laptop.gpu_list:
            self.__gpu = value
        else:
            raise Exception(f'GPU {value} not found')
    def __repr__(self):
        return f'{self.name}/{self.cpu}/{self.gpu}'

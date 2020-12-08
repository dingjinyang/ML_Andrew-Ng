class Gene:
    """
    Gene
    """

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        self.size = len(kwargs['data'])


class GA:
    def __init__(self, cross_rate, mutate_rate, gen_size, pop_size, min, max):
        """
        初始化参数，交叉率, 变异率, 繁殖代数, 种群大小, 最小值, 最大值
        """
        population = list()
        for i in range(gen_size):
            gen_info = list()
            
            

    def evaluate(self, geneinfo):
        """
        适应度函数
        """
        pass

    def selectBest(self, pop):
        """
        选择种群中最优个体
        """
        pass

    def selection(self, individuals, k):
        """
        从上一代中选择个体
        """
        pass

    def crossoperate(self, offspring):
        """
        交叉
        """
        pass

    def mutation(self, crossoff, bound):
        """
        变异
        """
        pass

    def GA_main(self):
        pass

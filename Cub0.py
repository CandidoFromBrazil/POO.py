class Calc_cubo:
    def __init__(self,valor):
        self.valor = valor
        print('\nObjeto criado')
    def Calcula_Cubo(self,):
        self.cubo = (self.valor * self.valor * self.valor)
        return 'Cubo calculado\n' + str(self.cubo) #Esse método 'retorna' um valor

vari = Calc_cubo(10)
print(vari.Calcula_Cubo())
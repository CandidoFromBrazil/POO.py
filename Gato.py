class gato:
    """Classe para trabalhar com gatos"""
    def __init__(self, nome): #metodo construtor/<self> faz referencia a classe(interna)
        """Inicializa a função(metodo), capiturando o nome do gato"""
        self.nome = nome #<nome> = parametro que o usuario vai passar, sendo passada para a variavel interna <self.nome>
        print(f'Seu gatinho se chama: {self.nome}')
    def peso_gato(self, peso): #primeiro metodo
        self.peso = peso
        if (self.peso > 5.0):
            print('Seu gato esta gordinho')
        elif self.peso > 3.5:
            print('Seu gato está no peso ideal')
        else:
            print('Seu gato está abaixo do peso')
    def _dieta_especial_gato(self): #metodo encapsulado, não aparece externamente á classe <para chamar, se faz o uso de outro metodo>
        self.msg = 'Tudo ok!'
        if (self.peso < 3.5):
            print('Aumente a ração do felino')
        if (self.peso > 3.5):
            print('Diminua a ração do felino')
        return self.msg #retornando <self.msg> de acordo com o if acentido
    def dados_gato(self): #metodo criado para poder "chamar" o metodo encapsulado <_dieta_especial_gato>
        print(f'\nO gato: {self.nome} , está pesando: {self.peso}kg')
        print(f'{self._dieta_especial_gato()}') #"chamando" o medodo encapsulado

        """Objeto invocando a classe, e seus metodos"""
nome_gato = input('Digite o nome do seu gato: ')
g1 = gato(nome_gato) #Atribuição da classe <gato> ao objeto <g1>
peso = float(input('Qual o peso do seu gato em Kg: '))
g1.peso_gato(peso) #objeto <g1> pedindo o uso do metodo <peso_gato>
g1.dados_gato() # "chama" a variavel encapsulada, + 'None' devido ao fato da variavel ser encapsulada <isso quando não está no mesmo projeto> (quando pedido o instanciamento do objeto, por outra aba[Teste.py])


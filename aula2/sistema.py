
def menu ():
    print ("="*45)
    print("Sistema do Café, chá e lasanha SENAI")
    print("="*45)
    print("1 - Criar um café :")
    print("2 - Listar os cafés :")
    print("3 - Qual o maior preço do café : ?")
    print("4 - Qual o preço mais barato")
    print("0 - Sair do sistema")

class Cafe:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def _str_(self):
        #.2f -> deixar somente dois numeros apos o ponto 
        return f"{self.nome} -R$ {self.preco:.2f}"  

cafes = []
     
while True:
    menu()
    opcao = int(input("Digite a opção desejada :")) 

    if opcao == 1:
        nome = input("Digite o nome do café :")
        preco = float(input("Digite o preço do café :"))

        novo_cafe = Cafe (nome, preco)   
        cafes.append(novo_cafe) #append adicionar um objeto na lista
    elif opcao == 2:
        # Listar os cafés
    
    #len -> Lenght -- Tamanho
        if len(cafes) ==0:
            print("Nenhum café cadastrado")
        else:
            #\n -- Quebrar linha
            print("\n---- Lista de Cafes----")
            #for -- repita
            for cafe in cafes:
                print(cafe)
    elif opcao == 3:
        #verificar o cafe com o maior preço 
        #cafes [0]--- Primeiro objeto
        mais_caro = cafes[0]
        for cafe in cafes:
            if cafe.preco > mais_caro.preco:
             mais_caro = cafe

        print(f"\n\nCafé mais caro : {mais_caro.nome}")
        print(f"Preço do café : {mais_caro.preco}")      
    elif opcao ==0:
        print("Saindo do sistema")
        break                

                













      



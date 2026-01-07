#%%
#para abrir um arquivo, utilizamos o "open()":
nome_arquivo = "historia.txt"
open_file = open(nome_arquivo)

# O print não mostra o conteúdo dentro do arquivo:
print(open_file)

#Para pegar o conteúdo dentro do arquivo, utilizamos o .read() da seguinte maneira:
conteudo = open_file.read()

#Exibir o conteúdo do arquivo:
print(conteudo)
#Após abrir o arquivo, é importante que a gente feche ele, assim ele não fica
open_file.close()



# %%
#Podemos acabar esquecendo de fechar o arquivo, então segue abaixo a forma mais comum e utilizável para leitura de arquivos python.
nome_arquivo = "historia.txt"
#With ele é como se fosse "Enquanto esse arquivo estiver aberto: leia o conteúdo.
#Isso faz com que o arquivo feche sozinho após o código sair do "With".
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

#Aqui o arquivo já é fechado automaticamente, saindo do With e exibindo seu conteúdo.
print(conteudo)
# %%
#Cria e escreve texto em um arquivo:
txt = "Meu nomvo arquivo\n" #\n faz ele pular para próxima linha. Assim o próximo comentário irá direto para linha 2.
txt2 = "Adicionando novo texto!!!"
nome_arquivo = "historia_2.txt"
with open(nome_arquivo,mode="w") as open_file:
    open_file.write(txt)

#Para adicionar dados de texto no arquivo, utilizamos "a" ao invés de "w"
with open(nome_arquivo,mode="a") as open_file:
    open_file.write

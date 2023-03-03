**> Trabalhando com dicionários**

1. Sao armazenados de forma não ordenada

2. Seus elementos possuem uma chave e um valor => chave: vai indexar um elemento no dicionário
   => valor: aceita listas, outros dicionários, inteiros, strings e etc.

3. SINTAXE: {'chave': 'valor'}



    **=> MANEIRAS DE CRIAR UM DICIONÁRIO:**

    1. maneira mais simples: 
        dicio = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

    2. UTILIZANDO A FUNÇÃO DICT: 
        dicio = dict(primeiro = 1, segundo = 2, terceiro = 3)

    3. UTILIZANDO A FUNÇÃO ZIP PARA CONCATENAR A chave:valor A UM ELEMENTO DO OBJETO dict: 
        dicio = dict(zip(['primeiro','segundo','terceiro'], [1,2,3]))

    4. UTILIZANDO LISTA DE *TUPLAS*
        dicio = dict([('primeiro',1),('segundo',2),('terceiro',3)])
        *tuplas*: > São listas estãticas
            > Ao inves de usarmos colchetes, usamos parênteses; 
            > São imutáveis
            > Não deixa alterar, adicionar ou excluir os elementos que estão dentro delas
            > "Para uma tupla de valor único, devemos sempre colocar uma vírgula (,) no final do valor, mesmo com os parênteses, ou o Python não interpretará como tupla."
            > Podemos utilizar listas dentro das tuplas

    5. *Com Dict Comprehensions!*
    > utiliza-se **for** e **in**
        {chave: valor for elemento in iteravel}

        dicio = {name: idx + 1 for idx in enumerate(('primeiro', 'segundo', 'terceiro'))}

    6. TRANSFORMAR UMA VARIÁVEL DO TIPO DICIONÁRIO EM DICIONÁRIO:
        dicio = dict({'primeiro':1, 'segundo': 2, 'terceiro': 3})



    **=> MANEIRAS DE ACESSAR UM DICIONÁRIO:**

    1. PODEMOS ACESSAR POR MEIO DA CHAVE: 
        dicio = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
        print(dicio['primeiro'])

    2. POR MEIO DE UM GET:
        print(dicio.get('primeiro'))

    **EXTRA**
    "Uma coisa interessante sobre esse método é que você pode definir um valor default, para o caso da chave não ser encontrada, exemplo:
        print(pessoa.get('peso', 'Chave não encontrada'))
        Como não existe nenhuma chave chamada 'peso', ele retorna:
        *Chave não encontrada*



    **=> ACESSANDO DICIONARIO DENTRO DE DICIONARIO**
    dicionario = {'m1': {'m2': 'olá mundo'}}
    print(dicionario['m1']['m2'])



    **=> OBTENDO CHAVES E VALORES**
    *CHAVES*
    Utilizar o método keys()
        dicio = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
        print(dicio.keys())

    *VALORES*
    Utilizar o método values()
        dicio = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
        print(dicio.values())



    **=> PERCORRENDO ELEMENTOS DO DICIONÁRIO**
    1. Podemos utilizar o keys()
        for chave in dicio.keys():
            print(f'Chave = {chave} e Valor = {dicio[chave]}')

    2. Podemos utilizar o values()
        for valor in dicio.values():
            print(f'Valor = {valor}')



    **=> PERCORRENDO AS CHAVES E VALORES DO DICIONÁRIO**
    1. Uma maneira de obte-los é usando o .items()
        print(dicio.items())

    2. Podemos utilizar o for:
        for chave, valor in dicio.items():
            print(f'Chave = {chave} e Valor = {valor}')

    3. Para conferirmos se a chave existe, podemos utilizar ifs: 
        if 'primeiro' in dicio:
            print(f"Como a chave desejada existe: {dicio[primeiro]}")



    **=> ADICIONANDO E ATUALIZANDO ITENS**
    1. MANEIRA MAIS SIMPLES:
        Adicionar uma chave nova depois do dicionário:
            dicio = {'primeiro': 1}
            dicio = ['segundo'] = 2

    2. Utilizando o *update()*, que pode criar ou atualizar dados
        dicio = {'primeiro': 1, 'segundo': 2}
        dicio.update({'primeiro': 2})
        dicio.update({'quarto': 4})
        print(dicio)
    
    **=> EXCLUINDO ITENS DO DICIONÁRIO**
    Utiliamos o *del*
    dicio = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
    del dicio['primeiro']

    **=> EXCLUINDO E RETORNANDO O ITEM EXCLUÍDO**
    Utilizamos o pop()
    dicio = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
    primeiro = dicio.pop('primeiro')
    print(dicio)
    print(primeiro)


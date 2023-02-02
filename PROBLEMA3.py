from sys import stdin


sulfixos_possivieis=(('o','ei','ai'),
    ('os','es','ais'),
    ('a','e','i'),
    ('om','em','aem'),
    ('ons','est','aist'),
    ('am','im','aim'))


def descobrir_sulfixo(palavra):
    limite_da_palavra=4
    sulfixo_final=''
    tempo_verbal=1
    infinitivo=''
    while(limite_da_palavra):
        sulfixo_da_entrada=palavra[-limite_da_palavra:]
        for tupla in sulfixos_possivieis:
            for sulfixo in tupla:
                if sulfixo == sulfixo_da_entrada:
                    if len(sulfixo)>len(sulfixo_final):
                        sulfixo_final=sulfixo
                        infinitivo=palavra[:-limite_da_palavra]+'en'
                else:
                    pass
            
            
        
        limite_da_palavra-=1
    if sulfixo_final == '':
        return "não é um tempo verbal"
        
        
    return sulfixo_final,infinitivo


def pessoa(sulfixo_palavra):
    pessoa=1
    for tupla in sulfixos_possivieis:
        if sulfixo_palavra in tupla:
            break
        else:
            pessoa+=1


    return(str(pessoa))


def tempo(sulfixo,pessoa):
    n_pessoa=int(pessoa)
    tupla=sulfixos_possivieis[n_pessoa-1]
    tempo_final=''
    if tupla[0]==sulfixo:
        tempo_final='presente'
    
    elif tupla[1]==sulfixo:
        tempo_final='pretérito'
    
    else:
        tempo_final='futuro'
    
    return tempo_final

 


def main():
    line=stdin.readline().strip()
    while True:
        
        if line == '':
            break

        if descobrir_sulfixo(line) == "não é um tempo verbal":
            print("não é um tempo verbal")
        
        else:
            sulfixo,infinitivo=descobrir_sulfixo(line)
            n_pessoa=pessoa(sulfixo)
            n_tempo=tempo(sulfixo,n_pessoa)
            print("{} - verbo {}, {}, {}a pessoa".format(line,infinitivo,n_tempo,n_pessoa))
            
            
        
        line=stdin.readline().strip()
        


if __name__=='__main__':
    main()

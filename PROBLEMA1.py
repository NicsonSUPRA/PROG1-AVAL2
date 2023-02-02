from sys import stdin


def verify_num(num):
    acumulador = 0
    contador = 1
    while(acumulador <= num):
        acumulador+=contador
        contador+=1
        if(acumulador == num):
            return True
    return False


def M_alternates(lista):
    first_index=0
    second_index=1
    counting=2
    listanova=list()
    while(second_index <= len(lista)):
        listanova.append(lista[first_index:second_index])
        first_index=second_index
        second_index+=counting
        counting+=1
    return listanova


def zero_um(first_element):
    if(first_element%2==0):
        resto=0
    else:
        resto=1
    return resto


def main():
    num=None
    while(num != ''):
        num=stdin.readline().strip()
        lista=stdin.readline().strip().split()
        hashtag=stdin.readline().strip()
        
        if num == '':
            break

        if(verify_num(int(num))):
            lista=M_alternates(list(map(lambda e: int(e),lista)))
            resto=zero_um(lista[0][0])
            answer=None
            
            for e in lista:
                
                for i in e:
                    
                    if(i%2==resto):
                        pass
                    
                    else:
                        answer='NAO'
                
                if resto == 1:
                    resto=0
                
                else:
                    resto=1
            
            if answer:
                
                if answer == 'NAO':
                    print('NAO')
                    print(hashtag)
                    break

                print(answer)
                print(hashtag)
            
            else:
                print(len(lista[-1]))
                print(hashtag)

        else:
            print('NAO')
            print(hashtag)
            break


        
if __name__=='__main__':
    main()

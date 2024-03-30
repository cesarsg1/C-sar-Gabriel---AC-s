import random

def main():
    vida_aventureiro = 100
    att_aventureiro = random.randint(10, 20)
    def_aventureiro = random.randint(1, 5)
    vida_monstro = random.randint(60, 80)
    att_monstro = random.randint(20, 30)
    count = 1

    print("Aventureiro: vida", vida_aventureiro, "- att", att_aventureiro, "- def", def_aventureiro, 
          "\nMonstro: vida", vida_monstro, "- att", att_monstro)

    while vida_aventureiro > 0 and vida_monstro > 0:
        print("Rodada", count)
        vida_monstro -= random.randint(1,att_aventureiro)
        if vida_monstro <= 0:
            print("O monstro morreu!")
            break
        vida_aventureiro -= random.randint(1, att_monstro) - def_aventureiro
        if vida_aventureiro <= 0:
            print("O aventureiro morreu!")
            break
        print("Aventureiro: vida", vida_aventureiro, "- att", att_aventureiro,
        "- def", def_aventureiro, "\nMonstro: vida", vida_monstro, "- att", att_monstro)
        count += 1
main()
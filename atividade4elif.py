# VAGA DE EMPREGO
idade = int(input("Qual sua idade"))
experiencia = input("Tem experiencia?:(True or False)")
antecedentes_criminais = input("Tem antecedentes criminais?:(True or False)")
ensino_superior = input("Tem curso superior?:(True or False)")
indicacao= input("Tem vip?:(True or False)")
if idade>18 and experiencia and not antecedentes_criminais:
    print("Vai ser contratado pela experiencia")
elif experiencia== "False" and (ensino_superior or indicacao and not antecedentes_criminais):
    print(" Contratado para entrevista mesmo sem experiencia")
else:
    print("Canditado  rejeitado")

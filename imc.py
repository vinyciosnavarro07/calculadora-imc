from colorama import init, Fore
init(autoreset=True)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return f"{Fore.RED}Baixo peso. É recomendado procurar um médico para avaliação criteriosa."
    elif 18.5 <= imc < 25:
        return f"{Fore.GREEN}Peso adequado. Tudo indica que está tudo bem, mas avalie outros parâmetros da composição corporal."
    elif 25 <= imc < 30:
        return f"{Fore.LIGHTRED_EX}Sobrepeso. Consulte um médico e reveja hábitos para reverter o quadro."
    elif 30 <= imc < 35:
        return f"{Fore.RED}Obesidade Grau I. É importante buscar orientação médica e nutricional."
    elif 35 <= imc < 40:
        return f"{Fore.RED}Obesidade Grau II. Indica um quadro de obesidade mais avançado, procure ajuda."
    else:
        return f"{Fore.RED}Obesidade Grau III. A chance de doenças associadas é alta, busque orientação médica urgentemente."

def main():
    print(f"{Fore.YELLOW}================Calculadora de IMC=====================")
    try:
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"\nSeu IMC é {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Por favor, insira valores válidos para peso e altura. Tente novamente")

if __name__ == "__main__":
    main()


point = 0


print("oi bem-vindo as perguntas da microsoft")
bing = input("qual o navegador da microsoft ? ")
if bing == 'bing':
    print("acertou")
    point = point + 100
    print(point)
else:
    print("errou")
    point = point - 50
    print(point)

VC = input("qual o aplicativo de criar codigos da microsoft ? ")
if VC == 'visual code':
    print("acertou")
    point = point + 100
    print(point)
else:
    print("errou")
    point = point - 50
    print(point)

corta = input("qual a inteligencia artificial da microsoft ? ")
if corta == 'cortana':
    print("acertou")
    point = point + 100
    print(point)
else:
    print("errou")
    point = point - 50
    print(point)
print("vc terminou com", point, "pontos")
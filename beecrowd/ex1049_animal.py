categoria = input()
classe = input()
dieta = input()
animal = ''
if categoria == 'vertebrado':
    if classe == 'ave':
        if dieta == 'carnivoro':
            animal = 'aguia'
        elif dieta == 'onivoro':
            animal = 'pomba'
    elif classe == 'mamifero':
        if dieta == 'onivoro':
            animal = 'homem'
        elif dieta == 'herbivoro':
            animal = 'vaca'
elif categoria == 'invertebrado':
    if classe == 'inseto':
        if dieta == 'hematofago':
            animal = 'pulga'
        elif dieta == 'herbivoro':
            animal = 'lagarta'
    elif classe == 'anelideo':
        if dieta == 'hematofago':
            animal = 'sanguessuga'
        elif dieta == 'onivoro':
            animal = 'minhoca'
print(animal)
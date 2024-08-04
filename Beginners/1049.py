x, y, z = input(), input(), input()

animals = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
        },

        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }   
    },

    'invertebrado':{
        'inseto':{
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },

        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

print(animals[x][y][z])
import pymongo

SERVER_ADDR="104.248.230.23"
connection =pymongo.MongoClient(SERVER_ADDR)
db = connection.aa
collection = db.bb

def find_pokemon_by_num(num):
    '''
    finds pokemon by num.
    '''
    pokemon = collection.find({'num':num})
    return [poke for poke in pokemon]

def find_pokemon_by_steps(steps):
    '''
    finds pokemon by the # of steps needed to hatch their egg.
    parameter should be given as <float> km.
    '''
    pokemon = collection.find({'egg':steps})
    return [poke for poke in pokemon]

def type_find(first_type, second_type):
    '''
    finds pokemon by types and returns them in a list.
    '''
    pokemon = collection.find(
        {'$and':[
            {'type':first_type},
            {'type':second_type},
            ]
        }
    )
    return [poke for poke in pokemon]

def type_spawn_find(type, rate):
    '''
    finds pokemon by type and less than the given spawn rate and returns them in a list.
    '''
    pokemon = collection.find(
        {'$and':[
            {'type':type},
            {'spawn_chance':{'$lt':rate}}, #nums are scores
            ]
        }
    )
    return [poke for poke in pokemon]

def type_id_weakness_find(type, id, weakness):
    '''
    finds pokemon by type, and greater than the id, and weakness and returns them in a list.
    '''
    pokemon = collection.find(
        {'$and':[
            {'type':type},
            {'id':{'$gt':id}}, #nums are scores
            {'weaknesses': weakness},
            ]
        }
    )
    return [poke for poke in pokemon]


if __name__ == '__main__':
    print('Printing num...')
    print(find_pokemon_by_num('049'))
    print('Printing steps....')
    print(find_pokemon_by_steps("5 km"))
    print('Printing dual types...')
    print(type_find('Ground', 'Rock'))
    print('Printing type and spawn...')
    print(type_spawn_find('Normal', 0.2))
    print('Printing type, id, and weakness...')
    print(type_id_weakness_find('Water', 12, 'Rock'))

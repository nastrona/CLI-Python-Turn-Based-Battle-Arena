class char:

    def Warrior(self):
        lvl = 1
        stat = [100,0,1,True,0,0,0,0]
        stat = {'HP':stat[0],
                'EXP':stat[1],
                'Level':stat[2],
                'Alive':stat[3],
                'MIN_ATK':stat[4],
                'MAX_ATK':stat[5],
                'MIN_DEF':stat[6],
                'MAX_DEF':stat[7]}

        if stat['Level'] == 1:
            stat['MIN_ATK'] = 5
            stat['MAX_ATK'] = 8
            stat['MIN_DEF'] = 2
            stat['MAX_DEF'] = 3
                
        elif stat['Level'] == 2:
            stat['MIN_ATK'] = 9
            stat['MAX_ATK'] = 13
            stat['MIN_DEF'] = 4
            stat['MAX_DEF'] = 6
            
        elif stat['Level'] == 3:
            stat['MIN_ATK'] = 14
            stat['MAX_ATK'] = 17
            stat['MIN_DEF'] = 7
            stat['MAX_DEF'] = 8
        
        elif stat['Level'] == 4:
            stat['MIN_ATK'] = 18
            stat['MAX_ATK'] = 20
            stat['MIN_DEF'] = 9
            stat['MAX_DEF'] = 10

        return stat

    def Tank(self):
        lvl = 1
        stat = [100,0,0,0,0,0,1,True]
        stat = {'HP':stat[0],
            'MIN_ATK':stat[1],
            'MAX_ATK':stat[2],
            'MIN_DEF':stat[3],
            'MAX_DEF':stat[4],
            'EXP':stat[5],
            'Level':stat[6],
            'Alive':stat[7]}
            
        if stat['Level'] == 1:
            stat['MIN_ATK'] = 1
            stat['MAX_ATK'] = 3
            stat['MIN_DEF'] = 5
            stat['MAX_DEF'] = 7
        elif stat['Level'] == 2:
            stat['MIN_ATK'] = 4
            stat['MAX_ATK'] = 6
            stat['MIN_DEF'] = 8
            stat['MAX_DEF'] = 10
        elif stat['Level'] == 3:
            stat['MIN_ATK'] = 7
            stat['MAX_ATK'] = 8
            stat['MIN_DEF'] = 11
            stat['MAX_DEF'] = 13
        elif stat['Level'] == 4:
             stat['MIN_ATK'] = 9
             stat['MAX_ATK'] = 10
             stat['MIN_DEF'] = 14
             stat['MAX_DEF'] = 15
             
        return stat
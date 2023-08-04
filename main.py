import random


#'sunday': None, 'monday': None, 'tuesday': None, 'wednesday': None, 'thursday': None, 'friday': None, 'saturday': None
calander = {}
personse = []
allshift = []
all_blocks = []
more_days = 'y'
answer = 'y'
want_to_block = None
x = 0
lefts_shift = 0
shift_str = ''
first = True
lent = True



def insert_shifts(name):
    i = 0
    y = True
    while i < name['shift_amount']:
        if y:
            for one_block in all_blocks:
                if name["blocked"][one_block] == None and calander[one_block] != name['name']:
                    calander[one_block] = name['name']
                    i = i + 1
                y = False
        day = random.choice(allshift)
        if calander[day] != name['name'] and name["blocked"][day] == None  and i < name['shift_amount']:
            calander[day] = name['name']
            i = i + 1


def chose_person(peple):
    for one in peple:
        for shif in allshift:
            if shif not in one["blocked"]:
                calander[shif].append(one["name"])
        while one["shift_amount"] > 0:
            shif = random.choice(allshift)
            chosen = random.choice(calander[shif])
            if chosen not in one["blocked"] and one["shift_amount"] > 0 and type(calander[shif]) != list:
                calander[chosen] = one["name"]
                one["shift_amount"] = one["shift_amount"] - 1




while more_days == 'y':
    shift = input('Please enter the shift date: ')
    calander[shift[:]] = []
    allshift.append(shift[:])
    more_days = input('do you want to add another date (y/n)? ')
    while more_days != 'y' and more_days != 'n':
        more_days = input('invalid answer! do you want to block another shift?  (y/n)? ')

for shif in allshift:
    if first:
        shift_str = shift_str + shif
        first = False
    else:
       shift_str = shift_str +"/ " + shif

while answer == 'y':
    personse.append({'name': input('What is his name? '), 'shift_amount': int(input('How much shift do you want to attend? ')), "blocked": [] })
    want_to_block = input('do you want to block (y/n)? ')
    while want_to_block != 'y' and want_to_block != 'n':
        want_to_block = input('Invalid answer! do you want to block (y/n)? ')
    while want_to_block == 'y':
        day_block = input(f'what is the day ({shift_str})? ')
        personse[x]["blocked"].append(day_block[:])
        if day_block[:] not in all_blocks:
            all_blocks.append(day_block[:])
        want_to_block = input('do you want to block another shift (y/n)? ')
        while want_to_block != 'y' and want_to_block != 'n':
            want_to_block = input('invalid answer! do you want to block another shift?  (y/n)? ')
    if lent:
        lefts_shift = len(allshift)
        lent = False
    while personse[x]['shift_amount'] > lefts_shift or personse[x]['shift_amount'] > 7:
        personse[x]['shift_amount'] = int(input(f"you can chose max of 7 and their is only {lefts_shift} shift left! pleas chose a new shift amount: "))
    lefts_shift = lefts_shift - personse[x]['shift_amount']
    if lefts_shift != 0:
        answer = None
        while answer != 'y' and answer != 'n':
            answer = input(f'{lefts_shift} shifts left. do you want to add more peple (y,n)? ')
    else:
        answer = 'n'
    x = x + 1
print(all_blocks)
chose_person(personse)
print(calander)
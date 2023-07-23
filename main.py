import random



calander = {'sunday':{'morning': None, 'evening': None, 'night': None}, 'monday': {'morning': None, 'evening': None, 'night': None}, 'tuesday': {'morning': None, 'evening': None, 'night': None}, 'wednesday': {'morning': None, 'evening': None, 'night': None}, 'thursday': {'morning': None, 'evening': None, 'night': None}, 'friday': {'morning': None, 'evening': None, 'night': None}, 'saturday': {'morning': None, 'evening': None, 'night': None}}
personse = []
answer = 'y'
x = 0
lefts_shift = 21



def insert_shifts(name):
    i = 0
    while i < name['shift_amount']:
        day = random.choice(['sunday', 'monday', 'tuesday','wednesday','thursday','friday','saturday'])
        if calander[day]['morning'] != name['name'] and calander[day]['evening'] != name['name'] and calander[day]['night'] != name['name']:
            random_shift(day, name)
            i = i + 1

def random_shift(day, name):
    run = True
    while run:
        shift = random.choice(['morning','evening','night'])
        if calander[day][shift] == None and name["blocked"][day][shift] == None:
            calander[day][shift] = name['name']
            run = False


def chose_person(peple):
    for one in peple:
        insert_shifts(one)

while answer == 'y':
    personse.append({'name': input('What is his name? '), 'shift_amount': int(input('How much shift do you want to attend? ')), "blocked": {
        'sunday': {'morning': None, 'evening': None, 'night': None},
        'monday': {'morning': None, 'evening': None, 'night': None},
        'tuesday': {'morning': None, 'evening': None, 'night': None},
        'wednesday': {'morning': None, 'evening': None, 'night': None},
        'thursday': {'morning': None, 'evening': None, 'night': None},
        'friday': {'morning': None, 'evening': None, 'night': None},
        'saturday': {'morning': None, 'evening': None, 'night': None}}})
    want_to_block = input('do you want to block (y/n)? ')
    while want_to_block == 'y':
        day_block = input('what is the day? ')
        shift_block = input('what is the shift? ')
        if shift_block == 'all':
            personse[x]["blocked"][day_block[:]]['morning'] = True
            personse[x]["blocked"][day_block[:]]['evening'] = True
            personse[x]["blocked"][day_block[:]]['night'] = True
        else:
            personse[x]["blocked"][day_block[:]][shift_block[:]] = True
        want_to_block = input('do you want to block another shift (y/n)? ')
    while personse[x]['shift_amount'] > lefts_shift or personse[x]['shift_amount'] > 7:
        personse[x]['shift_amount'] = int(input(f"you can chose max of 7 and their is only {lefts_shift} shift left! pleas chose a new shift amount: "))
    lefts_shift = lefts_shift - personse[x]['shift_amount']
    if lefts_shift != 0:
        answer = input(f'{lefts_shift} shifts left. do you want to add more peple (y,n)? ')
    else:
        answer = 'n'
    x = x + 1

chose_person(personse)
print(calander)


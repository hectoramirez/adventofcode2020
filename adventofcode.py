import pandas as pd
from math import prod
import numpy as np

# ++++++++++++++++++++++ #
# Day 1: Report Repair   #
# ++++++++++++++++++++++ #

data = pd.read_csv('data/input.txt', sep=" ", header=None)
data.columns = ['N']

'''for i in data['N']:
    for j in data['N']:
        if i + j == 2020:
            print(i, j, i*j)

for i in data['N']:
    for j in data['N']:
        for z in data['N']:
            if i + j + z == 2020:
                print(i, j, z, i*j*z)'''

# +++++++++++++++++++++++++++ #
# Day 2: Password Philosophy  #
# +++++++++++++++++++++++++++ #

data = pd.read_csv('data/day2.txt', sep=" ", header=None)
data.columns = ['code1', 'code2', 'pwd']
data[['in', 'out']] = data['code1'].str.split('-', expand=True)
data['code2'] = data['code2'].map(lambda x: x.rstrip(':'))

z = 0
for idx, row in data.iterrows():
    num = row['pwd'].count(row['code2'])
    i, j = int(row['in']), int(row['out'])
    if i <= num <= j:
        z += 1
# print(z)

k = 0
for idx, row in data.iterrows():
    i, j, pwd, le = int(row['in']), int(row['out']), row['pwd'], row['code2']
    if pwd[i - 1] == le or pwd[j - 1] == le:
        if pwd[i - 1] != pwd[j - 1]:
            k += 1
# print(k)

# +++++++++++++++++++++++++++ #
# Day 3: Toboggan Trajectory  #
# +++++++++++++++++++++++++++ #

data = pd.read_csv('data/day3.txt', sep=" ", header=None)
data.columns = ['T']


def split(word):
    return [char for char in word]


data['T'] = data['T'].apply(split)
df = pd.DataFrame.from_dict(dict(zip(data['T'].index, data['T'].values)))
df = df.T

x = 0
trees = 0
for idx, row in df.iterrows():
    if row[x % len(row)] == '#':
        trees += 1
    x += 3
# print(trees)


trees = []
for i in [1, 3, 5, 7]:
    x = 0
    trees_n = 0
    for idx, row in df.iterrows():
        if row[x % len(row)] == '#':
            trees_n += 1
        x += i
    trees.append(trees_n)

x = 0
trees_n = 0
for idx, row in df.iterrows():
    if idx % 2 == 0:
        if row[x % len(row)] == '#':
            trees_n += 1
        x += 1
trees.append(trees_n)
# print(prod(trees))


# +++++++++++++++++++++++++++ #
# Day 4: Passport Processing  #
# +++++++++++++++++++++++++++ #


elements = []
data = open('data/day4.txt', 'r')
data = data.read()
lines = data.split('\n\n')
for line in lines:
    element = line.split(' ')
    t = [el.split('\n') for el in element]
    li = [item for sublist in t for item in sublist]
    elements.append(li)

x = 0
for e_list in elements:
    if len(e_list) == 8:
        x += 1
        continue
    elif len(e_list) == 7:
        codes = [el[:3] for el in e_list]
        if 'cid' not in codes:
            x += 1
    else:
        continue
# print(x)

y = 0
for e_list in elements:
    if len(e_list) >= 7:
        codes = [el[:3] for el in e_list]
        vals = [el[4:] for el in e_list]
        res = dict(zip(codes, vals))

        try:
            if (len(res['byr']) == 4 and 1920 <= int(res['byr']) <= 2002
                    and len(res['iyr']) == 4 and 2010 <= int(res['iyr']) <= 2020
                    and len(res['eyr']) == 4 and 2020 <= int(res['eyr']) <= 2030
                    and ((res['hgt'][-2:] == 'cm' and 150 <= int(res['hgt'][:-2]) <= 193)
                         or (res['hgt'][-2:] == 'in' and 59 <= int(res['hgt'][:-2]) <= 76))
                    and (res['hcl'][0] == '#' and len(res['hcl']) == 7
                         and all(c in '0123456789abcdef' for c in res['hcl'][1:]))
                    and res['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    and (len(res['pid']) == 9 and all(c in '0123456789' for c in res['pid']))):
                y += 1
        except:
            continue
# print(y)

# +++++++++++++++++++++++++++ #
# Day 5: Binary Boarding      #
# +++++++++++++++++++++++++++ #

data = open('data/day5.txt', 'r')
data = data.read()
codes = data.split('\n')

ids = []
for code in codes:
    rows = np.arange(0, 128)
    for letter in code[:7]:
        div = int(rows.shape[0] / 2)
        if letter == 'F':
            rows = rows[:div]
        else:
            rows = rows[div:]
    row = rows[0]

    columns = np.arange(0, 8)
    for letter in code[7:]:
        div = int(columns.shape[0] / 2)
        if letter == 'L':
            columns = columns[:div]
        else:
            columns = columns[div:]
    column = columns[0]

    ids.append(row * 8 + column)
# print(max(ids))

id_min = np.sort(ids)[1]
id_max = np.sort(ids)[-1]
# print(set(np.arange(id_min, id_max+1)) - set(np.sort(ids)[1:]))


# +++++++++++++++++++++++++++ #
# Day 6: Custom Customs       #
# +++++++++++++++++++++++++++ #

data = open('data/day6.txt', 'r')
data = data.read()
groups = data.split('\n\n')

p = 0
for group in groups:
    people = group.replace("\n", "")
    p += len(list(set(people)))
print(p)

y = 0
for group in groups:
    people_n = len(group.split('\n'))
    all_g = group.replace("\n", "")
    letters = list(set(all_g))
    for let in letters:
        if all_g.count(let) == people_n:
            y += 1
print(y)

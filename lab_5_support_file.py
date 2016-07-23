f = [[1, 2, 3],
     [2, 4, 6],
     [3, 6, 9]
    ]

def transform(f):
    new_list = []
    Alphabet = ['A', 'B', 'C']
    count_2 = 0
    for l in f:
        new = {}
        for k in l:
            print(count_2, k)
            new[Alphabet[count_2]] = k
            count_2 += 1
        count_2 = 0
        new_list.append(new)
    print(new_list)

transform(f)
            
            
            

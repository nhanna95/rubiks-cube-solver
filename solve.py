#   B
# O W R
#   G

#   W
# O G R
#   Y

#   W
# G R B
#   Y

#   W
# R B O
#   Y

#   W
# B O G
#   Y

#   R
# G Y B
#   O

solved_cube_faces = [
    ['W', 'W', 'W',
     'W', 'W', 'W',
     'W', 'W', 'W'],
    ['G', 'G', 'G',
     'G', 'G', 'G',
     'G', 'G', 'G'],
    ['R', 'R', 'R',
     'R', 'R', 'R',
     'R', 'R', 'R'],
    ['B', 'B', 'B',
     'B', 'B', 'B',
     'B', 'B', 'B'],
    ['O', 'O', 'O',
     'O', 'O', 'O',
     'O', 'O', 'O'],
    ['Y', 'Y', 'Y',
     'Y', 'Y', 'Y',
     'Y', 'Y', 'Y']
]

solved_cube_pieces = [
    ['BOW', 'BW', 'BRW',
     'OW', 'W', 'RW',
     'GOW', 'GW', 'GRW'],
    ['BO', 'B', 'BR',
     'O', '', 'R',
     'GO', 'G', 'GR'],
    ['BOY', 'BY', 'BRY',
     'OY', 'Y', 'RY',
     'GOY', 'GY', 'GRY']
]

cube_faces = [
    ['W', 'Y', 'W',
     'Y', 'W', 'Y',
     'W', 'Y', 'W'],
    ['G', 'B', 'G',
     'B', 'G', 'B',
     'G', 'B', 'G'],
    ['R', 'O', 'R',
     'O', 'R', 'O',
     'R', 'O', 'R'],
    ['B', 'G', 'B',
     'G', 'B', 'G',
     'B', 'G', 'B'],
    ['O', 'R', 'O',
     'R', 'O', 'R',
     'O', 'R', 'O'],
    ['Y', 'W', 'Y',
     'W', 'Y', 'W',
     'Y', 'W', 'Y']
]

cube_pieces = [
    ['BOW', 'GY', 'BRY',
     'RY', 'W', 'OY',
     'GOW', 'BY', 'GRY'],
    ['GR', 'B', 'GO',
     'O', '', 'R',
     'BR', 'G', 'BO'],
    ['BOY', 'GW', 'BRY',
     'RW', 'Y', 'OW',
     'GOY', 'BW', 'GRY']
]

face_to_ind = {
    'W': 0,
    'G': 1,
    'R': 2,
    'B': 3,
    'O': 4,
    'Y': 5
}

face_rel_ind = {
    'WT': 3,
    'WB': 1,
    'WR': 2,
    'WL': 4,
    'GT': 0,
    'GB': 5,
    'GR': 2,
    'GL': 4,
    'RT': 0,
    'RB': 5,
    'RR': 3,
    'RL': 1,
    'BT': 0,
    'BB': 5,
    'BR': 4,
    'BL': 2,
    'OT': 0,
    'OB': 5,
    'OR': 1,
    'OL': 3,
    'YT': 2,
    'YB': 4,
    'YR': 3,
    'YL': 1
}

face_rel_tri = {
    'WTC': [2, 1, 0],
    'WBC': [2, 1, 0],
    'WRC': [2, 1, 0],
    'WLC': [2, 1, 0],

    'GTC': [6, 7, 8],
    'GBC': [0, 3, 6],
    'GRC': [0, 3, 6],
    'GLC': [8, 5, 2],

    'RTC': [8, 5, 2],
    'RBC': [2, 1, 0],
    'RRC': [0, 3, 6],
    'RLC': [8, 5, 2],

    'BTC': [2, 1, 0],
    'BBC': [8, 5, 2],
    'BRC': [0, 3, 6],
    'BLC': [8, 5, 2],

    'OTC': [0, 3, 6],
    'OBC': [6, 7, 8],
    'ORC': [0, 3, 6],
    'OLC': [8, 5, 2],

    'YTC': [6, 7, 8],
    'YBC': [6, 7, 8],
    'YRC': [6, 7, 8],
    'YLC': [6, 7, 8],

    'WTCW': [0, 1, 2],
    'WBCW': [0, 1, 2],
    'WRCW': [0, 1, 2],
    'WLCW': [0, 1, 2],

    'GTCW': [8, 7, 6],
    'GBCW': [6, 3, 0],
    'GRCW': [6, 3, 0],
    'GLCW': [2, 5, 8],

    'RTCW': [2, 5, 8],
    'RBCW': [0, 1, 2],
    'RRCW': [6, 3, 0],
    'RLCW': [2, 5, 8],

    'BTCW': [0, 1, 2],
    'BBCW': [2, 5, 8],
    'BRCW': [6, 3, 0],
    'BLCW': [2, 5, 8],

    'OTCW': [6, 3, 0],
    'OBCW': [8, 7, 7],
    'ORCW': [6, 3, 0],
    'OLCW': [2, 5, 8],

    'YTCW': [8, 7, 6],
    'YBCW': [8, 7, 6],
    'YRCW': [8, 7, 6],
    'YLCW': [8, 7, 6]
}

rotate_piece_dict = {
    'WC': [
        [[0, 0], [0, 1], [0, 2], [0, 3], [0, 5], [0, 6], [0, 7], [0, 8]],
        [[0, 6], [0, 3], [0, 0], [0, 7], [0, 1], [0, 8], [0, 5], [0, 2]]
    ],
    'WCW': [
        [[0, 0], [0, 1], [0, 2], [0, 3], [0, 5], [0, 6], [0, 7], [0, 8]],
        [[0, 2], [0, 5], [0, 8], [0, 1], [0, 7], [0, 0], [0, 3], [0, 6]]
    ],
    'GC': [
        [[0, 6], [0, 7], [0, 8], [1, 6], [1, 8], [2, 6], [2, 7], [2, 8]],
        [[2, 6], [1, 6], [0, 6], [2, 7], [0, 7], [2, 8], [1, 8], [0, 8]]
    ],
    'GCW': [
        [[0, 6], [0, 7], [0, 8], [1, 6], [1, 8], [2, 6], [2, 7], [2, 8]],
        [[0, 8], [1, 8], [2, 8], [0, 7], [2, 7], [0, 6], [1, 6], [2, 6]]
    ],
    'RC': [
        [[0, 8], [0, 5], [0, 2], [1, 8], [1, 2], [2, 8], [2, 5], [2, 2]],
        [[2, 8], [1, 8], [0, 8], [2, 5], [0, 5], [2, 2], [1, 2], [0, 2]]
    ],
    'RCW': [
        [[0, 8], [0, 5], [0, 2], [1, 8], [1, 2], [2, 8], [2, 5], [2, 2]],
        [[0, 2], [1, 2], [2, 2], [0, 5], [2, 5], [0, 8], [1, 8], [2, 8]]
    ],
    'BC': [
        [[0, 2], [0, 1], [0, 0], [1, 2], [1, 0], [2, 2], [2, 1], [2, 0]],
        [[2, 2], [1, 2], [0, 2], [2, 1], [0, 1], [2, 0], [1, 0], [0, 0]]
    ],
    'BCW': [
        [[0, 2], [0, 1], [0, 0], [1, 2], [1, 0], [2, 2], [2, 1], [2, 0]],
        [[0, 0], [1, 0], [2, 0], [0, 1], [2, 1], [0, 2], [1, 2], [2, 2]]
    ],
    'OC': [
        [[0, 0], [0, 3], [0, 6], [1, 0], [1, 6], [2, 0], [2, 3], [2, 6]],
        [[2, 0], [1, 0], [0, 0], [2, 3], [0, 3], [2, 6], [1, 6], [0, 6]]
    ],
    'OCW': [
        [[0, 0], [0, 3], [0, 6], [1, 0], [1, 6], [2, 0], [2, 3], [2, 6]],
        [[0, 6], [1, 6], [2, 6], [0, 3], [2, 3], [0, 0], [1, 0], [2, 0]]
    ],
    'YC': [
        [[2, 0], [2, 1], [2, 2], [2, 3], [2, 5], [2, 6], [2, 7], [2, 8]],
        [[2, 6], [2, 3], [2, 0], [2, 7], [2, 1], [2, 8], [2, 5], [2, 2]]
    ],
    'YCW': [
        [[2, 0], [2, 1], [2, 2], [2, 3], [2, 5], [2, 6], [2, 7], [2, 8]],
        [[2, 2], [2, 5], [2, 8], [2, 1], [2, 7], [2, 0], [2, 3], [2, 6]]]
}


def turn_face(c, p, f, d):
    face = face_to_ind[f]
    top = face_rel_ind[f + 'T']
    top_tri = face_rel_tri[f + 'T' + d]
    bottom = face_rel_ind[f + 'B']
    bottom_tri = face_rel_tri[f + 'B' + d]
    right = face_rel_ind[f + 'R']
    right_tri = face_rel_tri[f + 'R' + d]
    left = face_rel_ind[f + 'L']
    left_tri = face_rel_tri[f + 'L' + d]
    static_cube = []
    static_cube_pieces = []
    for i in c:
        static_face = []
        for j in i:
            static_face.append(j)
        static_cube.append(static_face)

    for i in p:
        static_pieces = []
        for j in i:
            static_pieces.append(j)
        static_cube_pieces.append(static_pieces)

    if d == 'C':
        c[face][0] = static_cube[face][6]
        c[face][1] = static_cube[face][3]
        c[face][2] = static_cube[face][0]
        c[face][3] = static_cube[face][7]
        c[face][5] = static_cube[face][1]
        c[face][6] = static_cube[face][8]
        c[face][7] = static_cube[face][5]
        c[face][8] = static_cube[face][2]
        for x, y in zip(top_tri, left_tri):
            c[top][x] = static_cube[left][y]
        for x, y in zip(right_tri, top_tri):
            c[right][x] = static_cube[top][y]
        for x, y in zip(bottom_tri, right_tri):
            c[bottom][x] = static_cube[right][y]
        for x, y in zip(left_tri, bottom_tri):
            c[left][x] = static_cube[bottom][y]
    else:
        c[face][0] = static_cube[face][2]
        c[face][1] = static_cube[face][5]
        c[face][2] = static_cube[face][8]
        c[face][3] = static_cube[face][1]
        c[face][5] = static_cube[face][7]
        c[face][6] = static_cube[face][0]
        c[face][7] = static_cube[face][3]
        c[face][8] = static_cube[face][6]
        for x, y in zip(left_tri, top_tri):
            c[left][x] = static_cube[top][y]
        for x, y in zip(top_tri, right_tri):
            c[top][x] = static_cube[right][y]
        for x, y in zip(right_tri, bottom_tri):
            c[right][x] = static_cube[bottom][y]
        for x, y in zip(bottom_tri, left_tri):
            c[bottom][x] = static_cube[left][y]

    points, replacements = rotate_piece_dict[f + d]

    for x, y in zip(points, replacements):
        x1 = x[0]
        x2 = x[1]
        y1 = y[0]
        y2 = y[1]
        p[x1][x2] = static_cube_pieces[y1][y2]

    return c, p


for i in cube_faces:
    print(i)
for i in cube_pieces:
    print(i)
cube_faces, cube_pieces = turn_face(cube_faces, cube_pieces, 'W', 'C')
print()
for i in cube_faces:
    print(i)
for i in cube_pieces:
    print(i)


counter = 0
while not (cube_faces[0][1] == 'W' and cube_faces[0][3] == 'W' and cube_faces[0][5] == 'W' and cube_faces[0][7] == 'W' and cube_faces[1][1] == 'G' and cube_faces[2][1] == 'R' and cube_faces[3][1] == 'B' and cube_faces[4][1] == 'O'):
    

    counter += 1
    if counter == 10:
        break

a_1 = " "
a_2 = " "
a_3 = " "
a_4 = 2
a_5 = 6
a_6 = " "
a_7 = 7
a_8 = " "
a_9 = 1
b_1 = 6
b_2 = 8
b_3 = " "
b_4 = " "
b_5 = 7
b_6 = " "
b_7 = " "
b_8 = 9
b_9 = " "
c_1 = 1
c_2 = 9
c_3 = " "
c_4 = " "
c_5 = " "
c_6 = 4
c_7 = 5
c_8 = " "
c_9 = " "
d_1 = 8
d_2 = 2
d_3 = " "
d_4 = 1
d_5 = " "
d_6 = " "
d_7 = " "
d_8 = 4
d_9 = " "
e_1 = " "
e_2 = " "
e_3 = 4
e_4 = 6
e_5 = " "
e_6 = 2
e_7 = 9
e_8 = " "
e_9 = " "
f_1 = " "
f_2 = 5
f_3 = " "
f_4 = " "
f_5 = " "
f_6 = 3
f_7 = " "
f_8 = 2
f_9 = 8
g_1 = " "
g_2 = " "
g_3 = 9
g_4 = 3
g_5 = " "
g_6 = " "
g_7 = " "
g_8 = 7
g_9 = 4
h_1 = " "
h_2 = 4
h_3 = " "
h_4 = " "
h_5 = 5
h_6 = " "
h_7 = " "
h_8 = 3
h_9 = 6
i_1 = 7
i_2 = " "
i_3 = 3
i_4 = " "
i_5 = 1
i_6 = 8
i_7 = " "
i_8 = " "
i_9 = " "

a = [a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9]
b = [b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9]
c = [c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9]
d = [d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9]
e = [e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8, e_9]
f = [f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9]
g = [g_1, g_2, g_3, g_4, g_5, g_6, g_7, g_8, g_9]
h = [h_1, h_2, h_3, h_4, h_5, h_6, h_7, h_8, h_9]
i = [i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9]

box1 = [a_1, a_2, a_3, b_1, b_2, b_3, c_1, c_2, c_3]
box2 = [a_4, a_5, a_6, b_4, b_5, b_6, c_4, c_5, c_6]
box3 = [a_7, a_8, a_9, b_7, b_8, b_9, c_7, c_8, c_9]
box4 = [d_1, d_2, d_3, e_1, e_2, e_3, f_1, f_2, f_3]
box5 = [d_4, d_5, d_6, e_4, e_5, e_6, f_4, f_5, f_6]
box6 = [d_7, d_8, d_9, e_7, e_8, e_9, f_7, f_8, f_9]
box7 = [g_1, g_2, g_3, h_1, h_2, h_3, i_1, i_2, i_3]
box8 = [g_4, g_5, g_6, h_4, h_5, h_6, i_4, i_5, i_6]
box9 = [g_7, g_8, g_9, h_7, h_8, h_9, i_7, i_8, i_9]

alpha = [a, b, c, d, e, f, g, h, i]


def Showing_map():
    print(" " + str(a[0]) + "  |  " + str(a[1]) + "  |  " + str(a[2]) + "  |  " + str(a[3]) + "  |  " + str(a[4]) +
          "  |  " + str(a[5]) + "  |  " + str(a[6]) + "  |  " + str(a[7]) + "  |  " + str(a[8]))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(b[0]) + "  |  " + str(b[1]) + "  |  " + str(b[2]) + "  |  " + str(b[3]) + "  |  " + str(b[4]) +
          "  |  " + str(b[5]) + "  |  " + str(b[6]) + "  |  " + str(b[7]) + "  |  " + str(b[8]))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(c[0]) + "  |  " + str(c[1]) + "  |  " + str(c[2]) + "  |  " + str(c[3]) + "  |  " + str(c[4]) +
          "  |  " + str(c[5]) + "  |  " + str(c[6]) + "  |  " + str(c[7]) + "  |  " + str(c[8]))
    print("----------------|-----------------|----------------")
    print(" " + str(d[0]) + "  |  " + str(d[1]) + "  |  " + str(d[2]) + "  |  " + str(d[3]) + "  |  " + str(d[4]) +
          "  |  " + str(d[5]) + "  |  " + str(d[6]) + "  |  " + str(d[7]) + "  |  " + str(d[8]))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(e[0]) + "  |  " + str(e[1]) + "  |  " + str(e[2]) + "  |  " + str(e[3]) + "  |  " + str(e[4]) +
          "  |  " + str(e[5]) + "  |  " + str(e[6]) + "  |  " + str(e[7]) + "  |  " + str(e[8]))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(f[0]) + "  |  " + str(f[1]) + "  |  " + str(f[2]) + "  |  " + str(f[3]) + "  |  " + str(f[4]) +
          "  |  " + str(f[5]) + "  |  " + str(f[6]) + "  |  " + str(f[7]) + "  |  " + str(f[8]))
    print("----------------|-----------------|----------------")
    print(" " + str(g[0]) + "  |  " + str(g[1]) + "  |  " + str(g[2]) + "  |  " + str(g[3]) + "  |  " + str(g[4]) +
          "  |  " + str(g[5]) + "  |  " + str(g[6]) + "  |  " + str(g[7]) + "  |  " + str(g[8]))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(h[0]) + "  |  " + str(h[1]) + "  |  " + str(h[2]) + "  |  " + str(h[3]) + "  |  " + str(h[4]) +
          "  |  " + str(h[5]) + "  |  " + str(h[6]) + "  |  " + str(h[7]) + "  |  " + str(h[8]))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(i[0]) + "  |  " + str(i[1]) + "  |  " + str(i[2]) + "  |  " + str(i[3]) + "  |  " + str(i[4]) +
          "  |  " + str(i[5]) + "  |  " + str(i[6]) + "  |  " + str(i[7]) + "  |  " + str(i[8]))

def Solver():
    """
    1, check the same row and column.
    2, check the box where it's in.
    3, if there's only one left num then put in
    4, otherwise, pass it
    """
    
    # global alpha, a,b,c,d,e,f,g,h,i, box1,box2,box3,box4,box5,box6,box7,box8,box9
    # global a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9
    # global b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9
    # global c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8,c_9
    # global d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8,d_9
    # global e_1,e_2,e_3,e_4,e_5,e_6,e_7,e_8,e_9
    # global f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9
    # global g_1,g_2,g_3,g_4,g_5,g_6,g_7,g_8,g_9
    # global h_1,h_2,h_3,h_4,h_5,h_6,h_7,h_8,h_9
    # global i_1,i_2,i_3,i_4,i_5,i_6,i_7,i_8,i_9
 

    for i in range(len(alpha)):
        "to get a,b,c,d,e,f,g,h,i"

        for j in range(len(alpha[i])):
            "inside of a,b,c,d,e,f,g,h,i"
            "to find nums where it's empty"
            numbers = []

            for e in range(len(alpha[i])):
                "row"
                if not j == e:
                    if alpha[i][e] != " ":
                        if not alpha[i][e] in numbers:
                            numbers.append(alpha[i][e]) 

            for h in range(len(alpha)):
                "column"
                if not h == i:
                    if alpha[h][j] != " ":
                        if not alpha[h][j] in numbers:
                            numbers.append(alpha[h][j])

            if 0<=i<=2 and 0<=j<=2:
                for z in range(len(box1)):
                    if box1[z] != " ":
                        if not box1[z] in numbers:
                            numbers.append(box1[z])
            elif 0<=i<=2 and 3<=j<=5:
                for z in range(len(box2)):
                    if box2[z] != " ":
                        if not box2[z] in numbers:
                            numbers.append(box2[z])
            elif 0<=i<=2 and 6<=j<=8:
                for z in range(len(box3)):
                    if box3[z] != " ":
                        if not box3[z] in numbers:
                            numbers.append(box3[z])
            elif 3<=i<=5 and 0<=j<=2:
                for z in range(len(box4)):
                    if box4[z] != " ":
                        if not box4[z] in numbers:
                            numbers.append(box4[z])
            elif 3<=i<=5 and 3<=j<=5:
                for z in range(len(box5)):
                    if box5[z] != " ":
                        if not box5[z] in numbers:
                            numbers.append(box5[z])
            elif 3<=i<=5 and 6<=j<=8:
                for z in range(len(box6)):
                    if box6[z] != " ":
                        if not box6[z] in numbers:
                            numbers.append(box6[z])
            elif 6<=i<=8 and 0<=j<=2:
                for z in range(len(box7)):
                    if box7[z] != " ":
                        if not box7[z] in numbers:
                            numbers.append(box7[z])
            elif 6<=i<=8 and 3<=j<=5:
                for z in range(len(box8)):
                    if box8[z] != " ":
                        if not box8[z] in numbers:
                            numbers.append(box8[z])
            elif 6<=i<=8 and 6<=j<=8:
                for z in range(len(box9)):
                    if box9[z] != " ":
                        if not box9[z] in numbers:
                            numbers.append(box9[z])


            if len(numbers) == 8:
                for q in range(1,10):
                    if not q in numbers:
                        if alpha[i][j] == " ":
                            alpha[i][j] = q






Showing_map()
print("--------------------------------------------------------------")
Solver()
Solver()
Solver()
Solver()
Solver()
Showing_map()

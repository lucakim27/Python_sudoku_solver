a_1 = " "
a_2 = " "
a_3 = 3
a_4 = " "
a_5 = 4
a_6 = 2
a_7 = " "
a_8 = 9
a_9 = " "
b_1 = " "
b_2 = 9
b_3 = " "
b_4 = " "
b_5 = 6
b_6 = " "
b_7 = 5
b_8 = " "
b_9 = " "
c_1 = 5
c_2 = " "
c_3 = " "
c_4 = " "
c_5 = " "
c_6 = " "
c_7 = " "
c_8 = 1
c_9 = " "
d_1 = " "
d_2 = " "
d_3 = 1
d_4 = 7
d_5 = " "
d_6 = " "
d_7 = 2
d_8 = 8
d_9 = 5
e_1 = " "
e_2 = " "
e_3 = 8
e_4 = " "
e_5 = " "
e_6 = " "
e_7 = 1
e_8 = " "
e_9 = " "
f_1 = 3
f_2 = 2
f_3 = 9
f_4 = " "
f_5 = " "
f_6 = 8
f_7 = 7
f_8 = " "
f_9 = " "
g_1 = " "
g_2 = 3
g_3 = " "
g_4 = " "
g_5 = " "
g_6 = " "
g_7 = " "
g_8 = " "
g_9 = 1
h_1 = " "
h_2 = " "
h_3 = 5
h_4 = " "
h_5 = 9
h_6 = " "
h_7 = " "
h_8 = 2
h_9 = " "
i_1 = " "
i_2 = 8
i_3 = " "
i_4 = 2
i_5 = 1
i_6 = " "
i_7 = 6
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

boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

alpha = [a, b, c, d, e, f, g, h, i]


def Showing_map():
    global alpha, a,b,c,d,e,f,g,h,i, boxes, box1,box2,box3,box4,box5,box6,box7,box8,box9
    global a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9
    global b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9
    global c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8,c_9
    global d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8,d_9
    global e_1,e_2,e_3,e_4,e_5,e_6,e_7,e_8,e_9
    global f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9
    global g_1,g_2,g_3,g_4,g_5,g_6,g_7,g_8,g_9
    global h_1,h_2,h_3,h_4,h_5,h_6,h_7,h_8,h_9
    global i_1,i_2,i_3,i_4,i_5,i_6,i_7,i_8,i_9


    print(" " + str(a_1) + "  |  " + str(a_2) + "  |  " + str(a_3) + "  |  " + str(a_4) + "  |  " + str(a_5) +
          "  |  " + str(a_6) + "  |  " + str(a_7) + "  |  " + str(a_8) + "  |  " + str(a_9))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(b_1) + "  |  " + str(b_2) + "  |  " + str(b_3) + "  |  " + str(b_4) + "  |  " + str(b_5) +
          "  |  " + str(b_6) + "  |  " + str(b_7) + "  |  " + str(b_8) + "  |  " + str(b_9))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(c_1) + "  |  " + str(c_2) + "  |  " + str(c_3) + "  |  " + str(c_4) + "  |  " + str(c_5) +
          "  |  " + str(c_6) + "  |  " + str(c_7) + "  |  " + str(c_8) + "  |  " + str(c_9))
    print("----------------|-----------------|----------------")
    print(" " + str(d_1) + "  |  " + str(d_2) + "  |  " + str(d_3) + "  |  " + str(d_4) + "  |  " + str(d_5) +
          "  |  " + str(d_6) + "  |  " + str(d_7) + "  |  " + str(d_8) + "  |  " + str(d_9))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(e_1) + "  |  " + str(e_2) + "  |  " + str(e_3) + "  |  " + str(e_4) + "  |  " + str(e_5) +
          "  |  " + str(e_6) + "  |  " + str(e_7) + "  |  " + str(e_8) + "  |  " + str(e_9))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(f_1) + "  |  " + str(f_2) + "  |  " + str(f_3) + "  |  " + str(f_4) + "  |  " + str(f_5) +
          "  |  " + str(f_6) + "  |  " + str(f_7) + "  |  " + str(f_8) + "  |  " + str(f_9))
    print("----------------|-----------------|----------------")
    print(" " + str(g_1) + "  |  " + str(g_2) + "  |  " + str(g_3) + "  |  " + str(g_4) + "  |  " + str(g_5) +
          "  |  " + str(g_6) + "  |  " + str(g_7) + "  |  " + str(g_8) + "  |  " + str(g_9))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(h_1) + "  |  " + str(h_2) + "  |  " + str(h_3) + "  |  " + str(h_4) + "  |  " + str(h_5) +
          "  |  " + str(h_6) + "  |  " + str(h_7) + "  |  " + str(h_8) + "  |  " + str(h_9))
    print("- - - - - - - - | - - - - - - - - | - - - - - - - -")
    print(" " + str(i_1) + "  |  " + str(i_2) + "  |  " + str(i_3) + "  |  " + str(i_4) + "  |  " + str(i_5) +
          "  |  " + str(i_6) + "  |  " + str(i_7) + "  |  " + str(i_8) + "  |  " + str(i_9))


def Solver():
    """
    1, check the same row and column.
    2, check the box where it's in.
    3, if there's only one left num then put in
    4, otherwise, pass it
    """
    global alpha, a,b,c,d,e,f,g,h,i, boxes, box1,box2,box3,box4,box5,box6,box7,box8,box9
    global a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9
    global b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9
    global c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8,c_9
    global d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8,d_9
    global e_1,e_2,e_3,e_4,e_5,e_6,e_7,e_8,e_9
    global f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9
    global g_1,g_2,g_3,g_4,g_5,g_6,g_7,g_8,g_9
    global h_1,h_2,h_3,h_4,h_5,h_6,h_7,h_8,h_9
    global i_1,i_2,i_3,i_4,i_5,i_6,i_7,i_8,i_9

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
                "checking the nums"
                for q in range(1,10):
                    if not q in numbers:
                        if alpha[i][j] == " ":
                            alpha[i][j] = q






# def checker():
#     """
#     checking whether it's done or not.
#     """
#     for i in range(len(alpha)):
#         for j in range(len(alpha[i])):
#             print(alpha[i])



Showing_map()
print("--------------------------------------------------------------")

Solver()
Solver()

Showing_map()

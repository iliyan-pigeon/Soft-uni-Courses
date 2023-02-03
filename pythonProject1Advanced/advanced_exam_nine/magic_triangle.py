def get_magic_triangle(number):
    the_triangle = []
    for i in range(number):
        if i == 0:
            the_triangle.append([1])
        else:
            the_triangle.append([])
            for j in range(len(the_triangle)):
                if j == 0:
                    the_triangle[i].append(the_triangle[i-1][0])
                else:
                    combined = 0
                    combined += the_triangle[i-1][j-1]

                    if len(the_triangle) - 1 != j:
                        combined += the_triangle[i-1][j]

                    the_triangle[i].append(combined)
    print(the_triangle)


get_magic_triangle(10)
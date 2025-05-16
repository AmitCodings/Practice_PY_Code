class nested_loop():
    def print_triangle_pattern(self):

        rows = 5  # Number of rows

        for i in range(1, rows+1):  # Loop for rows
            for j in range(i):  # Loop for columns (stars)
                print("*", end=" ")  # Print star
            print()  # Move to the next line

    def print_number_triangle(self):

         row =5  #Number of rows

         for i in range(1, row+1):  # Loop for rows
             for j in range(i):     # Loop for columns
                print(f"{j+1}", end=" ")
             print()  # Move to the next line

    def print_reverse_triangle(self):
        row=5  #Number of rows
        for i in range(row,0,-1):
            for j in range(i):
                print(f"*",end=" ")
            print()

    def print_right_aligned_triangle(self):
        rows = 5
        for i in range(1, rows + 1):
            # Print spaces first
            for space in range(rows - i):
                print(" ", end=" ")
            # Then print stars
            for star in range(i):
                print("*", end=" ")
            print()

    def print_number_pattern_ascending(self):
        row =5
        for i in range (1,row +1):
            for j in range (i):
                print(f"{j+1}",end=" ")
            print()

    # def Centered_Star_Pyramid(self):
    #     row=5
    #     for i in range (1,row+1):
    #         #print Space
    #         for space in range(row-i):
    #             print(" ",end=" ")
    #         #Print star
    #         for star in range(i):
    #             print("*",end=" ")
    #         print()

    def Centered_Star_Pyramid(self):
        row = 5
        for i in range(1, row + 1):
            # Print spaces (decreasing as i increases)
            for space in range(row - i):
                print(" ", end=" ")
            # Print stars (increasing with i)
            for star in range(2*i -1):
                print("*", end=" ")
            print()  # Move to next line

    def number_centered_pyramid(self):
        row=5
        for i in range (1,row + 1):
        #print space
            for space in range (row-i):
                print(" ",end=" ")
        #Print number (increasing with i)
            for num in range(2*i -1):
                print(i, end =" ")
            print()

    def print_diamond_star_pattern(self):
        row=9
        for i in range (1,5):
        # print space
            for space in range (5-i):
                print(" ",end=" ")
            for space in range (1,9):
                     #Print star (increasing with i)
            for i in range (2*i-1):
                print("*", end=" ")
            for i in range (4,1):
                print("*", end=" ")
            print()



obj=nested_loop()
# obj.print_triangle_pattern()
# obj.print_number_triangle()
# obj.print_reverse_triangle()
# obj.print_right_aligned_triangle()
# obj.print_number_pattern_ascending()
# obj.print_reverse_number_triangle()
# obj.Centered_Star_Pyramid()
# obj.number_centered_pyramid()
# obj.print_diamond_star_pattern()
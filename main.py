keep_going = "yes"
while keep_going == "yes":

    def choose_exercise():
        exercise = int(input("\nSelect the recursive exercise \n1 - Sum of Positive Integers \n2 - Lowest Element and Logical Size \n3 - Potention Operation \n4 - Conversion to Binary \nSelect option: : "))
        return exercise
    
    exercise = choose_exercise()

    if exercise not in range (1,6):
        print("\nInvalid option! Please choose again.")
        exercise = choose_exercise()


    if exercise == 1:

        print("\nExercise 1 selected - Sum of Positive Integers")

        def integer_sum(x):
            if x == 1:
                return 1
            else:
                return (x + (integer_sum(x - 1)))
            
        x = int(input("\nEnter a positive integer: "))
        print(f"The sum of the integers between 0 and {x} is: {integer_sum(x)}")
            

    elif exercise == 2:

        print("\nExercise 2 selected - Lowest Element and Logical Size")

        def vector_treatment(x, y):
         if y == 0:
             return x[0]
    
         treated_vector = vector_treatment(x, y - 1)
    
         if x[y] < treated_vector:
             return x[y]
         else:
             return treated_vector


        x = list(map(int, input("List the elements of the vector, separated by spaces: ").split()))
        print(f"The vector's logical size is {len(x)} and its lowest element is {vector_treatment(x, len(x) - 1)}")


    elif exercise == 3:

        print("\nExercise 3 selected - Potention Operation")

        def power(x, y):
            if y == 0:
                return 1
            else:
                return (x * power(x, y - 1))
        
        x = int(input("\nEnter the base: "))
        y = int(input("Enter the exponent: "))
        print(f"The base {x} raised to the {y}° power is: {power(x, y)}")


    elif exercise == 4:

        print("\nExercise 4 selected - Greatest Common Divisor")
        
        def GCD(x, y):

            if y == 0:
                return x
            else:
                return GCD(y, x % y)
            
        print("Next, enter integers other than zero.")
        x = int(input("Enter the first element: "))
        y = int(input("Enter the second element: "))
        print(f"The GCD between {x} and {y} is: {GCD(x, y)}")


    else:

        print("\nExercise 5 selected - Conversion to Binary")

        def binary_converter(x):

            rest = x % 2
            rest_string = str(rest)

            if x < 2:
                return str(x)
            else:
                return (binary_converter(x // 2) + rest_string)

            
        x = int(input("\nEnter a decimal element: "))
        print(f"The binary representation of {x} is: {binary_converter(x)}")


    keep_going = input("\nDo you want to do another exercise? (yes/no): ").lower()
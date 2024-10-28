def calculate_bmi(height, weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))

    bmi = weight / (height * height)
    print("BMI=" + str(bmi))

    if bmi < 18.5:
        print("Weight Classification=Under Weight")
        return_value = -1
    elif 18.5 <= bmi <= 25.0:
        print("Weight Classification=Normal Weight")
        return_value = 0
    else:
        print("Weight Classification=Over Weight")
        return_value = 1
    
    return return_value

# Call the function and store the result
result = calculate_bmi(weight=57, height=1.73)
print("Return value=" + str(result))

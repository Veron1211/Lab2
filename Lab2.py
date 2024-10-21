def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    num_list = x.split(",")
    num_list = [float(num) for num in num_list]
    return num_list

def calc_average_temperature(num_list):
    total_sum=sum(num_list)
    avg_temp=total_sum/len(num_list)
    print("Average temperature="+str(avg_temp))

def calc_min_max_temperature(num_list):
    print("Min_Max temperature=["+str(min(num_list))+", "+str(max(num_list))+"]")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)

main()
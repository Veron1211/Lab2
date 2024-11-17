def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    num_list = x.split(",")
    num_list = [float(num) for num in num_list]
    return num_list

def calc_average(num_list):
    total_sum=sum(num_list)
    avg_temp=total_sum/len(num_list)
    return avg_temp

def find_min_max(num_list):
    return [min(num_list), max(num_list)]

def calc_median_temperature(num_list):
    num_list.sort()
    mid = len(num_list)//2
    res = (num_list[mid]+num_list[~mid])/2
    return res

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print("Average temperature="+str(calc_average(num_list)))
    print("Min_Max temperature="+str(find_min_max(num_list)))
    print("Median temperature="+str(calc_average(num_list)))

if __name__ == "__main__":
    main()
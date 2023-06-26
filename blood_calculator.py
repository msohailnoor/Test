def interface():
    print("Blood Test Analysis")
    keep_running = True

    while keep_running:
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Cholesterol")
        print("9 - Quit")
        choice = input("Enter your choice: ")

        if choice=='9':
            keep_running = False
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()
        elif choice == '3':
            cholesterol_driver()
    return


def accept_input(test_name):
    entry = input("Enter the {} test result: ".format(test_name))
    return int(entry)


def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(test_value, test_name, test_class)
    print(out_string)
    return


def check_HDL(HDL):
    if HDL >= 60:
        return "Normal"
    elif 40 <= HDL < 60:
        return "Borderline Low"
    else:
        return "Low"  

def HDL_driver():
    HDL_value = accept_input("HDL")
    classification = check_HDL(HDL_value)
    print_result("HDL", HDL_value, classification)


def check_LDL(LDL):
    if LDL < 130:
        return "Normal"
    elif 130 <= LDL < 159:
        return "Borderline high"
    elif 160 <= LDL < 189:
        return "high"
    else:
        return "very high"  

def LDL_driver():
    LDL_value = accept_input("LDL")
    classification = check_LDL(LDL_value)
    print_result("LDL", LDL_value, classification)


def check_cholesterol(cholesterol):
    if cholesterol < 200:
        return "Normal"
    elif 200 <= HDL < 239:
        return "Borderline high"
    else:
        return "high"

def cholesterol_driver():
    cholesterol_value = accept_input("cholesterol")
    classification = check_cholesterol(cholesterol_value)
    print_result("cholesterol", cholesterol_value, classification)



interface()
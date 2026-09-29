from vinutils import line


def process():
    data = input("Enter 2 numbers separated by comma: ")
    data = data.split(",")
    try:
        num = data[0]
        den = data[1]

        num = int(num)
        den = int(den)
        qot = num / den
        print(f"{num} / {den} = {qot}")
        # exit(1)
        # return
    except IndexError:
        print(f"Minimum 2 numbers expected. But you entered {len(data)} numbers.")
    except ValueError as err:
        print("Invalid type of data. Only integers are accepted.")
        print("Python says: " + str(err))
    # except ZeroDivisionError:
    #     print("Cannot divide by zero.")
    except Exception as err:
        print("Something went wrong!")
        print("Python error:", err)    
    finally:
        print("****************** This is always executed ******************")

    print(">>>>>>>>> This is the last statement in the process() function")



def do_stuff():
    print("doing stuff...")
    process()
    print("done doing stuff!")

def main():
    print("program execution started...")
    do_stuff()
    print("done with program execution")

line()
main()
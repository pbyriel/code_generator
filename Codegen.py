import random, csv, sys


# Func to get num of codes to be generated from user and test if integer
def get_num():
    num = input("How many codes: ")
    try:
        limit = int(num)
    except:
        wassup = input("Not an integer. Try again [Y/N]?")
        if wassup.lower().strip() == "y":
            get_num()
        else:
            sys.exit()
    return limit


# Func to get a name for the new file with new codes
def get_new_filename():
    name = input("Name for new file w/out .extension: ")
    return name.strip() + '.csv'


# Func to generate x no of codes and check if already in file
def generate_codes(limit, old_codes):
    code_length = 8
    num_generated = 0
    alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
    test_against = old_codes
    new_codes = []
    while num_generated < limit:
        code = ""
        t = ""
        for i in range(0, code_length):
            t = random.choice(['String', 'Integer'])
            if t == 'String':
                t = random.choice(["small", "CAPS"])
                x = random.choice(alfa)
                if t == "small":
                    code += x.lower()
                else:
                    code += x.upper()
            else:
                code += str(random.randint(1, 10))

        if (code in new_codes) or (code in test_against):
            pass
        else:
            new_codes.append(code)
            num_generated += 1
    print(new_codes)
    return new_codes


# Func to open code_file and import 
# list of existing codes
def get_old_codes(old_file):
    # in v2 add test for existence of ifile
    ifile = open(old_file, 'r')
    reader = csv.reader(ifile)
    codes = list(reader)
    ifile.close()
    return codes


# Func to write codes to old file and 
# generate new file with the new codes
def write_codes(new_codes, old_file, new_file):
    # add to csv file with old codes
    oldfile = open(old_file, "a")
    writer_old = csv.writer(oldfile, delimiter=',')
    for code in new_codes:
        writer_old.writerow([code])
    oldfile.close()
    # add to csv file with new codes
    newfile = open(new_file, "w")
    writer_new = csv.writer(newfile, delimiter=',')
    for code in new_codes:
        writer_new.writerow([code])
    newfile.close()


# Defines and runs main program below
def main():
    old_file = "codes.csv"
    new_file = get_new_filename()
    limit = get_num()
    old_codes = get_old_codes(old_file)
    new_codes = generate_codes(limit, old_codes)
    write_codes(new_codes, old_file, new_file)


if __name__ == "__main__":
    main()

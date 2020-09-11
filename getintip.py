import re
import sys

# this code just prints out the interface IP prefixes from CGX ION interfaces.

if __name__ == "__main__":
    # grab parameters
    if len(sys.argv) != 2:
        print("usage: getintip.py <original yaml file>")
        sys.exit(0)
    else:
        origfile = sys.argv[1]
        interfacestring = input("Enter comma separated list of interfaces (e.g. \"controller1, lan1, or 12 for bypass pair 12\": ")
        interfaceslist = re.sub(r'\s',"", interfacestring).split(",")
#        print("list of interfaces: ", interfaceslist)
        interfacesmap = {
            "controller1": "controller 1",
            "controller2": "controller 2",
            "lan1": "lan 1",
            "lan2": "lan 2",
            "lan3": "lan 3",
            "lan4": "lan 4",
            "lan5": "lan 5",
            "1": "\'1\'",
            "2": "\'2\'",
            "3": "\'3\'",
            "4": "\'4\'",
            "5": "\'5\'",
            "6": "\'6\'",
            "7": "\'7\'",
            "8": "\'8\'",
            "12": "\'12\'",
            "45": "\'45\'",
            "56": "\'56\'",
            "78": "\'78\'",
        }
        interfaceslist2 = []
        for interface in interfaceslist:
            if interface in interfacesmap:
                interfaceslist2.append(interfacesmap.get(interface))
#        print(interfaceslist2)

        file = open(origfile)
        for line in file:
            for interface in interfaceslist2:
                interface += ":"
                if interface in line:
                    interfacefound = True
#                    print(interfacefound)
                    for _ in range(25):
                        try:
                            line = file.__next__()
                            newfile = line.split(" ")
#                            if re.match('\wstatic_config:', line) != None:
#                                print("static_config")
                            for line in newfile:
                                if re.match('\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,32}', line) != None:
#                                    print("RE match")
                                    print(interface, end=" ")
                                    print(line, end="")
                        except StopIteration:
                            break

'''
        userstring_in_file = -1
        for line in open(origfile):
            for interface in interfaceslist:
                if interface in line:
                    userstring_in_file = 1

            if append_after_str in line:
                userstring_in_file = 1
                output.write(line)
                for addconfig in open(configfile):
                    output.write(addconfig)
                print("Done! New File is: ", outputfile)
                sys.exit(1)
            else:
                output.write(line)
        if userstring_in_file == -1:
            print("Error: String was not in file")
            sys.exit(0)
'''
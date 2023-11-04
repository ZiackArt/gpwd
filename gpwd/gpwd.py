import getopt, sys, helps
from itertools import product, combinations, combinations_with_replacement, permutations
from time import perf_counter

numbers_list = [0,1,2,3,4,5,6,7,8,9]
Output = False
key = 4
With_replacement = False
module_name = "Gpwd: Generate a list of passwords"
__version__ = "0.1"
Filename = "gpwd.txt"

def Arrangement(numbers_list=numbers_list, with_replacement=With_replacement,key=key,output=Output,filename=Filename):
    outputs = []
    if with_replacement:
        [outputs.append(list(p)) for p in product(numbers_list,repeat=key)]
    else:
        [outputs.append(list(p)) for p in permutations(numbers_list,key)]

    gpwd_call_function(output=output,filename=filename,outputs=outputs)

def Combinaition(numbers_list=numbers_list, with_replacement=With_replacement,key=key,output=Output,filename=Filename):
    outputs = []
    if with_replacement:
        [outputs.append(list(c)) for c in combinations_with_replacement(numbers_list,key)]
    else:
        [outputs.append(list(c)) for c in combinations(numbers_list,key)]
    
    gpwd_call_function(output=output,filename=filename,outputs=outputs)
   

def gpwd_call_function(output=Output,filename=Filename,outputs=None):
    if output:
        Output_f(outputs,filename=filename)
        # Show(outputs)
    else:
        # Output_f(outputs,filename=filename)
        Show(outputs)

def Output_f(outputs=[],filename=Filename):
    try:
        file = open(filename,"a")
        file.write(f"======================================SIZE {len(outputs)}======================================\n")
        [file.write(str(o)+"\n") for o in outputs]
        file.close()
        # print("___________END___________")
    except:
        print("=======Opening file error=======")

def Show(outputs=[]):
    print(f"======================================SIZE {len(outputs)}======================================")
    [print(o) for o in outputs]

def main():
    begin_perf = perf_counter()
    global With_replacement, key, Output, Filename
    Oparation = ""
    argumentList = sys.argv[1:]
    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:]

    if len(argumentList) == 0:
        print(f"{module_name} \nVersion: {__version__}")
        sys.exit()

    # Options
    options = "hacwk:o:v"
    long_options = ["Help", "Arrangement", "Combinaition","With_replacement","Output","Key","Version"]

    try: 
        # Parsing argument
        arguments, values = getopt.getopt(argumentList,options,long_options)
    
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        sys.exit()
        

    try:
        for currentArgument, currentValue in arguments:
            # print(currentArgument,currentValue)
            if currentArgument in ('-h',"--Help"):
                helps.Helps_menu()
            elif currentArgument in ("-a","--Arrangement"):
                Oparation = "Arrangement"
            elif currentArgument in ("-c","--Combinaition"):
                Oparation = "Combinaition"
            elif currentArgument in ("-w", "--With_replacement"):
                With_replacement = True
            elif currentArgument in ("-k", "--Key"):
                key = int(currentValue)
            elif currentArgument in ("-o", "--Output"):
                Output = True
                Filename = str(currentValue) if len(currentValue) >= 5 else Filename
            elif currentArgument in ("-v", "Version"):
                print(f"{module_name} \nVersion: {__version__}")
                sys.exit()
        
        if Oparation == "Arrangement":
            print("Wating....")
            Arrangement(with_replacement=With_replacement,key=key,output=Output,filename=Filename)
        elif Oparation == "Combinaition":
            print("Wating....")
            Combinaition(with_replacement=With_replacement,key=key,output=Output,filename=Filename)
    except getopt.error as err:
        if err:
            print(str(err))
        else:
            print("Unknown error")
    
    delta = perf_counter() - begin_perf
    print(f"Exécution time: {delta:.2f}s")
    
if __name__ == "__main__":
    main()
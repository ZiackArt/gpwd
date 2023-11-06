import getopt, sys
from itertools import product, combinations, combinations_with_replacement, permutations
from time import perf_counter
from colorama import Fore

numbers_list = [0,1,2,3,4,5,6,7,8,9]
Output = False
key = 4
With_replacement = False
module_name = "Gpwd: Password Combination Generator"
__version__ = "1.0"
Filename = "gpwd.txt"
helps = """
Run GPWD.
$ python3 gpwd -h
GPWD Passwords Combination Generator
Parameters
----------
`-h`  : to display Helps
`-v`  : to have a runing version of gpwd
`-a`  : to generate a Arangement 
`-c`  : to generate a Combination
`-k`  : (Optional) to give the number of digit (4 by default)
`-w`  : (Optional) to Arangement or Combination with replacement
`-o`  : (Optional) to give output file name ( put nan to use default name)
Good use
----------
Author : ZiackArt
GitHub : https://github.com/ZiackArt
"""

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
        file.write(f"______________________ SIZE {len(outputs)}______________________\n")
        [file.write(str(o)+"\n") for o in outputs]
        file.close()
        # print("___________END___________")
    except F:
        sys.exit(Fore.RED + "＞︿＜ Opening file error")

def Show(outputs=[]):
    print(Fore.CYAN + f"______________________SIZE {len(outputs)}______________________")
    [print(Fore.GREEN + str(o)) for o in outputs]


def main():
    begin_perf = perf_counter()
    global With_replacement, key, Output, Filename
    Oparation = ""
    argumentList = sys.argv[1:]
    # Remove 1st argument from the
    if len(argumentList) == 0:
        sys.exit(Fore.GREEN + f"{module_name} \nVersion: {__version__}")
    # Options
    options = "hacwk:o:v"
    long_options = ["Help", "Arrangement", "Combinaition","With_replacement","Output","Key","Version"]
    try: 
        # Parsing argument
        arguments, values = getopt.getopt(argumentList,options,long_options)
    except getopt.error as err:
        # output error, and return with an error code
        sys.exit(Fore.RED + str(err))
    
    try:
        for currentArgument, currentValue in arguments:
            if currentArgument in ('-h',"--Help"):
                sys.exit(Fore.CYAN + helps)
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
                sys.exit(Fore.GREEN + f"{module_name} \nVersion: {__version__}")
        
        if Oparation == "Arrangement":
            print("Wating....")
            Arrangement(with_replacement=With_replacement,key=key,output=Output,filename=Filename)
        elif Oparation == "Combinaition":
            print("Wating....")
            Combinaition(with_replacement=With_replacement,key=key,output=Output,filename=Filename)
    except getopt.error as err:
        if err:
            print(Fore.RED+"＞︿＜ "+str(err))
        else:
            print(Fore.RED+"＞︿＜ Unknown error")
    
    delta = perf_counter() - begin_perf
    print(f"Exécution time: {delta:.2f}s")

if __name__ == "__main__":
    main()
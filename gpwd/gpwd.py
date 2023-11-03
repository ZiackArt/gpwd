import getopt, sys
from itertools import product, combinations, combinations_with_replacement, permutations

numbers_list = [0,1,2,3,4,5,6,7,8,9]
Output = False
key = 4
With_replacement = False

def Arrangement(numbers_list=numbers_list, with_replacement=With_replacement,key=key,output=Output ):
    outputs = []
    if with_replacement:
        [outputs.append(list(p)) for p in product(numbers_list,repeat=key)]
    else:
        [outputs.append(list(p)) for p in permutations(numbers_list,key)]

    if output:
        Output_f(outputs)
        Show(outputs)
    else:
        Show(outputs)

def Combinaition(numbers_list=numbers_list, with_replacement=With_replacement,key=key,output=Output ):
    outputs = []
    if with_replacement:
        [outputs.append(list(c)) for c in combinations_with_replacement(numbers_list,key)]
    else:
        [outputs.append(list(c)) for c in combinations(numbers_list,key)]
    
    if output:
        Output_f(outputs)
        Show(outputs)
    else:
        Show(outputs)

def Output_f(outputs):
    try:
        file = open("Gpwd.txt","a")
        file.write(f"======================================SIZE {len(outputs)}======================================\n")
        for  output in outputs:
            file.write(str(output)+"\n")
        file.close()
        print("=======END=======")
    except:
        print("=======Opening fille error=======")

def Show(outputs):
    print(f"======================================SIZE {len(outputs)}======================================")
    for output in outputs:
        print(output)

def main():
    
    global With_replacement, key, Output
    Oparation = ""
    argumentList = sys.argv[1:]
    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:]
    # Options
    options = "hacwk:o"
    long_options = ["Help", "Arrangement", "Combinaition","With_replacement","Output","Key="]

    try: 
        # Parsing argument
        arguments, values = getopt.getopt(argumentList,options,long_options)
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        

    try:
        for currentArgument, currentValue in arguments:
            
            if currentArgument in ('-h',"--Help"):
                print("Help")
                break
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
        
        if Oparation == "Arrangement":
            print("Wating....")
            Arrangement(with_replacement=With_replacement,key=key,output=Output)
        elif Oparation == "Combinaition":
            print("Wating....")
            Combinaition(with_replacement=With_replacement,key=key,output=Output)
    except:
        print("ERREUR INCONU")
    
if __name__ == "__main__":
    main()
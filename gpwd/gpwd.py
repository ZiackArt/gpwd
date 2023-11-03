import getopt, sys
from itertools import product, combinations, combinations_with_replacement, permutations

helps = """
Run GPWD.

Checks for existence of username on various social media sites.

Keyword Arguments:
username               -- String indicating username that report
                        should be created against.
site_data              -- Dictionary containing all of the site data.
query_notify           -- Object with base type of QueryNotify().
                        This will be used to notify the caller about
                        query results.
tor                    -- Boolean indicating whether to use a tor circuit for the requests.
unique_tor             -- Boolean indicating whether to use a new tor circuit for each request.
proxy                  -- String indicating the proxy URL
timeout                -- Time in seconds to wait before timing out request.
                        Default is 60 seconds.

Return Value:
Dictionary containing results from report. Key of dictionary is the name
of the social network site, and the value is another dictionary with
the following keys:
    url_main:      URL of main site.
    url_user:      URL of user on site (if account exists).
    status:        QueryResult() object indicating results of test for
                account existence.
    http_status:   HTTP status code of query which checked for existence on
                site.
    response_text: Text that came back from request.  May be None if
                there was an HTTP error when checking for existence.
"""

numbers_list = [0,1,2,3,4,5,6,7,8,9]
Output = False
key = 4
With_replacement = False
module_name = "Gpwd: Generate a list of a lots of passwords"
__version__ = "0.1"

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
    options = "hacwk:ov"
    long_options = ["Help", "Arrangement", "Combinaition","With_replacement","Output","Key=","Version"]

    try: 
        # Parsing argument
        arguments, values = getopt.getopt(argumentList,options,long_options)
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        

    try:
        for currentArgument, currentValue in arguments:
            
            if currentArgument in ('-h',"--Help"):
                print (helps)
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
            elif currentArgument in ("-v", "Version"):
                print(f"{module_name} \nVersion: {__version__}")
        
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
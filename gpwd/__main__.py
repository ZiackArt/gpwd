#! /usr/bin/env python3
"""
Gpwd: Passwords Combination Generator

This module contains the main logic to generate a combinaisons of passwords
"""

import sys
from colorama import Fore


if __name__ == "__main__":
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]
    
    if sys.version_info < (3, 6):
        print(Fore.RED + "Gpwd requires Python 3.6+\nYou are using Python %s, which is not supported by Sherlock" % (python_version))
        sys.exit(1)

    import gpwd
    gpwd.main()
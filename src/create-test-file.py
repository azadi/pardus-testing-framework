#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
try:
    from lxml import etree
except ImportError:
    sys.exit("Error importing the 'lxml' library.\nYou need the 'lxml' library package installed to run this software.")
    
    
def print_tag(question):
    """Print the formatted prompt after accepting the input."""
    formattedQuestion = question + ':' + '\n'
    answer = raw_input(formattedQuestion)
    return answer


def main():
    """Ask the user for the type of testcase and output it accordingly."""
    while True:
        print 'What type of a testcase do you want?'
        print '1. Install\t2. GUI\n3. Shell\t4. Automated'
        try:
            answer = int(raw_input('Enter a value [1 - 4] > ')) 
        except ValueError:
            print '\nInvalid input. Enter a value between [1 - 4]\n'
            continue
        if not answer in range(1, 5):
            print '\nInvalid input. Enter a value between [1 - 4]\n'
            continue 
        # Extend the dictionary below to add more testcases
        testcases = {1: "install", 2: "gui", 3: "shell", 4: "automated"}
        return testcases[answer]


if __name__ == '__main__':
    welcomeMessage = 'Pardus Testing Framework'
    print welcomeMessage, '\n', len(welcomeMessage) * '-'
    main()
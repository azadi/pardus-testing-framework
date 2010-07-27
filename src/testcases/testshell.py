#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
from clcolorize import colorize


class TestShell:
    """This class is used to handle the testcase of shell, in which the user is
    told to run a certain command on and note down the output."""
    def __init__(self, element, text, report=None):
        self.element = element
        self.textlist = text
        self.report = list()
        
    def test_shell_main(self):
        """Print the text and ask the user to run the commands."""
        case = self.element.xpath('case')
        totalCases = len(case)
        counter = 0
        while counter < totalCases:
            print colorize('Case {0} of {1}', 'bold').format(counter+1, totalCases)
            print ''.join(self.textlist)
            for text in self.element.getiterator('command'):
                print colorize(text.text, 'yellow')
            # Get the observations
            print colorize('Enter your observation of the test:', 'bold')
            observation = raw_input('> ')
            if not observation == '':
                self.report.append('Case {0} Observation: {1}'.format(counter+1, observation))
            else:
                self.report.append('Case {0}: No observation entered.'.format(counter+1))
            print '\n'
            counter += 1        
        
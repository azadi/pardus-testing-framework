#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

from clcolorize import colorize


class TestGUI:
    """class for the testcase gui."""
    def __init__(self, element, packagelist, report=None):
        self.element = element
        self.packagelist = packagelist
        self.report = list()
        
    def test_gui_main(self):
        """Execute the gui test case and display the commands."""
        case = self.element.xpath('case')
        totalCases = len(case)
        counter = 0
        while counter < totalCases:
            print colorize('Case {0} of {1}',
                           'bold').format(counter+1, totalCases)
            print 'Package: ', colorize('{0}', 'bold').format(''.join(self.packagelist))
            downloadList = []
            for downloadTag in case[counter].getiterator('download'):
                downloadList.append(downloadTag.text)
            if downloadList:
                self.download_file(downloadList)
            textList = []
            for element in case[counter].getiterator('text'):
                textList.append(element.text)
            for number, element in enumerate(textList, 1):
                print colorize('{0}. ', 'bold').format(number), element
            raw_input('> Press ENTER to continue ')
            counter += 1
        print colorize('Enter your observation of the tests:', 'bold')
        observation = raw_input('> ')
        self.report.append(observation)
        
    def download_file(self, file):
        """Download a file using wget."""
        downloadFile = ['wget'] + ['-m'] + ['-nd'] + file
        fileName = os.path.basename(''.join(file))
        startwget = subprocess.call(downloadFile, stderr=open(os.devnull, 'w'))
        if startwget == 0:
            print colorize('{0}', 'bold').format(fileName), " downloaded to: '{0}'".format(os.getcwd())
            self.report.append('{0} downloaded to: {1}'.format(fileName, os.getcwd()))
        else:
            print "The file specified for the download does not exist."
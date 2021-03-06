#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from PyQt4 import QtCore, QtGui

from ui_main import Ui_Dialog


class Main(QtGui.QMainWindow):
    """class for creating a QDialog."""
    def __init__(self, element, packagelist, summary=None, report=None, package=None,
                                             checkcode=None, case=None,
                                             casecounter=None, totalcases=None):
        QtGui.QMainWindow.__init__(self)
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        # self.checkcode checks for premature exit of the application
        self.checkcode = 0
    
        self.element = element
        self.case = self.element.xpath('case')
        self.packagelist = packagelist
                
        self.casecounter = 0
        self.totalcases = len(self.case)
        
        self.summary = list()
        self.report = list()
        
        self.package = package
        
        if self.package is None:
            #  if the test is of shell type
            self.ui.type_label.setText('Shell Test')
            packageText = 'Packages: {0}'.format(', '.join(self.packagelist))
            for lst in (self.summary, self.report):
                lst.append(packageText)
            self.ui.text_edit.append("The following packages will be tested: " \
                                "<b>{0}</b>".format(', '.join(self.packagelist)))
            self.ui.text_edit.append("Press 'Start' to begin testing ...")
        else:
            # if the test is of gui type
            self.ui.type_label.setText('GUI Test')
            singlePackage = 'Package: {0}'.format(self.package)
            for lst in (self.summary, self.report):
                lst.append(singlePackage)
            self.ui.text_edit.append("The package <b>'{0}'</b> " \
                                          "will be tested".format(self.package))
            self.ui.text_edit.append("Press 'Start' to begin testing ...")
        
        self.connect(self.ui.next_button, QtCore.SIGNAL("clicked()"), self.next_case)
        self.connect(self.ui.save_button, QtCore.SIGNAL("clicked()"), self.get_text)
        
    def update_text(self):
        """Update the text by parsing through the case tag."""
        self.ui.text_observation.clear()
        self.ui.group_box.setTitle('Case {0} of {1}'.format(self.casecounter+1,
                                                            self.totalcases))
        if self.package is not None:
            self.ui.package_label.setText('Package: {0}'.format(self.package))
            self.ui.text_edit.clear()
            # get the list of files that were downloaded
            filesDownloaded = []
            for files in self.case[self.casecounter].iter('download'):
                filesDownloaded.append(files.text)
            if filesDownloaded:
                self.ui.text_edit.append("Using files in '{0}'".format(os.getcwd()))
            # get the text
            textList = []
            for text in self.case[self.casecounter].iter():
                if text.text.strip() == '':
                    continue
                if text.tag == 'link':
                    textList.append('{0}'.format(text.text))
                    continue
                if text.tag == 'download':
                    textList.append('{0}'.format(os.path.basename(text.text)))
                    continue
                textList.append(text.text)            
            if textList:
                self.ui.text_edit.append('')
            self.ui.text_edit.append('\n'.join(textList))
        else:
            self.ui.package_label.setText('Package(s): ' \
                                      '{0}'.format(', '.join(self.packagelist)))
            self.ui.text_edit.clear()
            # get the text
            textList = []
            for element in self.case[self.casecounter].iter('text'):
                textList.append(element.text)
            if textList:
                self.ui.text_edit.append('')
                for number, element in enumerate(textList, 1):
                    self.ui.text_edit.append('<b>{0}</b>. {1}'.format(number, element))
            # get the commands
            commandList = []
            for element in self.case[self.casecounter].iter('command'):
                commandList.append(element.text)
            if commandList:
                self.ui.text_edit.append('')
                self.ui.text_edit.append('{0}'.format('\n'.join(commandList)))
            
    def next_case(self):
        """Increment the case counter and display the next case."""
        if self.casecounter < self.totalcases:
            self.ui.next_button.setEnabled(True)
            self.ui.text_edit.setEnabled(True)
            self.ui.label.setEnabled(True)
            self.ui.yes_button.setEnabled(True)
            self.ui.no_button.setEnabled(True)
            self.ui.unable_button.setEnabled(True)
            self.ui.save_button.setEnabled(True)
            # update the text based on the testcase
            self.ui.next_button.setText('N&ext')
            self.update_text()            
            self.ui.next_button.setEnabled(False)
        else:
            self.ui.quit_button.setEnabled(True)            
            self.ui.text_observation.setEnabled(False)
            self.ui.label.setEnabled(False)
            self.ui.yes_button.setEnabled(False)
            self.ui.clear_button.setEnabled(False)
            self.ui.no_button.setEnabled(False)
            self.ui.label_observation.setEnabled(False)
            self.ui.unable_button.setEnabled(False)
            self.ui.next_button.setEnabled(False)
            # set the checkcode to 1 since everything is ok
            self.checkcode = 1            
            self.ui.package_label.setText('')
            self.ui.text_observation.setPlainText('')
            self.ui.text_edit.setText("End of package testing. " \
                                      "Press 'Finish' to exit.")
            self.ui.group_box.setTitle('Finished')

    def get_text(self):
        """Get the observation from the user."""
        if self.ui.yes_button.isChecked():
            self.report.append('Case {0} of {1}: Success'.format(self.casecounter+1,
                                                            self.totalcases))
            self.summary.append('Case {0} of {1}: Success'.format(self.casecounter+1,
                                                            self.totalcases))
        elif self.ui.unable_button.isChecked():
            failure_message = 'Case {0} of {1}: The user was unable to perform ' \
                        'this test'.format(self.casecounter+1, self.totalcases)
            for lst in (self.summary, self.report):
                lst.append(failure_message)
            observation = self.ui.text_observation.toPlainText()
            if observation == '':
                self.report.append('\tCase {0}: No observation ' \
                                          'entered.'.format(self.casecounter+1))
            else:
                self.report.append('\tCase {0} Observation: ' \
                                   '{1}'.format(self.casecounter+1, observation))
        elif self.ui.no_button.isChecked():
            self.report.append('Case {0} of {1}: Failed'.format(self.casecounter+1,
                                                          self.totalcases))
            self.summary.append('Case {0} of {1}: Failed'.format(self.casecounter+1,
                                                          self.totalcases))
            observation = self.ui.text_observation.toPlainText()
            if observation == '':
                self.report.append('\tCase {0}: No observation ' \
                                        'entered.'.format(self.casecounter+1))
            else:
                self.report.append('\tCase {0} Observation: ' \
                                   '{1}'.format(self.casecounter+1, observation))
        else:
            self.report.append('Case {0} of {1}: ' \
                               'No information entered'.format(self.casecounter+1,
                                                             self.totalcases))
            self.summary.append('Case {0} of {1}: Failed'.format(self.casecounter+1,
                                                             self.totalcases))
        # disable everything related to input
        self.ui.text_edit.setEnabled(False)
        self.ui.text_observation.setEnabled(False)
        self.ui.label.setEnabled(False)
        self.ui.yes_button.setEnabled(False)
        self.ui.clear_button.setEnabled(False)
        self.ui.no_button.setEnabled(False)
        self.ui.label_observation.setEnabled(False)
        self.ui.unable_button.setEnabled(False)        
        self.ui.save_button.setEnabled(False)        
        self.ui.next_button.setEnabled(True)
        self.casecounter += 1
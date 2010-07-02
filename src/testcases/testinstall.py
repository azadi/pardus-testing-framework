#! /usr/bin/env python
# -*- coding: utf-8 -*-

import string

from pisi.api import install
from pisi.api import list_available
from pisi.api import calculate_download_size

from pisi.errors import PrivilegeError

from clcolorize import colorize


class TestInstall:
    """class for the testcase install."""
    def __init__(self, packagelist, installedpackages, availablepackages):
        self.packagelist = packagelist
        self.installedpackages = installedpackages
        self.availablepackages = availablepackages
    
    def test_install_main(self):
        """Use the pisi api to install the packages"""
        # Packages which are in the testcase file and are not installed
        packagestNotInstalled = list(set(self.packagelist) - set(self.installedpackages))
        if not packagestNotInstalled:
            print colorize('All the required packages are installed.\n', 'green')
            return
        # Install only packages that are in all the repositories
        packagesNotInRepo = list(set(packagestNotInstalled) - set((self.availablepackages)))
        if packagesNotInRepo:
            print "The following packages were not found in the repository:", colorize('{0}', 'red').format(string.join(packagesNotInRepo, ', '))
        # Only try installing those packages which are in the repository
        finalPacakges = list(set(packagestNotInstalled) - set(packagesNotInRepo))
        totalPackages = len(finalPacakges)
        if totalPackages == 0:
            print colorize('No packages were installed.\n', 'green')
            return
        downloadSize = calculate_download_size(finalPacakges)[0]/(1024.0 * 1024.0)
        print "Number of packages to be installed: '{0}', total size: '{1:.2f} MB'".format(totalPackages, downloadSize)
        print 'Installing required packages, please wait ... '
        counter = 0 
        while counter < totalPackages:
            # Pisi installs new packages by using a list. However if we pass all the
            # packages as a single list, we don't have much control over the errors.
            # That is why pass a single package as a list here
            package = finalPacakges[counter]
            singlePackage = string.split(finalPacakges[counter])
            try:
                install(singlePackage)
            except PrivilegeError:      # in case the user doesn't have permission
                print colorize('Error: To install the packages, run the framework with root privileges.\n', 'red')
                return
            counter += 1
        print colorize("Finished installing the following packages: '{0}'\n", 'green').format(string.join(finalPacakges, ', '))
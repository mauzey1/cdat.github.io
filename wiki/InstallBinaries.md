## Install Binaries

**You will need admin privileges**

Current Version is: 1.2.0rc1

1. Download and untar the binaries best matching your OS.

        cd /
        sudo tar xjvf UV-CDAT-[version number]-[your OS here].tar.bz2

2. Mac and RedHAT6 **ONLY**
  * Download the tarsal containing the version of QT UVCDAT has been compiled against

            **RedHAT6**
            cd /
            sudo tar xjv qt-RH6-64bit-4.8.0.tar.bz2

            **Mac**
            double click the .dmg file and follow instructions

3. Additional things you might need
  * **Mac**: the mac build is picky about which gfortran make sure you get the dmg from the binaries website
  * **Linux**: make sure you have:

            gfortran
            libqt4-dev (if not under RH6)
            xorg-dev
            libxml2-dev
            libxslt2-dev
            sqlite3

4. Start enjoying UVCDAT:
  * GUI - /usr/local/uvcdat/[version number]/bin/uvcdat
  * bash/sh - You can run your old CDAT script via: First make sure your environment is set correctly:

            source /usr/local/uvcdat/[version number]/bin/setup_cdat.sh
            /usr/local/uvcdat/[version number]/bin/python [your_scritp_name_here].py

  * csh/tcsh - You can run your old CDAT script via: First make sure your environment is set correctly:

            source /usr/local/uvcdat/[version number]/bin/setup_cdat.csh
            /usr/local/uvcdat/[version number]/bin/python [your_scritp_name_here].py
  
* NOTE -On mac if you are using the vcs module you will need to start the scripts using "cdat" instead of python

            /usr/local/uvcdat/[version number]/Library/Frameworks/Python.framework/Versions/2.7/bin/cdat
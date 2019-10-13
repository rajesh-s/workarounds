#!/usr/bin/env python
""" Script to check for latest versions of Open Source HW tools """

import subprocess
VERILATOR_VERSION = subprocess.check_output("verilator -version | awk '{print $2}'", shell=True)
VERILATOR_REL = subprocess.check_output(r"git ls-remote --tags --sort=v:refname https://github.com/verilator/verilator.git | tail -n1 | sed 's/.*\///; s/\^{}//'", shell=True)
YOSYS_VERSION = subprocess.check_output(r"yosys -V | awk '{print $2}' | sed 's/+\(.*\)//'", shell=True)
YOSYS_REL = subprocess.check_output(r"git ls-remote --tags --sort=v:refname https://github.com/YosysHQ/yosys.git | tail -n1 | sed 's/.*\///; s/\^{}//'", shell=True)
print "Installed Verilator version: " + VERILATOR_VERSION + "Latest Available version: " + VERILATOR_REL
print "Installed Yosys version: " + YOSYS_VERSION + "Latest Available version: " + YOSYS_REL

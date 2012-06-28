# CTS Regression Test Plan Generating System
# Prepared by Kelly Lai

from bs4 import BeautifulSoup

prev_package_name = ''
package_list = []

#create the regression test plan file
output = open('ctsRegression.xml', 'w')
# insert starting initial code into the output xml file
output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
output.write('<TestPlan version="1.0">\n')

soup = BeautifulSoup(open("testResult.xml"))

# Find all the fail test cases
fail_cases_list = soup.find_all(result="fail")

# For every failed test case, find the package it belongs to 
for fail_cases in fail_cases_list:
    package = fail_cases.find_parent("testpackage")
    new_package_name = package['apppackagename']
    # write unique reference to the package into the output file 
    # without duplication
    if new_package_name != prev_package_name:  
        prev_package_name = new_package_name
        xml_text = '  <Entry uri="' + str(new_package_name) + '"/>\n'
        output.write(xml_text)
                
output.write('</TestPlan>\n')
output.close()

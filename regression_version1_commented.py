
# CTS Regression Test Plan Generating System
# Prepared by Kelly Lai

# output file should have the name testResult.xml
input = open('testResult.xml', 'r')
# output file should have the name ctsRegession.xml
output = open('ctsRegression.xml', 'w')

# insert starting initial code into the output xml file
output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
output.write('<TestPlan version="1.0">\n')

# initialize the type and value of the variable to be used
line = ''
package = ''
xml_text = ''
package_list = []
start_a_new_package = 1
no_of_failed_test_cases = 0       
# Keep checking how many test cases are failed, if the number of test cases 
# failed are over 1000, a message will be printed out, suggesting user not to
# perform regression test 

# check if the end of file is reached, and keep on reading 
# every line of the CTS report
while line.find('</TestResult>') is -1 :
    if line.find('<TestPackage') != -1:
        tmp = line.split('"')  
        package = tmp[3]                         
        #temporarily saving the package name in a variable 'package'
        start_a_new_package = 1                  
        #this variable is used to prevent redundant package name
        
    if (line.find('result="fail"') != -1): 

        no_of_failed_test_cases = no_of_failed_test_cases + 1

        if (start_a_new_package == 1):
            start_a_new_package = 0
            package_list.append(package)              
            xml_text = '  <Entry uri="' + package + '"/>\n'
            output.write(xml_text)
                
    line = input.readline()

if (no_of_failed_test_cases >= 1000) : 
    print 'Number of failed test cases exceeds 1000 '
    print 'regression testing is not suggested'

output.write('</TestPlan>\n')
input.close()
output.close()

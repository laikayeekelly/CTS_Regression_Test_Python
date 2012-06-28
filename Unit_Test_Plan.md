# Project part a - CTS Regression Testing

## CTS Regression test plan generating system
## Unit Test Plan

##  1. Purpose
The unit test plan is to describe the necessary tests that are used to test against the functionality of every components of the system.

## 2. Test Case Specification
### Component 
#### 2.1 Find out failed test cases
##### 2.1.1	Single failed test case
###### 2.1.1.1	Test Description
Generate a CTS Report with one failed test case and run the component with this CTS Report.
###### 2.1.1.2	Expected Result

A list of name of the failed test cases should be printed out that refer to the failed test case that is stated in the CTS Report. 

##### 2.1.2	Multi failed test cases
###### 2.1.2.1 Test Description
Generate a CTS Report with more than one failed test cases and run the component with this CTS Report
###### 2.1.2.2 Expected Result

A list of names of the failed test cases should be printed out that refer to the failed test cases that are stated in the CTS Report. 

##### 2.1.3	Zero failed test cases
###### 2.1.3.1 Test Description 
Generate a CTS Report with zero failed test cases and run the component with this CTS Report.
###### 2.1.3.2 Expected Result

A list of name of the failed test cases should be printed out that should be empty.


#### 2.2 Generating the regression test plan
##### 2.2.1	Successful Generation of test plan
###### 2.2.1.1 Test Description 
Run the component with a list of fail test cases.
###### 2.2.1.2	Expected Result
A test plan should be generated which should contain the reference identifiers referencing to the failed test cases, and in the correct format of XML document.
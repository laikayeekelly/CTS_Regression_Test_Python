# Project part a - CTS Regression Testing

## CTS Regression test plan generating system
## Design Specification


## 1. Purpose

The design specification is to define the design for all components of the CTS Regression test plan generating system.


## 2. System Design

The following is the Data Flow diagram for the design of the system.

![Alt text](https://github.com/laikayeekelly/CTS_Regression_Test/raw/master/Data_Flow_Diagram.JPG)




## 3. Component Design

### 3.1	Method
#### 3.1.1	Find out failed test cases
* Input: CTS Report
* Output: List of failed test cases
* Description of its function: Read the CTS Report given, and whenever a failed test case is found in the report, add the name of the package of this test case to the list and redundant package name should be avoided. 

#### 3.1.2	Generating the regression test plan
* Input: List of failed test cases
* Output: XML document of the regression test plan
* Description of its function: Generate a XML document that contains some reference identifiers referencing to the test packages that contain the failed test cases.

### 3.2	Data member
#### 3.2.1	List of failed test cases
A List of elements containing the name of the package that contains the failed test cases stated in the CTS Report



## 4. Command line interface design 

Before the system being run, make sure the input and output are in the expected format as specified in the requirement specification. The command ‘./regression ‘ is then used to execute the program, in which regression is the name for the program.

The Regression CTS test plan generated will have a file name regressionCTS.xml, and to run the CTS regression test using this test plan, the command “run cts –plan regressionCTS” will have to be used.
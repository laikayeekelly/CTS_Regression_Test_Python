# Project part a - CTS Regression Testing

## CTS Regression test plan generating system
## Integration Test Plan

##  1. Purpose
The integration test plan is to describe the necessary tests that are used to find out errors in the interactions between different components of the system.


## 2. Test Case Specification
### 2.1	Single failed test case
#### 2.1.1	Purpose
Ensure that the system can find out which test case failed when there’s one failed test case stated in the CTS Report
#### 2.1.2	Test Description 
Generate a CTS Report with one failed test case and run the system with this CTS Report.
#### 2.1.3	Expected Result
The test plan generated should only contain one reference identifier referencing to the failed test case.


### 2.2	Multi failed test cases
#### 2.2.1 Purpose
Ensure that the system can find out which test cases failed when there are more than one failed test cases stated in the CTS Report
#### 2.2.2 Test Description
Generate a CTS Report with more than one failed test cases and run the system with this CTS Report.
#### 2.2.3 Expected Result
The test plan generated should contain some reference identifiers referencing to the failed test cases.


### 2.3	Zero failed test cases
#### 2.3.1 Purpose
Ensure that the system can check that there are no test cases failed.
#### 2.3.2 Test Description 
Generate a CTS Report with zero failed test cases and run the system with this CTS Report.
#### 2.3.3 Expected Result
The test plan generated should not contain any reference identifiers referencing to the failed test cases


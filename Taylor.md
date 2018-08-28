# 1. Introduction

## 1.3 Glossary 

i) Databse - Collection of all the information monitered and used by the system.

ii) User - A member of faculty that is part of the administration or the mark review committe(The Dean, Head Of School and Lecturers).  

iii) Software Requirments Specification - A document that completely all of the functions of a proposed system and the constraint under which it must operate. For example this document.

iv) Faculty Of Science - A group of university scientific schools.

v) School - A department concerned with a specific discipline e.g School Of Mathematics.

vi) Member - An employee of the faculty of Science who is part of the mark review committe  e.g The Dean Of Faculty.

vii) Student - A registered individual for a specicific degree in the faculty.

viii) Vaadin - An open-source platform for web application development. 

ix) MySQL- 

## 1.4 References
IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications 
(Revision of IEEE Std 830-1993), IEEE Computer Society, 1998.

## 1.5 Overview of Documentation
The forthcoming section i.e. the Overall Description, will give a more broad explanation of how the product
is intended to work. It will delve into things like the product functions, design constraints, assumptions etc.
The  Specific Requirements section is a derivation of the preceeding section written specifically for developers
hence it uses a lot of technical jargon.

# 2. Overall description
## 2.1 Product perspective
### (a) Software Interface
#### Client on Internet
Web browser(IE12, Mozilla Firefox 49.0.1, Chrome 48.0 and above), OS (Windows Vista and above)
#### Client on Intranet
Web browser(IE12, Mozilla Firefox 49.0.1, Chrome 48.0 and above), OS (Windows Vista and above)
#### Web Server
Apache
#### Database Server
MySQL
#### Development end
Vaadin(Java, JavaScript, HTML, CSS, XML), phpMyAdmin, OS (Windows 7)
### (b) Hardware Interface
## 2.2 Product Functions
The system must:
(a) - Display a list of all registered students in the Science faculty.
    - View all the courses in which each student is enrolled for , marks , class attendance , progress etc. *insert picture of marks
(b) - Create a voting session for each individual course. 
    - Enable members to vote on progress outcome of each course. 
    - Count number of votes and decide on outcome. 
(c) - Update the student's status together with the mark.

## 2.3 User Characteristics 
The system will require basic computer skills and the use of a web browser.

Registrar/Dean - Will be facilitating the mark review process
Members- These include lecturers , school reprisentatives.

## 2.4 Constraints
The application will be web based and written in Java, JavaScript, HTML and CSS. Anyone willing to further devlop it will
have to know these technologies. 
And since it is web based, it will require internet access. The apps should be restricted to work on the Wits proxy only.
Furthermore, the system should only allow members of the Science Faculty to access it.

## 2.5 Assumptions and Dependencies
- The system assumes that the user has basic web-browser knowledge
- The software is meant to be run locally on the clients designated hardware in which the design of the system is based.
- A working java runtime environment version 1.8 and above is required.

## 2.6 Apportioning of Requirements 
 TO DO

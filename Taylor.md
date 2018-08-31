# 1. Introduction


## 1.1. Purpose
The purpose of this document is to present a detailed description of the Examiners' Board Meeting Web-Application. It will explain the purpose and features of the system, the interfaces of the system, what the system will do, the constraints under which it must operate and how the system will react to external stimuli. This document is intended for both the stakeholders and the developers of the system and will be proposed to the Faculty of Science for its approval.
## 1.2. Scope of Project
This software system will be a Web-Application System for the Faculty of Science. This system will be designed to maximize the productivity by providing tools to assist in automating the voting system review and publishing process, which would otherwise have to be performed manually. By maximizing the faculty registers work efficiency and production the system will meet the faculty’s needs while remaining easy to understand and use.

More specifically, this system is designed to allow the faculty to manage and communicate with a group of Administrators, Dean and Lecturers  to vote on the website. The software will facilitate voting between Administrators, Dean and Lecturers using the web-application. 

This is a Python web application that to allow members of the Science Faculty at Wits University to approve the promotion, failure or exclusion status of each student.
This application enables each student's marks to be viewed on any device used by the participants of the meeting.

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
 ## 2.6 Use Cases
 View Student
 Create Session
 Create Staff 
 View Staff
 Update Staff
 Archive Staff
 
 

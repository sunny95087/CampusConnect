# CampusConnect

CampusConnect is a planned web-based platform for managing common student and campus-related activities from one place.

This project is being developed as part of my internship work. The first few weeks are focused on understanding the problem, preparing requirements, designing the system, creating technical prototypes, and preparing a testing and quality assurance plan before starting the actual application development.

## Why I chose this project

In colleges, students often receive information from different places such as WhatsApp groups, emails, notice boards, forms and college websites. Service requests and complaints can also involve separate processes.

The idea behind CampusConnect is to bring some of these common activities together in one platform.

## What CampusConnect will do

### For Students

* Login to the platform
* View important announcements
* See upcoming college events
* Register for events
* Submit campus service requests
* Check the status of submitted requests
* Receive notifications
* Give feedback after a request is completed

### For Staff

* View service requests
* Check pending and assigned requests
* Update request status
* Add comments or updates
* Manage requests assigned to them

### For Admin

* Manage users and roles
* Manage announcements and events
* View basic statistics
* Manage basic platform settings
* View relevant activity/audit information

## Project Scope

For the first version, the project is limited to the main features mentioned above.

Features such as online fee payment, a complete LMS, mobile applications, live chat and AI-based counselling are not included in the first version. They can be considered later if the basic system works properly.

## Project Flow

The planned development process is:

**Planning → Requirements → Design → Prototype → Testing → Development → Deployment → Feedback**

The project is planned so that feedback from students and staff can be used to improve later versions.

## Week 1 – Project Planning and Requirements

During Week 1, I worked on:

* Understanding the problem
* Defining the project idea
* Identifying users and stakeholders
* Defining project scope
* Writing functional requirements
* Writing non-functional requirements
* Preparing user stories
* Identifying project risks
* Creating a project timeline
* Estimating resources and effort
* Planning the technology stack
* Preparing a basic testing plan

The complete Week 1 planning document is available in the `docs` folder.

## Week 2 – Design Documentation and Architecture

Week 2 focused on converting the requirements into a technical design for the proposed system.

I prepared documentation covering:

* High-level system architecture
* Frontend and backend structure
* Database design
* Module interactions
* Data flow
* REST API design
* Technology choices and their rationale
* Security design
* Performance and capacity assumptions
* Error handling
* Testing approach
* Technical risks
* Future scaling approach

### Week 2 Deliverables

* Design documentation
* System architecture diagram
* Data flow diagram
* Service request flow diagram

The Week 2 documentation and diagrams are available in the `docs` and `diagrams` folders.

## Week 3 – Feature Development and Code Prototype Documentation

Week 3 focused on creating a technical prototype plan for one of the key features identified during the earlier planning and design stages.

The selected feature was **Student Service Request Submission & Tracking**.

The Week 3 work covers:

* Feature objective and scope
* Code architecture
* Data structures
* Service request status workflow
* Request creation algorithm
* Input validation
* Duplicate request detection
* Error handling
* Notification workflow
* Security considerations
* Efficiency and performance improvements
* Pseudocode
* API contract
* Testing plan
* Prototype development effort estimation

### Week 3 Deliverables

* Feature prototype documentation
* Service request prototype flow diagram
* Pseudocode and algorithm design
* API prototype contract
* Testing plan

The Week 3 documentation is available in the `docs` folder and the prototype flow diagram is available in the `diagrams` folder.

## Week 4 – Software Testing and Quality Assurance

Week 4 focused on preparing a comprehensive Software Testing and Quality Assurance (QA) plan for CampusConnect.

The QA plan was prepared using the requirements, architecture and feature prototype developed during the previous weeks.

The Week 4 work covers:

* Unit testing
* Integration testing
* API testing
* System testing
* Regression testing
* Performance testing
* Security testing
* Usability and accessibility testing
* Test environment and test data
* Defect management
* QA metrics and success benchmarks
* Requirements-to-test traceability
* Release readiness criteria
* Continuous testing and CI/CD quality checks

Special attention was given to the **Student Service Request Submission & Tracking** feature because it involves authentication, validation, database operations, authorization, status transitions, notifications and error handling.

### Week 4 Deliverables

* Software Testing and QA Plan
* Detailed sample test cases
* Performance testing benchmarks
* Security testing checklist
* Requirements-to-test traceability
* Defect management process
* Release readiness checklist

The complete Week 4 QA and testing documentation is available in the `docs` folder.

## Requirements

Some important functional requirements are:

* User login and role management
* Student dashboard
* Announcements
* Events and event registration
* Service request submission
* Request tracking
* Staff request management
* Notifications
* Admin management

The project also considers non-functional requirements such as:

* Security
* Performance
* Usability
* Accessibility
* Availability
* Data backup
* Maintainability

## Planned Technology Stack

| Part              | Technology                  |
| ----------------- | --------------------------- |
| Frontend          | React + TypeScript          |
| Backend           | Java + Spring Boot          |
| Database          | PostgreSQL                  |
| Authentication    | OAuth2 / OpenID Connect     |
| API               | REST + JSON                 |
| API Documentation | Swagger / OpenAPI           |
| Version Control   | Git & GitHub                |
| Testing           | JUnit + API/Browser Testing |
| File Storage      | Object Storage              |

These technologies are currently planned for the project. Some choices may change later depending on implementation requirements.

## Initial System Assumptions

The current design uses some planning assumptions to make the architecture measurable:

* Around **1,000 registered users**
* Around **250–300 daily active users**
* Around **100 peak concurrent users**
* Normal API target of **95% requests within 2 seconds**
* Maximum attachment size of around **10 MB**
* Initial target of up to **100,000 service-request records**

These are design assumptions, not production measurements.

## Planned Timeline

The initial plan is for around 12 weeks.

* **Week 1:** Project planning and requirements
* **Week 2:** Design documentation and system architecture
* **Week 3:** Feature prototype and technical documentation
* **Week 4:** Software testing and quality assurance plan
* **Week 5:** Project setup, login and basic structure
* **Weeks 6–7:** Announcements and events
* **Weeks 8–9:** Service request system
* **Week 10:** Admin features and notifications
* **Week 11:** Testing and pilot testing
* **Week 12:** Deployment and documentation

The timeline may change once actual development starts.

## Repository Structure

```text
CampusConnect/
│
├── README.md
│
├── docs/
│   ├── Week_1_Project_Planning_CampusConnect.docx
│   ├── Week_2_Design_Documentation_Architecture_CampusConnect.docx
│   ├── Week_3_Feature_Prototype_Documentation.docx
│   ├── Week_4_Software_Testing_QA_Plan_CampusConnect.docx
│   └── campusconnect_lifecycle.png
│
├── diagrams/
│   ├── system-architecture.png
│   ├── data-flow.png
│   ├── service-request-flow.png
│   └── service-request-prototype-flow.png
│
├── requirements/
│   └── requirements.md
│
├── planning/
│   └── project-timeline.md
│
└── .gitignore
```

More folders will be added when actual development starts.

## Current Status

**Completed:**

* Week 1 – Project Planning and Requirements Analysis
* Week 2 – Design Documentation and Architecture Planning
* Week 3 – Feature Development and Code Prototype Documentation
* Week 4 – Software Testing and Quality Assurance Plan

**Next step:**

Start the basic project setup and begin implementing the planned system structure.

## Project Note

CampusConnect is currently a hypothetical project created for my internship task.

The project plan, requirements, architecture, timeline, technology choices, feature prototypes and testing plan are proposed as part of the internship exercises. Actual application implementation will begin in the upcoming weeks.

---

**Created by Sunny**

Engineering Student | Internship Project

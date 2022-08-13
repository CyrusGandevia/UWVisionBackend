# UWVision's new Backend Service
TODO: Table of contents

## Overview
This is a scalable Django service intended to handle variable amounts of traffic and deal with a continuously growing user base. The server itself is hosted on AWS EC2, the Postgres DBs are hosted on AWS RDS, and the static file storage is supported through AWS S3. 

We employ AWS Elastic Beanstalk to abstract away the complexities involved with load balancing, auto-scaling, maintaining multiple environments (testing, production), as well as orchestrating deployments between AWS EC2, RDS, and S3. 

A high level overview of this service's architecture can by explained by the following diagram:

![image](https://user-images.githubusercontent.com/28494892/184505244-c222785e-05b5-4f52-9c6c-3e68a7f615e0.png)

*(diagram credits go to https://realpython.com)*


## What happened to the old service?
Initially, UWVision's backend service was an Express.js service, using MongoDB Atlas to host a (noSQL) document database in the cloud. However, there were a few reasons for why we decided to move away from this old service's architecture:
- Hosting costs for MongoDB Atlas proved to be more expensive than we were comfortable with. We found AWS Elastic Beanstalk to give us more flexibility with tuning the parameters (load balancing, cluster tiers, etc...) that allowed us to control our costs more precisely. However, this did mean we'd also need to have a more involved role with maintenance of the service, which we didn't mind.

- Our initial choice to go with a document database was because of the flexibility it provided. We liked that it didn't have a rigid schema, meaning that we didn't have to deal with the task of constantly creating migrations. However, Django's ability to automatically detect changes in the schema and generate migrations basically made this a non-issue.

- Similarly, while the unstructured, schema-free data model was initially a positive, we realized over time that the relational model would be a natural fit because our data had many relations (ex. companies and jobs, jobs and salaries, jobs and reviews, jobs and interview questions, etc...). These relations could be easily expressed using foreign key relationships and proved to be more organized than the document database, which started to become quite overwhleming as we had more relationships to express.

- Django's admin panel and permission classes abstraction proved to be extremely beneficial.

## Environments
- TODO: Add links to the test and prod panel
- TODO: Add base URLs for test and prod environment
- TODO: AWS EB Env specific configs
- TODO: Add Route53 explanation (including domain and nameservers) and HTTPS load balancing explanation 
- TODO: Talk about whitelisting and CORS allowed

## API Documentation
(high-level as the apiviews and URL files are self explanatory, include hyperlinks)

## Pending features



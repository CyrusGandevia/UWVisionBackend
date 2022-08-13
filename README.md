# UWVision's new Backend Service
This is a scalable Django service intended to handle variable amounts of traffic and deal with a continuously growing user base. The server itself is hosted on AWS EC2, the Postgres DBs are hosted on AWS RDS and the static file storage is supported through AWS S3. 

We employ AWS Elastic Beanstalk to abstract away the complexities involved in load balancing, auto-scaling, mainting multiple environments (testing, prod), as well as orchestrating deployments between AWS EC2, RDS, and S3. 

A high level overview of this service's architecture can by explained by the following diagram:

![image](https://user-images.githubusercontent.com/28494892/184505244-c222785e-05b5-4f52-9c6c-3e68a7f615e0.png)

*(diagram credits go to https://realpython.com)*


## What happened to the old one?

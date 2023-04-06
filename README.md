# de_zoomcamp_project

# What is it about?

This project explores protected areas' types and years of enactment of that status based on The World Database on Protected Areas (WDPA).

# What questions is this project trying to answer?

Keeping in mind that expression 'protected areas' more or less on hearing, it would be interesing to know:
1. What are the most common protected areas' types?

Here in project protected areas with explicitly defined year of status are only viewed, so this question can be answered too:

2. What dynamics of such statuses enactment per decades?

# How to run it?

Follow the instructions:
1. Create Google Cloud Platform (GCP) account;
2. Create GCP project;
3. GCP console (left menu) -> APIs & Service -> Library -> Search engine ('
Identity and Access Management (IAM) API') ->  Enable -> Create credentials;
4. Create serivce account (click 'application data', pick roles 'BigQuery Admin', 'Storage Admin', 'Storage Object Admin');
5. GCP console (left menu) -> IAM & Admin -> Service Accounts -> Select recently created -> Sidebar menu -> 'Manage keys' -> 'Add key' -> 'Create new key' -> 'JSON' -> Create;
6. GCP console (left menu) -> Compute Engine -> VM instances -> Enable API -> Create instance -> Ubuntu (recommended);
7. Create a folder '.ssh' in your home directory on local machine;
8. Generate ssh keys (in a folder '.ssh'). Enter in CLI: `ssh-keygen -t rsa -f gcp -C your_name -b 2048`;
9. Run this command in terminal: `cat gcp.pub`;
10. Copy output;
11. Open in GCP console 'Compute Engine' -> 'Metadata' -> 'SSH KEYS' -> 'ADD SSH KEYS';
12. Paste the output from step 10 there;
13. You can enter VM via this command: `ssh -i ~/.ssh/gcp your_name@External_IP_of_your_VM`

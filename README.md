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
13. You can enter VM via this command: `ssh -i ~/.ssh/gcp your_name@External_IP_of_your_VM`;
14. Enter VM;
15. Download the JSON credentials and save it: `~/gc/your_credentials.json`;
16. Run this commands:

`export GOOGLE_APPLICATION_CREDENTIALS=<path_to_your_credentials>.json`

`gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS`

17. Create a folder 'data' in home directory;
18. Clone repository (also in home directory):

`git clone https://github.com/lantenak/de_zoomcamp_project`

19. Download Anaconda for Linix:

`wget https://repo.anaconda.com/archive/Anaconda3-2023.03-Linux-x86_64.sh`

`bash Anaconda3-2023.03-Linux-x86_64.sh`

20. Logout and login to make sure Anaconda works;
21. Go to `~/de_zoomcamp_project/prefect/` and run the command: `pip install -r requirements.txt`;
22. Run this commands:

`pip install prefect-dbt`

`pip install dbt-bigquery`

23. Create a folder 'bin' in home directory;

24. Install Terraform:

`cd ~/bin`

`wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg`

`echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list`

`sudo apt update && sudo apt install terraform`

`terraform -version`

25. To initiate, plan and apply the infrastructure, adjust and run the following Terraform commands:

`~/de_zoomcamp_project/terraform/`

`terraform init`

`terraform plan -var="project=<your-gcp-project-id>"`

`terraform apply -var="project=<your-gcp-project-id>"`

26. 

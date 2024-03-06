Azure RM Python Pulumi Program
This repository contains a Pulumi program for deploying a robust Azure infrastructure using Python. The infrastructure includes a resource group, a storage account, an App Service Plan, a Function App, a Virtual Network (VNet), a Network Security Group (NSG), a Public IP address, and an SQL Server with a SQL Database.

Prerequisites
Pulumi
Azure CLI
Python 3.x
Setup
Clone the Repository

Start by cloning this repository to your local machine.

bash
Copy code
git clone <repository-url>
cd <repository-name>
Login to Pulumi

Ensure you're logged into Pulumi using the CLI.

bash
Copy code
pulumi login
Configure Azure

Make sure you're logged into Azure CLI and have selected the correct subscription.

bash
Copy code
az login
az account set --subscription "<Your-Subscription-ID>"
Install Dependencies

Install the required Python packages.

bash
Copy code
pip install -r requirements.txt
Deploying the Infrastructure
To deploy your infrastructure, follow these steps:

Set Up Pulumi Configuration

Configure the Azure region (adjust the value as needed).

bash
Copy code
pulumi config set azure-native:location uaenorth
Preview the Deployment

Preview the changes Pulumi will perform.

bash
Copy code
pulumi preview
Deploy

To deploy the infrastructure, execute the following command:

bash
Copy code
pulumi up
Review the plan and confirm the deployment by selecting yes.

Cleanup
To destroy the resources, use the following command:

bash
Copy code
pulumi destroy
Confirm the deletion by selecting yes. This will remove all resources managed by this Pulumi program from your Azure account.

Note
This Pulumi program is designed for demonstration purposes and includes features like resource protection to prevent accidental deletion. Adjust the configurations as necessary for production use, and always review best practices for security and compliance.

Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

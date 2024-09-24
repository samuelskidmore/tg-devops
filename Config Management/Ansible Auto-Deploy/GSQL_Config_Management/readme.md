TigerGraph Configuration Management
This project utilizes Ansible to automate the configuration management of TigerGraph instances.

Table of Contents
Overview
Requirements
Installation
Usage
Configuration
Tasks
License
Overview
This project configures various settings for TigerGraph using Ansible playbooks. It aims to ensure that the desired configurations are applied consistently across multiple TigerGraph instances.

Requirements
Ansible (version 2.10 or higher)
SSH access to the TigerGraph server
Appropriate user privileges
Installation

Install Ansible:


pip install ansible
Usage
Run the Ansible playbook to apply configurations:


ansible-playbook -i inventory.ini playbook.yml

To run Ansible in check mode, you can use the --check flag when running a playbook. Here's an example command:

ansible-playbook playbook.yml --check
This command will run the specified playbook in check mode, showing you what changes would occur without actually applying them.

Additionally, if you want to see the detailed differences of what would be changed, you can combine --check with the --diff flag:


ansible-playbook playbook.yml --check --diff
This will show the differences between the current state and the state that would be achieved by running the playbook, which is especially useful for configuration management tasks.





Configuration
The configurations are defined in YAML files located in the configs directory:

enable_configs.yml: Contains settings that are to be enabled.
other_configs.yml: Contains additional configurations.
Tasks
The playbook performs the following tasks:

Debug the current PATH environment variable.
Check and set enable configurations.
Check and set other configurations.
Apply configuration changes if needed.
Restart services if configurations were applied.


05b6a289-1740-4520-aff2-316e16cc3995
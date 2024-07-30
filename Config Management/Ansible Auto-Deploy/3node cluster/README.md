# TigerGraph Ansible Installation

This project contains Ansible playbooks for automating the installation and configuration of TigerGraph on remote servers. It simplifies the process of setting up TigerGraph environments, ensuring consistency across installations.

## Prerequisites

Before you begin, ensure you have the following:
- Ansible installed on your control machine.
- Access to the target server(s) with SSH.
- The target server(s) are running a supported Linux distribution.
- You have the necessary permissions to execute commands as `sudo` on the target server(s).

## Getting Started

1. **Clone this repository** to your local machine or control node where Ansible is installed.

    ```bash
    git clone <repository-url>
    cd <repository-dir>
    ```

2. **Set up your inventory** by editing the `hosts.ini` file. Replace the placeholder values with your server's details.

    ```ini
    [tigergraph_servers]
    server1 ansible_host=your_server_ip ansible_user=your_user ansible_ssh_private_key_file=path_to_your_pem_file
    ```

3. **Review the playbook** `install_tigergraph.yml` to ensure it matches your installation requirements. You may need to adjust the TigerGraph version or installation parameters.

## Running the Playbook

To install TigerGraph on your target server(s), run the following command:

```bash
ansible-playbook -i hosts.ini install_tigergraph_3cluster.yml
ansible-playbook -vvv -i hosts.ini install_tigergraph_3cluster.yml
for verbose

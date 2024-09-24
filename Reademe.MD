# TigerGraph Multi-Version Docker Setup

This project uses Docker Compose to run multiple versions of TigerGraph (3.6, 3.7, 3.8, 3.9, 3.10, and 4.1) on different ports. Each version of TigerGraph has its own container, port forwarding, and data volume.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

Make sure both Docker and Docker Compose are installed and properly configured on your machine before proceeding.

## Setup

1. Clone this repository or copy the `docker-compose.yml` file to your working directory.

2. Adjust the volume paths if needed. By default, data is stored in subdirectories under `~/data/` (e.g., `~/data/tg36` for TigerGraph 3.6).

3. Run the following command to start all the TigerGraph containers:

    ```bash
    docker-compose up -d
    ```

4. Verify the containers are running by executing:

    ```bash
    docker ps
    ```

## Port Forwarding

Each TigerGraph version is mapped to different ports to avoid conflicts:

- **TigerGraph 3.6**
  - SSH: `14026 -> 22`
  - UI: `9001 -> 9000`
  - REST API: `14241 -> 14240`

- **TigerGraph 3.7**
  - SSH: `14027 -> 22`
  - UI: `9002 -> 9000`
  - REST API: `14242 -> 14240`

- **TigerGraph 3.8**
  - SSH: `14028 -> 22`
  - UI: `9003 -> 9000`
  - REST API: `14243 -> 14240`

- **TigerGraph 3.9**
  - SSH: `14029 -> 22`
  - UI: `9004 -> 9000`
  - REST API: `14244 -> 14240`

- **TigerGraph 3.10**
  - SSH: `14030 -> 22`
  - UI: `9005 -> 9000`
  - REST API: `14245 -> 14240`

- **TigerGraph 4.1**
  - SSH: `14031 -> 22`
  - UI: `9006 -> 9000`
  - REST API: `14246 -> 14240`

You can access each version’s web UI by visiting `http://localhost:<port>` where `<port>` is the port number for the respective version (e.g., `http://localhost:9001` for TigerGraph 3.6).

## Data Storage

Each TigerGraph instance is configured with its own data storage to prevent interference between versions:

- **TigerGraph 3.6**: Data stored at `~/data/tg36`
- **TigerGraph 3.7**: Data stored at `~/data/tg37`
- **TigerGraph 3.8**: Data stored at `~/data/tg38`
- **TigerGraph 3.9**: Data stored at `~/data/tg39`
- **TigerGraph 3.10**: Data stored at `~/data/tg310`
- **TigerGraph 4.1**: Data stored at `~/data/tg41`

## Stopping and Restarting Containers

To stop all containers, run:

```bash
docker-compose down

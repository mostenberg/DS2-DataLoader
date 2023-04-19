# Section 4: Linode CLI

## Purpose

Install the Linode Command Line Interface (CLI) to make it easy to interact with Linode via the command line.
Become familiar with the Linode Command Line Interface.
Learn a way to create more users so your colleagues can also login to Linode.

## Install and Configure Linode-cli (Option 1: on local system)

1. Requires python3 and pip3. Check if installed in terminal with:
   `python3 --version`
   `pip3 --version`
   If python3 or pip3 not installed:
   Installation instructions: https://www.linode.com/docs/products/tools/cli/guides/install/

After python3 and pip 3 are installed, install Linode CLI with command:
`pip3 install linode-cli --upgrade`

Configure linode-cli with command:
`linode-cli configure`

    - Set default Region as: us-southeast
    - Set default Linode size as (1) g6-1-nanode
    - Set default linux flavor as (34) Ubuntu22.1
    - Set default user as (1) \<your username>

### Install and configure Linode CLI (Option2: on a Linux Instance)

(Used if you don't want to make modifications to your local machine)

1. Create a linode instance by going to 'Linodes -> Create Linode'. Select
   - Images: Ubuntu 22.10
   - Region: Atlanta, GA
   - Linode Plan: Shared CPU 1 GB Nanode
   - Linode Label: \<yourname>-cli
   - Enter a root password (and remember it! )
   - Click on 'Create Linode
2. In Linode Cloud Console, generate a token as follows:
   - Click username in upper right corner.
   - Click on 'API tokens'
   - Click on 'Create a personal access token'
     - Expiry: 6 months
     - Access Restrictions: None
     - Click on 'Create Token'
3. SSH into your linode instance and install linode-cli:
   - `sudo apt update`
   - `sudo apt install python3-pip`
   - `pip3 install linode-cli --upgrade`
   - `linode-cli configure`
     - Enter your download token
     - Default Region: Select '3 - ap-southeast'
     - Default Instance: Select '1-g6-nanode-1'
       Default Image: Select '34 - linode/ubuntu 22.10'

## Using the Linode CLI

1. User management (create user)

   - List current linode users (linode-cli users list)
   - Check for required field to create user by typing ‘linode-cli users create --help’’
   - Create an additional unrestricted user called ‘yourname-cli’ with your email address with : linode-cli users create --username pickAUsername --email youremail --restricted false
   - List users with ‘linode-cli users list’ and confirm your new userid is in the list.

2. Instance Creation

   - List existing linode regions with linode-cli regions list Note the region name for Atlanta.
   - List existing linode types with linode-cli linodes list . Note node type for smallest nanodes.
   - List help on node creation with `linode-cli linodes create --help` . Note required fields format
   - Create a small nanode instance in Atlanta with label ‘<myname>-cli-instance’ and root password ‘NiceLongPassword!’ with command: `linode-cli linodes create --type g6-nanode-1 --region us-southeast --root_pass NiceLongPassword! --label  <yourname-cli-instance>`

3. Instance Cleanup (optional..but recommended so you don’t leave systems running )
   - List all existing linode instances with `linode-cli linodes list` . Note instance id's.
   - Remove all instances (one at a time) with `linode-cli linodes delete <instanceid>`

# Section 2: Setup an ELK server

### Purpose

Become familiar with the Akamai Control Center (Linode) user interface by deploying an ELK stack server using a stack script.

## Steps

1. Login to Linode.
2. Click on ‘Create Linode’
3. Click on tab ‘Stack-Scripts -> Community Stack Scripts’
4. Search for stack script ‘DataStream2’ by ‘hokamoto’
5. Enter and remember fields for:
   - Password for elastic user
   - Name of ds2user (prolly use ‘ds2user’)
   - Password for ds2user
   - Ubuntu 22.04
   - Region: Atlanta
   - Instance Size: Dedicated 8GB Instance
   - Label: elk-\<yourname>-\<mm-dd-yy>
   - Root password (make sure it’s something you remember)
6. Click ‘Create Linode’
7. Open LISH console to view screen as Linode launched.
8. Process will takes around 8 minutes. Watch in LISH to view progress.
9. Click on instance and go to ‘network’ tab and use reverse dns as hostname of your instance
10. Open browser and go to: \<yourHostname>:5601 . Should see Elastic login prompt
11. Login with username ‘elastic’ and password you entered during setup.
12. Go to ‘Left-navigation -> Analytics -> Dashboard and click on ‘Akamai’ dashboard (will open with no data yet)
13. SUCCESS!!! SECTION 2 COMPLETED.

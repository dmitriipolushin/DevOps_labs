# Playbook deploy

```
┌─[dmitriipolushin@MacBook-Air-Dmitrij] - [~/Innopolis/DevOps/DevOps_labs/ansible] - [2629]
└─[$] ansible-playbook -i .inventory/default.yml playbooks/dev/main.yml

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Load OS-specific vars.] *****************************
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : include_tasks] **************************************
included: /Users/dmitriipolushin/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for dmitriipolushin@130.193.48.228

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *****************
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ***
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Add Docker apt key.] ********************************
changed: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Add Docker repository.] *****************************
changed: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Install Docker packages.] ***************************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***
changed: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Install docker-compose plugin.] *********************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

RUNNING HANDLER [geerlingguy.docker : restart docker] **************************
changed: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : include_tasks] **************************************
included: /Users/dmitriipolushin/.ansible/roles/geerlingguy.docker/tasks/docker-compose.yml for dmitriipolushin@130.193.48.228

TASK [geerlingguy.docker : Check current docker-compose version.] **************
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : set_fact] *******************************************
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Delete existing docker-compose version if it's different.] ***
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Install Docker Compose (if configured).] ************
changed: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [dmitriipolushin@130.193.48.228]

PLAY RECAP *********************************************************************
┌─[dmitriipolushin@MacBook-Air-Dmitrij] - [~/Innopolis/DevOps/DevOps_labs/ansible] - [2629]
```

# Playbook list

```
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "dmitriipolushin@130.193.48.228"
        ]
    }
}
```

# Docker deploy

```

TASK [geerlingguy.docker : Install docker-compose plugin.] **********************************************************************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **********************************************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***************************************************************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Configure Docker daemon options.] ********************************************************************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *******************************************************
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***************************************

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************
included: /Users/dmitriipolushin/.ansible/roles/geerlingguy.docker/tasks/docker-compose.yml for dmitriipolushin@130.193.48.228

TASK [geerlingguy.docker : Check current docker-compose version.] ***************************************************************
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : set_fact] ********************************************************************************************
ok: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Delete existing docker-compose version if it's different.] *******************************************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Install Docker Compose (if configured).] *************************************************************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Get docker group info using getent.] *****************************************************************
skipping: [dmitriipolushin@130.193.48.228]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ********************************************

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************
skipping: [dmitriipolushin@130.193.48.228]

TASK [../../roles/deploy_python_app : Pull docker image] ************************************************************************
changed: [dmitriipolushin@130.193.48.228]

TASK [../../roles/deploy_python_app : Run docker image] *************************************************************************
changed: [dmitriipolushin@130.193.48.228]

PLAY RECAP **********************************************************************************************************************
dmitriipolushin@130.193.48.228 : ok=15   changed=2    unreachable=0    failed=0    skipped=14   rescued=0    ignored=0

```

The result of `docker ps` on yandex-cloud instance

```
dmitriipolushin@terraform:~$ docker ps
CONTAINER ID   IMAGE                                    COMMAND                  CREATED         STATUS         PORTS                                       NAMES
94c8372163cb   dmitriipolushin/lab2_python_app:latest   "uvicorn main:app --…"   3 minutes ago   Up 3 minutes   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   blissful_beaver
```
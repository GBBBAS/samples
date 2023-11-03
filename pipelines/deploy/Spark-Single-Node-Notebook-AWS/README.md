# Spark Single Node Notebook AWS

This article provides a guide on how to create a conda based self-contained environment to run RTDIP that integrates the following components:
* Java JDK and Apache Spark (Single node configuration). Currently, v3.4.1 Spark (PySpark) has been configured and tested.
* AWS Libraries.
* Jupyter Notebook. 

The components of this environment are all pinned to a specific source distribution of RTDIP.

## Prerequisites

* run_in_docker: Docker desktop or another local Docker environment (e.g. Ubuntu Docker) 
* run_conda_installer.sh: Tested on an x86 Environment.
* For AWS access (e.g. S3) the required permissions available in the environment are required at runtime.

When the installation completes, a Jupyter notebook will be running on port 8080. 
Please check that this port is available or change the configuration in the installer if required.

# Deploy and Running
Run *run_in_docker.sh*. After the installer completes:
* Inside the container a new file *conda_environment_rtdip-sdk.sh* will be created. If required please use this file (e.g. *source ./conda_environment_lfenergy.sh*)  to activate the conda environment within the container.
* On http://localhost:8080/ where host is the machine where the installer was run, a jupyter notebook server will be running. Notebooks can be created to run for example RTDIP pipelines.
* To test the envinroment, create a new notebook and copy the contents of MISO_pipeline_sample.py and run it. 


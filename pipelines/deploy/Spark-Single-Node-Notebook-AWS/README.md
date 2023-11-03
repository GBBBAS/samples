# Spark Single Node Notebook AWS

This article provides a guide on how to create a conda based self-contained environment to run LFEnergy RTDIP that integrates the following components:
* Java JDK and Apache Spark (Single node configuration). Currently, v3.4.1 Spark (PySpark) has been configured and tested.
* AWS Libraries (e.g for accessing files in S3).
* Jupyter Notebook server.

The components of this environment are all pinned to a specific source distribution of RTDIP and have been tested in x86 Windows and Linux environments.

## Prerequisites
* Docker desktop or another local Docker environment (e.g. Ubuntu Docker).
* gitbash environment for Windows environments.

When the installation completes, a Jupyter notebook will be running on port 8080. 
Please check that this port is available or change the configuration in the installer if required.

# Deploy and Running
Run *run_in_docker.sh*. After the installer completes:
* At http://localhost:8080/ a jupyter notebook server will be running. Notebooks can be created to run for example RTDIP pipelines (see below).
* To test the environment, create a new notebook and copy the contents of MISO_pipeline_sample.py and run it. This pipeline queries MISO and saves the results locally under a newly created directory called spark-warehouse.
* For debugging and running from inside the container new RTDIP pipeplines, a new file *conda_environment_rtdip-sdk.sh* is created. Please use this environment to activate 
the LFEnergy RTDIP environment  (e.g. *source ./conda_environment_lfenergy.sh*) within the container.


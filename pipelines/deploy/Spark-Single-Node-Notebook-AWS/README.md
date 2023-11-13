# Spark Single Node Dagster MySql Notebook AWS Integration

This article provides a guide on how to create a conda based self-contained environment to run LFEnergy RTDIP that integrates the following components:
* Java JDK and Apache Spark (Single node configuration). Currently, v3.4.1 Spark (PySpark) has been configured and tested.
* AWS Libraries (e.g for accessing files in AWS S3 if required).
* Jupyter Notebook server.
* Dagster (MySQL backend).

The components of this environment are all pinned to a specific source distribution of RTDIP and have been tested in x86 Windows (using gitbash) and Linux environments.

## Prerequisites
* Docker desktop or another local Docker environment (e.g. Ubuntu Docker).
* gitbash environment for Windows environments.

When the installation completes, a Jupyter notebook will be running locally on port 8080 and Dagster Webserver will be running on port 3000 
Please check that this port is available or change the configuration in the installer if required.

# Deployment
Run *run_in_docker.sh*. After the installer completes:
* At http://localhost:8080/ a jupyter notebook server will be running. Notebooks can be created to run for example new RTDIP pipelines. Sample MISO_pipeline_sample.py provided. This pipeline can be run in a Notebook.
* At http://localhost:3000/ Dagster Server with the sample MISO_pipeline_sample_dagster.py configured as a Dagster asset.
* To test the Notebook environment, create a new notebook and copy the contents of MISO_pipeline_sample.py into it and run it. This pipeline queries MISO (Midcontinent Independent System Operator) and saves the results of the query locally under a newly created directory called spark-warehouse.
* To test the Dagster environment, materialize the asset.
* For debugging purposes and running from inside the container, a file called *conda_environment_lfenergy.sh* is created under /home/rtdip/apps/lfenergy. Please use this file to activate the conda environment (e.g. *source ./conda_environment_lfenergy.sh; conda activate lfenergy*) within the container.


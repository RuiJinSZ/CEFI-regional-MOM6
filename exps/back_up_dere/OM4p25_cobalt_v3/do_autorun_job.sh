#!/bin/bash

count=$1
year=$((count+1958))
data_DIR="/glade/derecho/scratch/rui/MOM6_base_output/"${year}
job_DIR="/glade/derecho/scratch/rui/CEFI-regional-MOM6/exps/OM4p25_cobalt_v3"


# prepare inputs
python generate_input_txt.py ${count}
if ((${year} >= 1959)); then
    mv ./RESTART/*.res* ./INPUT
fi


# do the job
mpiexec /glade/derecho/scratch/rui/CEFI-regional-MOM6/builds/build/linux-intel-intelmpi/ocean_ice/prod/MOM6SIS2 > mom6sis2.log 2> mom6sis2.err


# collect output
mkdir ${data_DIR}
mkdir ${data_DIR}/job-dir
mkdir ${data_DIR}/outputs

mv ${year}*.nc ${data_DIR}/outputs
cp -r ${job_DIR} ${data_DIR}/job-dir


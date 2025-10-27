#!/bin/bash

#SBATCH --nodes=25
#SBATCH --time=60
#SBATCH --job-name="OM4p25_cobalt"
#SBATCH --output=OM4p25_cobalt_o.%j
#SBATCH --error=OM4p25_cobalt_e.%j
#SBATCH --qos=normal
#SBATCH --partition=batch
#SBATCH --clusters=c6
#SBATCH --account=ira-cefi


# Avoid job errors because of filesystem synchronization delays
sync && sleep 1

srun --ntasks=4671 --cpus-per-task=1 --export=ALL MOM6SIS2

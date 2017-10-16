#!/bin/bash
START_ANGLE=$1;
STOP_ANGLE=$2;
N_ANGLES=$3;
N_LEVELS=$5;
N_NODES=$4;

MESHNAME=r${N_LEVELS}a${START_ANGLE}n${N_NODES};
cd /home/fenics/local/ACC-1/murtazo/cloudnaca/;
./runme.sh $START_ANGLE $STOP_ANGLE $N_ANGLES $N_NODES $N_LEVELS;
cd /home/fenics/local/ACC-1/murtazo/cloudnaca/msh/;
dolfin-convert ${MESHNAME}.msh ${MESHNAME}.xml;
cd /home/fenics/local/ACC-1/murtazo/navier_stokes_solver/
./airfoil 10 0.0001 10. 0.1 ../cloudnaca/msh/${MESHNAME}.xml

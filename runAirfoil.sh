#!/bin/bash
ANGLE = $1;
N_LEVELS = $2;
N_NODES = $3;
MESHNAME = r${N_LEVELS}a${ANGLE}n${N_NODES};
cd /home/fenics/local/ACC-1/;
./murtazo/cloudnaca/runme.sh $ANGLE $ANGLE $N_LEVELS $N_NODES;
dolfin-convert ${MESHNAME}.msh ${MESHNAME}.xml;
./airfoil 10 0.0001 10. 0.001 ./murtazo/cloudnaca/msh/${MESHNAME}.xml

#!/bin/bash
mesh
Xmin=`cat xmin3D.txt`
Xmax=`cat xmax3D.txt`
Ymin=`cat ymin3D.txt`
Ymax=`cat ymax3D.txt`
Zmin=`cat zmin3D.txt`
Zmax=`cat zmax3D.txt`
sc=`cat sc.txt`
az=`cat AZ.txt`
el=`cat EL.txt`
gmt4 psxyz topomesh.txt -So -Jx${sc} -Jz${sc} -R${Xmin}/${Xmax}/${Ymin}/${Ymax}/${Zmin}/${Zmax} -Ba500/a500/a500sNeWZ -E${az}/${el} -Wblack -Ccp.cpt -P -K > topo.ps
#gmt4 psxyz test.txt -So -Jx0.004 -Jz0.004 -R-1500/1500/-1500/1500/500/1700 -Ba500/a500/a500sNeWZ -E330/40 -Wblack -Ccp.cpt -P  > topo.ps
#gmt4 psscale cp.cpt -D14/12/5/1 -B
#!/bin/sh
filename="point"
Xmin=`cat xmin2D.txt`
Xmax=`cat xmax2D.txt`
Ymin=`cat ymin2D.txt`
Ymax=`cat ymax2D.txt`
gfig
gmt4 psxy gfig.txt -JX15 -R${Xmin}/${Xmax}/${Ymin}/${Ymax} -Ba500 -K -m -P > ${filename}.ps
gmt4 psxy obscc.txt -J -R -Sc0.1 -Gred -B -K -O -P >> ${filename}.ps

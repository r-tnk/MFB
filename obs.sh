#!bin/sh

#auto file builder for ModEM 
#Written by R.Tanaka@HU 2018.4.19

#原点および観測点の決定，観測点の原点移動
p2p
cp blh2xyz_obs.in blh2xyz.in 
blh2xyz #needs obs.txt
head -n 1 obs.out > origin.txt
obscentre
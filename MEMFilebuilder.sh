#!bin/sh

#auto file builder for ModEM 
#Written by R.Tanaka@HU 2018.4.19
#Version up by R.Tanaka@HU 2019.1.23 with seafloor

#陸上DEMおよび海底DEMの準備
echo "DEM loading"
cp blh2xyz_land.in blh2xyz.in
blh2xyz #needs out.xyz
mv out.out dem.out
echo "SEA DEM loading"
seastart #needs sea.txt"
cp blh2xyz_sea.in blh2xyz.in
blh2xyz

#原点および観測点の決定，観測点の原点移動
echo "Observation point setting"
cp blh2xyz_obs.in blh2xyz.in 
blh2xyz #needs obs.txt
head -n 1 obs.out > origin.txt
obscentre

#各グリッドの中心座標の決定
echo "Grid setting"
calx #needs xset.txt
caly #needs yset.txt
calxy 

#地形ファイルの作成準備
echo "Block setting"
dem #needs dem.out
seadem #needs seaout.out
demcor #needs dzset.txt
h
seah
dcor

#観測点深さの計算
obs
echo "Success!!"


program main
implicit none

real(8) x,y,z,mx,my,zmax,zcor,xmax,ymax,xmin,ymin,zlim
real(8) dz(1000),xp(10000),yp(10000)
integer h,hn(1000),hmax,i,j,n,h0

open(21,file="dz.txt")
open(22,file="demcor.txt")
open(23,file="seademcor.txt")

open(11,file="dem.txt")
open(12,file="xy.txt")
open(13,file="dzset.txt")
open(14,file="seadem.txt")
n=1

do
read(12,*,end=10)i,j,xp(n),yp(n)
n=n+1
end do

10 zmax=0.0

xmax=maxval(xp)
ymax=maxval(yp)
xmin=minval(xp)
ymin=minval(yp)

do
   read(11,*,end=100)x,y,z
   if(x.ge.xmin.and.y.ge.ymin)then
      if(x.le.xmax.and.y.le.ymax.and.z.gt.zmax)then
         zmax=z
         mx=x
         my=y
      end if
   end if
end do

100 h=1
z=0.0d0

read(13,*)zlim

do
   read(13,*,end=105)dz(h),hn(h)
   z=z+dz(h)*dble(hn(h))
   h=h+1
end do

105 h0=h-1

do
   dz(h)=dz(h0)*exp(dble(h-h0))
   hn(h)=1
   z=z+dz(h)*dble(hn(h))
   if(z.gt.zlim)then
      go to 110
   end if
   h=h+1
end do

110 hmax=h
do h=hmax,1,-1
   write(21,*)hn(h),dz(h)
end do

zcor=z-zmax

rewind(11)

do
   read(11,*,end=200)x,y,z
   z=zcor+z
   write(22,*)x,y,z
end do

200 do
   read(14,*,end=300)x,y,z
   z=zcor+z
   write(23,*)x,y,z
end do

300 end program main

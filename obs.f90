program main
implicit none

real(8)xo,yo,zo,x,y,r,rmin,xmin,ymin
real(8),allocatable::dz(:),zz(:)
integer,allocatable::h(:,:),nz(:),ntoz(:)
integer imax,jmax,kmax,i,j,mini,minj,dh,k

open(11,file="obscc.txt")
open(12,file="xy.txt")
open(13,file="topo.txt")
open(14,file="gridset.txt")
open(15,file="dz.txt")

open(21,file="obsh.txt")
open(22,file="obscor.txt")
read(14,*)imax,jmax,kmax
allocate(h(imax,jmax))


do i=1,imax
read(13,*)(h(i,j),j=1,jmax)
end do

i=0

do
read(15,*,end=10)k
i=i+1
end do

10 allocate(nz(i),dz(i),ntoz(i),zz(i))

imax=i

rewind(15)

do i=1,imax
   read(15,*)nz(i),dz(i)
end do

ntoz(imax)=nz(imax)
zz(imax)=dble(nz(imax))*dz(imax)

do i=imax-1,1,-1
   ntoz(i)=ntoz(i+1)+nz(i)
   zz(i)=zz(i+1)+dble(nz(i))*dz(i)
end do


do
rmin=1.0d3
mini=1
minj=1

read(11,*,end=200)xo,yo,zo
do
   read(12,*,end=20)i,j,x,y
   r=sqrt((xo-x)*(xo-x)+(yo-y)*(yo-y))
   if(r.lt.rmin)then
      rmin=r
      xmin=x
      ymin=y
      mini=i
      minj=j
   end if
end do

20 dh=kmax-h(mini,minj)
if(dh.le.ntoz(imax))then
   zo=dble(dh)*dz(imax)
else
   do i=imax-1,1,-1
      if(dh.le.ntoz(i))then
         zo=dble(dh-ntoz(i+1))*dz(i)+zz(i+1)
         go to 100
      end if
   end do
end if

100 write(21,*)xo,yo,zo
write(22,*)xmin,ymin,zo
rewind(12)
end do

200 end program main

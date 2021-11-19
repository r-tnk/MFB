program main
implicit none

real(8)x(100,100),y(100,100),z(100,100),dx(100),dy(100),ddx,ddy,dz(100),ddz,zz(100),x0,y0,sc
integer i,j,k,in,jn,kn,m,n,kl
integer,allocatable::h(:,:),seah(:,:) 

open(11,file="x.txt")
open(12,file="y.txt")
open(13,file="xy.txt")
open(14,file="dz.txt")
open(15,file="topoall.txt")
open(16,file="gridset.txt")
open(17,file="seatopo.txt")
open(18,file="sc.txt")

open(21,file="topomesh.txt")
open(22,file="Zmin3D.txt")
open(23,file="Zmax3D.txt")

read(18,*)sc

read(16,*)in,jn,kn
allocate(h(in,jn),seah(in,jn))
do i=1,in
   read(15,*)(h(i,j),j=1,jn)
   read(17,*)(seah(i,j),j=1,jn)
end do

kl=maxval(seah)+1

read(11,*)x0
read(12,*)y0


i=1
do
   read(11,*,end=10)m,ddx
   dx(i:i+m-1)=ddx
   i=i+m
end do

10 i=1
do
   read(12,*,end=20)m,ddy
   dy(i:i+m-1)=ddy
   i=i+m
end do

20 m=1

do 
   read(13,*,end=30)i,j,x(i,j),y(i,j)
end do

30 m=1

i=1

do
   read(14,*,end=40)m,ddz
   dz(i:i+m-1)=ddz
   i=i+m
end do

40 zz(1)=dz(1)

do k=2,kn
   zz(k)=zz(k-1)+dz(k)
end do

do i=1,in
   do j=1,jn
      write(21,*)x(i,j),y(i,j),zz(h(i,j))-zz(kl),zz(h(i,j))-zz(kl),dx(j)*sc,dy(i)*sc
   end do
end do

write(22,'(f0.2)')zz(kl)-zz(kl)
write(23,'(f0.2)')zz(maxval(h))-zz(kl)

end program main
      

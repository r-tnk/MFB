program main
implicit none
real(8),allocatable::dem(:,:),dz(:),z(:)
real(8) x,y,a,zz,dm
integer i,j,m,n,l,k,imax,jmax
integer,allocatable::h(:,:),kn(:),kto(:)
character fmt*8

!write(*,*)"Enter mesh size of dem"
!read(*,*)dm
dm=1.3d1
dm=dm/2.0d0

open(11,file="dz.txt")
open(12,file="demcor.txt")
open(13,file="xy.txt")

open(21,file="topo.txt")
open(22,file="gridset.txt")

m=0
do
read(12,*,end=10)a
m=m+1
end do

10 allocate(dem(m,3))
rewind(12)

do n=1,m
read(12,*)dem(n,1),dem(n,2),dem(n,3)
end do

l=0
do
read(11,*,end=20)a
l=l+1
end do

20 allocate(dz(l),z(l),kn(l),kto(l))

rewind(11)

z(0)=0.0d0
kto(0)=0

do n=1,l
   read(11,*)kn(n),dz(n)
   z(n)=z(n-1)+dz(n)*dble(kn(n))
   kto(n)=kto(n-1)+kn(n)
end do


do
read(13,*,end=50)i,j
end do

50 imax=i
jmax=j
allocate(h(imax,jmax))
rewind(13)
do
   read(13,*,end=200)i,j,x,y
   do n=1,m
      if(abs(dem(n,1)-x).le.dm.and.abs(dem(n,2)-y).le.dm)then
!         write(*,*)dem(n,1),dem(n,2)
!         write(*,*)x,y,dem(n,1),dem(n,2),dem(n,3)
         do k=1,l
            if(z(k).gt.dem(n,3))then
               zz=z(k-1)
               h(i,j)=kto(k-1)
               do
                zz=zz+dz(k)
                h(i,j)=h(i,j)+1
                if(zz.gt.dem(n,3))then
                   h(i,j)=h(i,j)-1
!                   write(*,*)x,y,dem(n,1),dem(n,2),zz,dem(n,3),h(i,j)
                   go to 100
                end if
             end do
          end if
       end do
    end if
 end do
100 end do

200 do i=1,imax
! do j=1,jmax
 write(21,'(99I3)')(h(i,j),j=1,jmax)
!    if(h(i,j).eq.0)write(*,*)i,j
 !end do
end do

write(22,*)imax,jmax,maxval(h)

end program main

program main
implicit none
integer i,j,k,in,jn,kn,n,nn,nnn,ii,jj
integer,allocatable::h(:,:),m(:,:),landh(:,:),seah(:,:)
real(8),allocatable:: s(:)
real(8)ss
character FMT*6

open(11,file="gridset.txt")
open(12,file="topo.txt")
open(13,file="seatopo.txt")
open(14,file="spara.txt")

open(21,file="topo.cov")
open(22,file="topoall.txt")
read(11,*)in,jn,kn
allocate(h(in,jn),m(in,jn),landh(in,jn),seah(in,jn))

FMT='(NNI3)'
write(FMT(2:3),'(I2)')jn

write(21,*)"+-----------------------------------------------------------------------------+"
write(21,*)"| This file defines model covariance for a recursive autoregression scheme.   |"
write(21,*)"| The model space may be divided into distinct areas using integer masks.     |"
write(21,*)"| Mask 0 is reserved for air; mask 9 is reserved for ocean. Smoothing between |"
write(21,*)"| air, ocean and the rest of the model is turned off automatically. You can   |"
write(21,*)"| also define exceptions to override smoothing between any two model areas.   |"
write(21,*)"| To turn off smoothing set it to zero. This header is 16 lines long.         |"
write(21,*)"| 1. Grid dimensions excluding air layers (Nx, Ny, NzEarth)                   |"
write(21,*)"| 2. Smoothing in the X direction (NzEarth real values)                       |"
write(21,*)"| 3. Smoothing in the Y direction (NzEarth real values)                       |"
write(21,*)"| 4. Vertical smoothing (1 real value)                                        |"
write(21,*)"| 5. Number of times the smoothing should be applied (1 integer >= 0)         |"
write(21,*)"| 6. Number of exceptions (1 integer >= 0)                                    |"
write(21,*)"| 7. Exceptions in the form e.g. 2 3 0. (to turn off smoothing between 3 & 4) |"
write(21,*)"| 8. Two integer layer indices and Nx x Ny block of masks, repeated as needed.|"
write(21,*)"+-----------------------------------------------------------------------------+"
write(21,*)""


read(14,*)ss

do i=1,in
   read(12,*)(landh(i,j),j=1,jn)
   read(13,*)(seah(i,j),j=1,jn)
end do

do i=1,in
   do j=1,jn
      if(seah(i,j).gt.landh(i,j))then
         h(i,j)=seah(i,j)
      else
         h(i,j)=landh(i,j)
      end if
   end do
end do

do i=1,in
   do j=1,jn
      if(h(i,j).eq.0)then
         do n=2,in
            do nn=1,n
               ii=nn-1
               do nnn=1,nn
                  jj=nnn-1
                  if(i.lt.in/2.and.j.lt.jn/2.and.h(i+ii,j+jj).gt.0)then
                     h(i,j)=h(i+ii,j+jj)
                     go to 20
                  else if(i.ge.in/2-1.and.j.lt.jn/2.and.h(i-ii,j+jj).gt.0)then
                     h(i,j)=h(i-ii,j+jj)
                     go to 20
                  else if(i.lt.in/2.and.j.ge.jn/2-1.and.h(i+ii,j-jj).gt.0)then
                     h(i,j)=h(i+ii,j-jj)
                     go to 20
                  else if(i.ge.in/2-1.and.j.ge.jn/2-1.and.h(i-ii,j-jj).gt.0)then
                     h(i,j)=h(i-ii,j-jj)
                     go to 20
                  end if
               end do
            end do
         end do
20    end if
   end do
end do

do i=1,in
   write(22,'(99I3)')(h(i,j),j=1,jn)
end do

write(21,'(3I4)')in,jn,kn
write(21,*)""

allocate(s(kn))

!do k=1,kn
!   if(k.lt.40)then
!      s(k)=0.4
!   else if(s(k-1).gt.0.2)then
!      s(k)=s(k-1)-1.0d-2
!   else
!      s(k)=0.2
!   end if
!end do

s(:)=ss

do i=1,2
   do k=1,kn
      write(21,fmt='(f5.2)',advance='no')s(k)
   end do
write(21,*)""
write(21,*)""
end do

write(21,'(f5.2)')ss

write(21,*)""
write(21,'(I3)')1
write(21,*)""
write(21,'(I3)')0
write(21,*)""

do k=kn,1,-1
if(minval(h).ge.k)then
   write(21,'(2I3)')kn-k+1,kn
   m(:,:)=1
   do i=1,in
      write(21,FMT)(m(i,j),j=1,jn)
   end do
   go to 100
else
   write(21,'(2I3)')kn-k+1,kn-k+1
   do i=1,in
      do j=1,jn
         if(h(i,j).lt.k.and.k.le.maxval(seah)+1)then
            m(i,j)=9
         else if(h(i,j).lt.k)then
            m(i,j)=0
         else
            m(i,j)=1
         end if
      end do
   end do
   do i=1,in
      write(21,FMT)(m(i,j),j=1,jn)
   end do
   write(21,*)""
end if
end do

100 end program main


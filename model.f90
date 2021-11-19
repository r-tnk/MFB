program main
implicit none
integer in,jn,kn,i,j,k,dh,imax
integer,allocatable::h(:,:),nz(:),ntoz(:),zz(:),landh(:,:),seah(:,:)
real(8) x,y,dx,dy,zo,rhoini
real(8),allocatable::iv(:,:),dz(:)
character FMT*11

open(11,file="gridset.txt")
open(12,file="x.txt")
open(13,file="y.txt")
open(14,file="dz.txt")
open(15,file="seatopo.txt")
open(16,file="topoall.txt")
open(17,file="IRV.txt")

open(21,file="model.ws")

read(17,*)rhoini

read(11,*)in,jn,kn

write(21,*)"#3D MT model"
write(21,'(4I4,a)')in,jn,kn,0," LOGE"

read(13,*)y
do
   read(13,*,end=10)i,dy
   do j=1,i
      write(21,'(f10.2)',advance='no')dy
   end do
end do

10 write(21,*)""

read(12,*)x

do
   read(12,*,end=20)i,dx
   do j=1,i
      write(21,'(f10.2)',advance='no')dx
   end do
end do

20 write(21,*)""

i=0 

do
   read(14,*,end=30)j
   i=i+1
end do

30 allocate(nz(i),dz(i),ntoz(i),zz(i))
imax=i

rewind(14)

do i=1,imax
   read(14,*)nz(i),dz(i)
end do

do i=imax,1,-1
   do j=1,nz(i)
      write(21,'(f10.2)',advance='no')dz(i)
   end do
end do

ntoz(imax)=nz(imax)
zz(imax)=dble(nz(imax))*dz(i)

do i=imax-1,1,-1
   ntoz(i)=ntoz(i+1)+nz(i)
   zz(i)=zz(i+1)+dble(nz(i))*dz(i)
end do


write(21,*)""
write(21,*)""

allocate(h(in,jn),iv(in,jn),landh(in,jn),seah(in,jn))

FMT='(NNE13.5e2)'
write(FMT(2:3),'(I2)')in

do i=1,in
   read(15,*)(seah(i,j),j=1,jn)
   read(16,*)(h(i,j),j=1,jn)
end do

do k=kn,1,-1
   do i=1,in
      do j=1,jn
         if(h(i,j).lt.k.and.k.le.maxval(seah)+1)then
            iv(i,j)=log(3.0d-1)
         else if(h(i,j).lt.k)then
            iv(i,j)=log(1.0d8)
         else
            iv(i,j)=log(rhoini)
         end if
      end do
   end do
   do j=1,jn
      write(21,FMT)(iv(i,j),i=1,in)
   end do
   write(21,*)""
end do

dh=kn-h(in,1)

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


100 write(21,'(3f12.3)')-y,x,0.0
write(21,'(f6.3)')0.0

end program main

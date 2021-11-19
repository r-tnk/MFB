program main
implicit none
real(8) x,dx(1000),xlim
integer i,in(1000),imax

open(11,file="yset.txt")
open(21,file="y.txt")

i=1
x=0.0

read(11,*)xlim

do
   read(11,*,end=10)dx(i),in(i)
   x=x+dx(i)*dble(in(i))
   i=i+1
end do

10 do
   dx(i)=dx(i-1)*1.4d0
   in(i)=1
   x=x+dx(i)*dble(in(i))
   if(x.gt.xlim)then
      go to 20
   end if
   i=i+1
end do

20 imax=i

write(21,*)x

do i=imax,1,-1
   write(21,*)in(i),dx(i)
end do

do i=1,imax
   write(21,*)in(i),dx(i)
end do
end program main

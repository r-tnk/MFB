program main
implicit none

real(8)x,y,x0,y0,z

open(11,file="dem.out")
open(12,file="origin.txt")
open(21,file="dem.txt")

read(12,*)x,y,z

x0=x
y0=y

rewind(11)

do
read(11,*,end=100)x,y,z
x=x-x0
y=y-y0
write(21,*)x,y,z
end do

100 end program main

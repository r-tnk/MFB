program main
implicit none
integer i
real(8)x,y,z



open(11,file="sea.txt")
open(21,file="seaout.xyz")

write(21,*)"data"

do
   read(11,*,end=100)i,x,y,z
   write(21,*)y,x,-z
end do

100 end program main

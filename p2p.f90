program main
implicit none

real(8)lat,lon,z

open(11,file="obsp.txt")
open(21,file="obs.txt")

z=0.0d0

write(21,*)"data"

do
   read(11,*,end=100)lat,lon
   write(21,*)lon,lat,z
end do

100 end program main

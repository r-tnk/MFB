program main
implicit none
real(8),allocatable::x(:),y(:),z(:)
real(8) xmin,xmax,ymin,ymax,sc
integer i,az,el

open(11,file="obscc.txt")

open(21,file="xmin2D.txt")
open(22,file="xmax2D.txt")
open(23,file="ymin2D.txt")
open(24,file="ymax2D.txt")
open(25,file="xmin3D.txt")
open(26,file="xmax3D.txt")
open(27,file="ymin3D.txt")
open(28,file="ymax3D.txt")
open(29,file="sc.txt")
open(30,file="AZ.txt")
open(31,file="EL.txt")
i=1

do
   read(11,*,end=10)xmin
   i=i+1
end do

10 allocate(x(i),y(i),z(i))

rewind(11)

i=1

do
   read(11,*,end=20)x(i),y(i),z(i)
   i=i+1
end do

20 xmin=minval(x)
xmax=maxval(x)
ymin=minval(y)
ymax=maxval(y)
sc=1.0d1/(xmax-xmin)
az=135
el=60

write(21,100)xmin
write(22,100)xmax
write(23,100)ymin
write(24,100)ymax
write(25,100)xmin
write(26,100)xmax
write(27,100)ymin
write(28,100)ymax
write(29,'(f0.5)')sc
write(30,'(I0)')az
write(31,'(I0)')el

100 format(f0.2)

end program main

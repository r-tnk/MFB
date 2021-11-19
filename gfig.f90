program main
implicit none
real(8)x0,y0,dx(100),dy(100),x1,y1,x2,y2
integer i,imax,jmax,j,m(100),n(100),k

open(11,file="xset.txt")
open(12,file="yset.txt")

open(21,file="gfig.txt")

read(11,*)x0
read(12,*)y0

x0=0
y0=0

i=1

do
   read(11,*,end=20)dx(i),m(i)
   x0=x0+dx(i)*real(m(i))
   i=i+1
end do

20 imax=i-1

j=1

do
   read(12,*,end=30)dy(j),n(j)
   y0=y0+dy(j)*real(n(j))
   j=j+1
end do

30 jmax=j-1

x1=0.0d0
y1=y0
y2=-y0

do i=1,imax
   do k=1,m(i)
      write(21,*)x1,y1
      write(21,*)x1,y2
      write(21,*)">"
      write(21,*)-x1,y1
      write(21,*)-x1,y2
      write(21,*)">"
      x1=x1+dx(i)
   end do
end do

y1=0.
x1=x0
x2=-x0

do j=1,jmax
   do k=1,n(j)
      write(21,*)x1,y1
      write(21,*)x2,y1
      write(21,*)">"
      write(21,*)x1,-y1
      write(21,*)x2,-y1
      write(21,*)">"
      y1=y1+dy(j)
   end do
end do

end program main



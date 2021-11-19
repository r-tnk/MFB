program main
implicit none
real(8),allocatable:: x(:),y(:),dx(:),dy(:),xto(:),yto(:)
real(8)a,x0,y0
integer i,j,m,n,imax,jmax
integer,allocatable::in(:),jn(:),ito(:),jto(:)

open(11,file="x.txt")
open(12,file="y.txt")
open(21,file="xy.txt")

m=2
n=2

read(11,*)a
read(12,*)a
do
read(11,*,end=10)a
m=m+1
end do

10 do
read(12,*,end=20)a
n=n+1
end do

20 allocate(in(m),jn(n),dx(m+1),dy(n+1),ito(m+1),jto(n+1),xto(m+1),yto(n+1))

rewind(11)
rewind(12)
imax=0
jmax=0
ito(1)=0
jto(1)=0
xto(1)=0
yto(1)=0


read(11,*)x0
read(12,*)y0
do i=2,m-1
   read(11,*)in(i),dx(i)
   ito(i)=ito(i-1)+in(i)
   xto(i)=xto(i-1)+dx(i)*dble(in(i))
   imax=imax+in(i)
end do

do i=2,n-1
   read(12,*)jn(i),dy(i)
   jto(i)=jto(i-1)+jn(i)
   yto(i)=yto(i-1)+dy(i)*dble(jn(i))
   jmax=jmax+jn(i)
end do

allocate(x(imax+1),y(jmax+1))
x(1)=x0
y(1)=y0
n=2
m=2
dx(1)=0.0d0
dy(1)=0.0d0
xto(1)=0
yto(1)=0
ito(1)=0
jto(1)=0

do i=2,imax+1
   if(i-1.gt.ito(m-1))then
      x(i)=x(i-1)+dx(m-1)/2.0d0+dx(m)/2.0d0
      m=m+1
   else
      x(i)=x(i-1)+dx(m-1)
   end if
end do

do j=2,jmax+1
   if(j-1.gt.jto(n-1))then
      y(j)=y(j-1)-dy(n-1)/2.0d0-dy(n)/2.0d0
      n=n+1
   else
      y(j)=y(j-1)-dy(n-1)
   end if
end do

do i=2,imax+1
   do j=2,jmax+1
      write(21,*)j-1,i-1,x(i),y(j)
   end do
end do

end program main

program main
implicit none

integer kmax,znum(1000),zs,imax,jmax,n,nmax
real(8) dz(1000)


open(11,file="gridset.txt")
open(12,file="dz.txt")

read(11,*)imax,jmax,kmax

zs=0
n=1

do
   read(12,*,end=10)znum(n),dz(n)
   zs=zs+znum(n)
   n=n+1
end do

10 close(12)

nmax=n-1

znum(nmax)=znum(nmax)-(zs-kmax)

open(21,file="dz.txt")

do n=1,nmax
   write(21,*)znum(n),dz(n)
end do

end program main
   




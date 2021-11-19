program main
implicit none

integer i,j,m,n,k,ii,jj

i=1
j=1

!do k=2,10
!   do m=1,k
!      ii=i-2+m
!      do n=1,m
!         jj=j-2+n
!         write(*,*)ii,jj
!      end do
!   end do
!end do


do k=2,10
   do m=1,k
      ii=i-2+m
      do n=1,m
         jj=j-2+n
         write(*,*)-ii,jj
      end do
   end do
end do

end program main

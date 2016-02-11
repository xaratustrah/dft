!
! double precision dft subroutine
! xaratustrah
! 2016
!

subroutine dft(n, x, y)
  implicit none
  integer, parameter :: dp = kind(1.0d0)
  real(dp), parameter :: pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628
  integer, intent (in) :: n
  complex(dp), intent (in), dimension(n) :: x
  complex(dp), intent (out), dimension(n) :: y
  real(dp), dimension (n) :: xre, xim, yre, yim
  real(dp) :: sumreal, sumimag, angle
  integer :: k, t

  xre = real(x)
  xim = aimag (x)

  do k = 1, n
     sumreal = 0.0_dp
     sumimag = 0.0_dp
     do t = 1, n
        angle = 2.0_dp * pi * t * k / n
        sumreal = sumreal + xre(t) * cos(angle) + xim(t) * sin(angle)
        sumimag = sumimag - xre(t) * sin(angle) + xim(t) * cos(angle)
     enddo
     yre(k) = sumreal
     yim(k) = sumimag
  enddo

  y = dcmplx(yre, yim)
end subroutine dft

! -------------------------------------

program test_dft
  implicit none
  integer, parameter :: dp = kind(1.0d0)
  complex(dp), dimension (4) :: x, y

  x = [(1,2), (2,3) ,(3,4), (4, 5)]
  call dft(size(x), x, y)
  print *, x
  print *, y
end program test_dft



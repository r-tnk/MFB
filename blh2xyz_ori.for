      PARAMETER (M=100000000)
      IMPLICIT REAL*8(A-H,O-Z)
      DIMENSION HIGH(M),HOK(M),TOK(M)
      COMMON /CST1/E,ED,A,F,PI,IND
      COMMON /CST2/FA1,FA2,FA3,R1,R2,R3,r1a
      COMMON /CST3/DR,CS,TA,RN,ET
      CHARACTER FILE1*14,FILE2*14,KIND*1,dum*20
c
c     kind J, W  ë»â~ëÃ
c     fa1        datum lat  
c     r1         datum lon
c     ind        decimal deg or ddmmss
c
c
C     ---------------------------------- file open
      OPEN(1,FILE='blh2xyz.in',STATUS='OLD')
C
      READ(1,'(A)') FILE1
      READ(1,*) KIND,IND
      READ(1,*) fa1a, r1a
      CLOSE(1)
C     ---------------------------------- output file name
      L=1
    1 IF(FILE1(L:L).EQ.'.') GOTO 2
      L=L+1
      GOTO 1
    2 L=L-1
      FILE2=FILE1(1:L)//'.out'
C     ---------------------------------- file open
      OPEN(1,FILE=FILE1)
      OPEN(2,FILE=FILE2)
C     ---------------------------------- input data
c      write(*,*) file1
c
      READ(1,*) dum
c      write(*,*) dum
      K=1
c
c     
       
    5 rEAD(1,*,END=99) TOK(K), HOK(K), HIGH(k)
      K=K+1
      GOTO 5
   99 N=K-1
c
c      write(*,*) ( HOK(K), TOK(K), HIGH(K), K=1,2)
c   

c      FA1=33.0
      Fa1=fa1a
      FA2=0.
      FA3=0.
c
c
c      R1=131.
      r1=r1a
      r2=0.
      r3=0.
c      
C     ---------------------------------- coord. source
      CALL CONST(KIND)
      CALL SHIGO(S0)
c      
c        write(*,*) s0    
C     ================================== coordinate repeate
      DO 100 I=1,N
c      IF (mod (I,1000) .eq. 0)  write(*,*) I
      IF (HIGH(I) .LT. -9000) goto 100
      IF(IND.NE.1) GOTO 10
      FA1=REAL(INT(HOK(I)/10000.))
      FA2=REAL(INT((HOK(I)-FA1*10000.)/100.))
      FA3=( HOK(I)-FA1*10000.-FA2*100.)
      R1 =REAL(INT(TOK(I)/10000.))
      R2 =REAL(INT((TOK(I)- R1*10000.)/100.))
      R3 =( TOK(I)- R1*10000.- R2*100.)
      GOTO 20
   10 FA1=HOK(I)
      R1 =TOK(I)
c
c      write(*,*) s0
c      
c       write(*,*) HOk(1), TOK(1)     
C     ---------------------------------- culc.
   20 CALL SHIGO(S)
c   
c      write(*,*) s
c 
      CALL COMPA
      CALL ZAHYO(S,S0,X,Y)
      WRITE(2,*) Y, ',' , X , ',',HIGH(I)
c      WRITE(2,'(2(A,F10.2),A, F10.2)') I,',', Y, ',' , X , ',' ,
c     1                                  HIGH(I)
  100 CONTINUE
      CLOSE(2)
C
      STOP
      END
C     //////////////////////////////////
      SUBROUTINE CONST(KIND)
      IMPLICIT REAL*8(A-H,O-Z)
      COMMON /CST1/E,ED,A,F,PI,IND
      CHARACTER KIND*1
C     ---------------------------------- World/Japan
      IF(KIND.EQ.'J'.OR.KIND.EQ.'j') THEN
      A =6.377397155D6
      F =2.99152813D2
      ELSE
      A =6.378137D6
      F =2.98257222101D2
      ENDIF
      PI=3.1415926D0
C     ---------------------------------- ë»â~ëÃåˆéÆ
      E =SQRT(2.*F-1.)/F
      ED=SQRT(2.*F-1.)/(F-1.)
C
      RETURN
      END
C     //////////////////////////////////
      SUBROUTINE SHIGO (S)
      IMPLICIT REAL*8(A-H,O-Z)
      COMMON /CST1/E,ED,A,F,PI,IND
      COMMON /CST2/FA1,FA2,FA3,R1,R2,R3,r1a
C
      AA=1.+3.*E**2/4.+45.*E**4/64.+175.*E**6/256.+11025.*E**8/16384.
     *  +43659.*E**10/65536.+693693.*E**12/1048576.
     *  +19324305.*E**14/29360128.+4927697775.*E**16/7516192768.
      BB=3.*E**2/4.+15.*E**4/16.+525.*E**6/512.+2205.*E**8/2048.
     *  +72765.*E**10/65536.+297297.*E**12/262144.
     *  +135270135.*E**14/117440512.+547521975.*E**16/469762048.
      CC=15.*E**4/64.+105.*E**6/256.+2205.*E**8/4096.
     *  +10395.*E**10/16384.+1486485.*E**12/2097152.
     *  +45090045.*E**14/58720256.+766530765.*E**16/939524096.
      DD=35.*E**6/512.+315.*E**8/2048.+31185.*E**10/131072.
     *  +165165.*E**12/524288.+45090045.*E**14/117440512.
     *  +209053845.*E**16/469762048.
      EE=315.*E**8/16384.+3465.*E**10/65536.+99099.*E**12/1048576.
     *  +4099095.*E**14/29360128.+348423075.*E**16/1879048192.
      FF=693.*E**10/131072.+9009.*E**12/524288.
     *  +4099095.*E**14/117440512.+26801775.*E**16/469762048.
      GG=3003.*E**12/2097152.+315315.*E**14/58720256.
     *  +11486475.*E**16/939524096.
      HH=45045.*E**14/117440512.+765765.*E**16/469762048.
      RI=765765.*E**16/7516192768.
C
      B1=A*(1.-E**2)*AA
      B2=A*(1.-E**2)*(-BB/2.)
      B3=A*(1.-E**2)*(CC/4.)
      B4=A*(1.-E**2)*(-DD/6.)
      B5=A*(1.-E**2)*(EE/8.)
      B6=A*(1.-E**2)*(-FF/10.)
      B7=A*(1.-E**2)*(GG/12.)
      B8=A*(1.-E**2)*(-HH/14.)
      B9=A*(1.-E**2)*(RI/16.)
C
      RAD=180./PI
      IF(IND.EQ.1) FAI=(FA1*3600.+FA2*60.+FA3)/(3600.*RAD)
      IF(IND.EQ.2) FAI=FA1/RAD
C     ---------------------------------- culc. sin,cos,tan
      S02=SIN(FAI* 2.)
      S04=SIN(FAI* 4.)
      S06=SIN(FAI* 6.)
      S08=SIN(FAI* 8.)
      S10=SIN(FAI*10.)
      S12=SIN(FAI*12.)
      S14=SIN(FAI*14.)
      S16=SIN(FAI*16.)
      S=B1*FAI+B2*S02+B3*S04+B4*S06+B5*S08+B6*S10+B7*S12+B8*S14+B9*S16
C
      RETURN
      END
C     //////////////////////////////////
      SUBROUTINE COMPA
      IMPLICIT REAL*8(A-H,O-Z)
      COMMON /CST1/E,ED,A,F,PI,IND
      COMMON /CST2/FA1,FA2,FA3,R1,R2,R3,r1a
      COMMON /CST3/DR,CS,TA,RN,ET
C
      RAD=180./PI
      IF(IND.EQ.1) DR=((R1*3600.+ R2*60.+ R3)/3600.-r1a)/RAD
      IF(IND.EQ.2) DR=(R1-r1a)/RAD
c      
c      write(*,*) 'dr',  dr, r1, r1a      
C     ---------------------------------- cos É’
      IF(IND.EQ.1) FAI=(FA1*3600.+FA2*60.+FA3)/(3600.*RAD)
      IF(IND.EQ.2) FAI=FA1/RAD
      CS=COS(FAI)
      TA=TAN(FAI)
C     ---------------------------------- èké⁄åWêî
      V=SQRT(1.+(ED*CS)**2)
      C=A*F/(F-1.)
      RN=C/V
      ET=ED*CS
C
      RETURN
      END
C     //////////////////////////////////
      SUBROUTINE ZAHYO(S,S0,X,Y)
      IMPLICIT REAL*8(A-H,O-Z)
      COMMON /CST3/DR,CS,TA,RN,ET
      DATA RM0/0.9999/
C
      E2=ET**2
      T2=TA**2
      T4=TA**4
      T6=TA**6
C     ---------------------------------- coordinate x,y
      X=((S-S0)+RN*CS**2*TA*DR**2/2.
     * +RN*CS**4*TA*(5.-T2+9.*E2+4.*E2**2)*DR**4/24.
     * -RN*CS**6*TA*(-61.+58.*T2-T4-270.*E2+330.*T2*E2)*DR**6/720.
     * -RN*CS**8*TA*(-1385.+3111.*T2-543.*T4+T6)*DR**8/40320.)*RM0
C
      Y=(RN*CS*DR-RN*CS**3*(-1.+T2-E2)*DR**3/6.
     * -RN*CS**5*(-5.+18.*T2-T4-14.*E2+58.*T2*E2)*DR**5/120.
     * -RN*CS**7*(-61.+479.*T2-179.*T4+T6)*DR**7/5040.)*RM0
C
      RETURN
      END

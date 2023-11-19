O=0
Q=O
W=O
E=O
R=O
T=O
Y=O
U=O
I=O
b=O
P=O
k=O
l=O
A=O
S=O
D=O
F=O
p="O"
X="x"
print "AMIRAL BATTI Oyununa hosgeldiniz"
while True:

    
    print"| 1 || 2 || 3 || 4 |"
    print"|",Q,"||",W,"||",E,"||",R, "| A"
    print"|",T,"||",Y,"||",U, "||",I,"| B"
    print"|",b,"||",P,"||",k,"||",l, "| C"
    print"|",A,"||",S,"||",D,"||",F, "| D"

    S1=raw_input("Hangi kareye ROKET atalim? :")
    if S1=="A1" or S1=="a1":
        Q=X
        print "vurdunuz!!"
        if Q==T and T==X:
            T=8
            Q=8
            print "ve BATTI!"
    if S1=="B1" or S1=="b1":
        T=X
        print "vurdunuz!!"
        if T==Q and Q==X:
            T=8
            Q=8
            print "ve BATTI!"
#2. gemi
    if S1=="D2" or S1=="d2":
        S=X
        print "vurdunuz!!"
        if S==D and D==X:
            S=8
            D=8
            print "ve BATTI!"
    if S1=="D3" or S1=="d3":
        D=X
        print "vurdunuz!!"
        if D==S and S==X:
            D=8
            S=8
            print "ve BATTI!"
#3.gemi
    if S1=="B4" or S1=="b4":
        I=X
        print "vurdunuz!!"
        if I==R and R==X:
            R=8
            I=8
            print "ve BATTI!"
    if S1=="A4" or S1=="a4":
        R=X
        print "vurdunuz!!"
        if R==I and I==X:
            R=8
            I=8
            print "ve BATTI!"
    
#hepsi batti
    if R==D and T==I :
        if S==Q and R==8 :
            print "Tebrikler. Butun Gemiler BATTI"
            break
    if S1!="a1" and S1!="A1" and S1!="b1" and S1!="B1" and S1!="d2" and S1!="D2" and S1!="D3" and S1!="d3" and S1!="B4" and S1!="b4" and S1!="A4" and S1!="a4":
        print "Karavana"

def main():
    
    li = list(map(int,input().split()))
    A=li[0]
    B=li[1]
    MN=0
    if B>A: MN=A
    else: MN=B
    for i in range(1,MN+1):
        if A%i==0 and B%i==0:
            HCF=i
    print(HCF)
    return 0

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        main()
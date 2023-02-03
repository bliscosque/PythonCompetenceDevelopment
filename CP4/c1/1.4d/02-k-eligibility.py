tc=int(input())
for _ in range(tc):
    name,sStudy,bithDate,courses=input().split()
    sStudyYear=int(sStudy.split('/')[0])
    bithYear=int(bithDate.split('/')[0])
    courses=int(courses)
    eligible=False
    petition=False
    if sStudyYear>=2010 or bithYear>=1991:
        eligible=True
    if not eligible:
        if courses<41:
            petition=True
    if eligible:
        print(f'{name} eligible')
    elif petition:
        print(f'{name} coach petitions')
    else: 
        print(f'{name} ineligible')
            

N1, N2, N3, N4 = map(float, input().split())

avarage = ((N1*2) + (N2*3) + (N3*4) + (N4*1)) / 10
print(f'Media: {avarage:.1f}')

if avarage >= 7.0:
    print('Aluno aprovado.')

elif  5.0 <= avarage <= 6.9:
    print('Aluno em exame.')

    examGrade = float(input())
    print(f'Nota do exame: {examGrade:.1f}')

    finalAvarage = (avarage + examGrade) / 2

    if finalAvarage < 4.9:
        print('Aluno reprovado.')

    else:
        print('Aluno aprovado.')
    
    print(f'Media final: {finalAvarage:.1f}')

else:
    print('Aluno reprovado.')
def nb_year(p0, percent, aug, p):
    years=0
    while p0<p:
        years+=1
        p0+=int(p0*(percent*0.01)+aug)
    return years

print(nb_year(1500,5,100,5000))

        
ceki=float((input("cekinizi kiloqram ile daxil edin:" )))
boy=float((input("boyunuzu metr ile daxil edin:" )))
BMI=ceki/(boy**2)
if BMI<18.5:
    print("ariqsiz")
elif 18.5<=BMI<25:
    print("normal cekili")
elif 25<=BMI<30:
    print("artiq ceki")
else:
    print("piylenme")
    
    

    

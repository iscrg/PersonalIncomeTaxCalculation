import ru_local

total_tax = 0

def Ivan():
    ans = input(ru_local.RESIDENT).lower()
    if ans == ru_local.Y:
        #IVAN

        #Insure benefits
        ans = float(input(ru_local.R_INSURE_BENEFITS))
        total_tax += ans * 0.13

        #Gift
        ans = input(ru_local.R_GIFT).lower()
        if ans == ru_local.Y:
            ans = float(ru_local.CADASTRAL_VALUE)
            total_tax += ans * 0.13
        else:
            pass

        #Cars
        ans = input(ru_local.CAR).lower()
        if ans == ru_local.Y:
            total_tax += ans * 0.13
        else:
            pass

        #CLC
        ans = float(input(ru_local.R_CLC))
        if ans > 5_000_000:
            total_tax += 5_000_000 * 0.13 + (ans - 5_000_000) * 0.15
        else:
            total_tax += ans * 0.13

        #Salary
        ans = float(input(ru_local.SALARY))
        if ans > 5_000_000:
            total_tax += 5_000_000 * 0.13 + (ans - 5_000_000) * 0.15
        else:
            total_tax += ans * 0.13 

def Dmitry():
    pass

def Daniil():
    pass
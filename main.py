import ru_local

def main():
    total_tax = 0

    ans = input(ru_local.RESIDENT).lower()
    if ans == ru_local.Y:

        # Insure benefits
        ans = float(input(ru_local.R_INSURE_BENEFITS))
        total_tax += ans * 0.13

        # Gift
        ans = input(ru_local.R_GIFT).lower()
        if ans == ru_local.Y:
            ans = float(input(ru_local.CADASTRAL_VALUE))
            total_tax += ans * 0.13
        else:
            pass

        # Cars
        ans = input(ru_local.CAR).lower()
        if ans == ru_local.Y:
            ans = float(input(ru_local.AMOUNT))
            total_tax += ans * 0.13
        else:
            pass

        # CLC
        ans = float(input(ru_local.R_CLC))
        if ans > 5_000_000:
            total_tax += 5_000_000 * 0.13 + (ans - 5_000_000) * 0.15
        else:
            total_tax += ans * 0.13

        # Salary
        ans = float(input(ru_local.SALARY))
        if ans > 5_000_000:
            total_tax += 5_000_000 * 0.13 + (ans - 5_000_000) * 0.15
        else:
            total_tax += ans * 0.13 

        # Obligation percents
        ans = input(ru_local.R_OBL_PERCENT).lower()
        if ans == ru_local.Y:
            ans = input(ru_local.R_OBL_2007).lower()
            if ans == ru_local.Y:
                ans = float(input(ru_local.AMOUNT))
                total_tax += ans * 0.09
            else:
                ans = float(input(ru_local.AMOUNT))
                total_tax += ans * 0.13
        else:
            pass
        
        # Securities
        ans = input(ru_local.R_SECURITIES).lower()
        if ans == ru_local.Y:
            ans = float(input(ru_local.AMOUNT))
            total_tax += ans * 0.3
        else:
            pass

        # Realty
        ans = input(ru_local.R_REALTY).lower()
        if ans == ru_local.Y:
            ans = float(input(ru_local.AMOUNT))
            total_tax += ans * 0.13
        else:
            pass

        # Prize summary
        ans_float = float(input(ru_local.R_PRIZE_SUMM).lower())
        if ans_float >= 4000:
            ans = input(ru_local.R_PRIZE_SUMM_4K).lower()
            if ans == ru_local.Y:
                total_tax += (ans_float - 4000) * 0.35
            else:
                total_tax += (ans_float - 4000) * 0.13

        else:
            pass

    else:

        # Privileges
        ans = input(ru_local.NR_WHO).lower
        if ans == ru_local.Y:
            ans = float(input(ru_local.SALARY))
            total_tax += ans * 0.13
        else:

            # Work for hire
            ans = input(ru_local.NR_HIRE_WORK).lower
            if ans == ru_local.Y:
                ans = float(input(ru_local.SALARY))
                if ans <= 5_000_000:
                    total_tax += ans * 0.13
                else:
                    total_tax += ans * 0.15
            else:
                ans = float(input(ru_local.SALARY))
                total_tax += ans * 0.3

        # Interest on deposits
        ans = float(input(ru_local.NR_PERC_CONTR))
        total_tax += ans * 0.13

        # Gift
        ans = input(ru_local.NR_GIFT).lower()
        if ans == ru_local.Y:
            ans = float(input(ru_local.NR_CADASTRAL_VALUE))
            total_tax += ans * 0.3
        
        # Interest on stocks
        ans = float(input(ru_local.NR_PERC_STOCK))
        total_tax += ans * 0.09

        # Dividends of international companies
        ans = float(input(ru_local.NR_DIV_INT))
        total_tax += ans * 0.05

        # Dividends of Russian companies
        ans = float(input(ru_local.NR_DIV_RU))
        total_tax += ans * 0.15

        # Property
        ans = input(ru_local.PROPERTY).lower()
        if ans == ru_local.Y:
            ans = float(input(ru_local.AMOUNT))
            total_tax += ans * 0.3
        else:
            pass

        # Cars
        ans = input(ru_local.CAR).lower() 
        if ans == ru_local.Y:
            ans = float(input(ru_local.CAR))
            total_tax += ans * 0.3

    print(total_tax)

if __name__ == '__main__':
    main()
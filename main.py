def main():
    """
    ##################################################
    Complete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    males = int(input("Enter the number of male students."))
    females = int(input("Enter the number of female students."))
    total = males + females
    float
    m_perc = (males / total) * 100
    float
    f_perc = (females / total) * 100
    print("The total number of students:\t\t", total)
    print("The number of males and females \t", males, '\t', females)
    print(
        f'The percentage of males and females \t {m_perc:.2f}%  {f_perc:.2f}%')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()

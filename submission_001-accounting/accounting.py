from user.authentication import authenticate_user
from transactions.journal import receive_income,pay_expense
import banking
import sys



def main():
    '''
    calls functions to print out required text
    '''
    #help("modules")
    for i in sys.argv:
        if i != sys.argv[0]:
            print(i)
        
    amount = 100
    authenticate_user()
    receive_income(amount)
    pay_expense(amount)
    #do_reconciliation()
    banking.do_reconciliation()
    #ubsa.do_reconciliation()
    #online.do_reconciliation()
    
    
if __name__ == '__main__':
    main()
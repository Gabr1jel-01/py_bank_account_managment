# import 



#deklaracija
def mask_ccn(ccn: str = '', 
             masking_symbol: str = '#',
             masking_limit_numbers: int = 4) -> str:
    
    masked_ccn = ''
    
    if ccn == '':
        print('Broj kreditne kartice ne moze biti prazan!')
        return # kao break u petlji prekida izvrsavanje funkcije
    
    lenght_credit_card_number = ccn[ : masking_limit_numbers]                
    for masked_number in lenght_credit_card_number:
        if masked_number == '-':
            masked_ccn += masked_number
        else:
            masked_ccn += masking_symbol

    masked_ccn += ccn[masking_limit_numbers : ]
    
    return masked_ccn
    

#main
credit_card_number = input('Upisite broj kreditne kartice: ')
masking_symbol = input('Upisite simbol sa kojim zelite zamaskirati brojeve: ')
#masking_symbol = '_'
masking_limit_numbers = int(input('Upisite limit maskiranja broja kartice: '))
masked_credit_card_number = mask_ccn(credit_card_number)

#end
print(f'Broj kreditne kartice {credit_card_number}')
if masked_credit_card_number != '': 
    print(f'Maskirani broj kreditne kartice: {masked_credit_card_number}')


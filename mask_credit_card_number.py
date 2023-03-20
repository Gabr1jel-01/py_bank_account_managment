# import 



#deklaracija
def mask_ccn(credit_card_number: str, masking_symbol: str) -> str:
    masked_ccn = ''
    
    lenght_credit_card_number = credit_card_number[ : -4]                
    for masked_number in lenght_credit_card_number:
        if masked_number == '-':
            masked_ccn += masked_number
        else:
            masked_ccn += masking_symbol

    masked_ccn += credit_card_number[-4 : ]
    
    return masked_ccn
    

#main
credit_card_number = input('Upisite broj kreditne kartice: ')
masking_symbol = input('Upisite simbol sa kojim zelite zamaskirati brojeve: ')
masked_credit_card_number = mask_ccn(credit_card_number, masking_symbol)

#end
print(f'Broj kreditne kartice {credit_card_number}')
print(f'Maskirani broj kreditne kartice: {masked_credit_card_number}')


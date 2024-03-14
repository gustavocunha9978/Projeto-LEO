product_value = float(input("What's the value of the product? "))

payment_terms = input("What will be the payment method? ( cash or check, credit, twice, twice with interest) ")

if payment_terms.lower() == 'cash' or payment_terms.lower() == 'check' :
    cash = product_value * 0.9
    print(f"Amount to be paid: ${cash:.2f}")
    
if payment_terms.lower() == 'credit':
    credit = product_value * 0.85
    print (f"Amount to be paid: ${credit:.2f}")
    
if payment_terms.lower() == 'twice':
    twice = product_value 
    print (f"Amount to be paid: ${twice:.2f}")
    
if payment_terms.lower() == 'twice with interest':
    twice_with_interest = product_value * 1.1
    print (f"Amount to be paid: ${twice_with_interest:.2f}")
      

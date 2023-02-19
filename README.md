# easymsgbox

### Create message boxes easily in Python
This module helps to create easy-to-use message boxes.

#### Installation

    pip install easymsgbox
   

#### Usage
  
    import easymsgbox as mb
    
    agreement = mb.agreement('Agreement', 'Are you agree?', is_cancel = True)
    if agreement == None:
        mb.alert('Sorry to bother!', 'Exiting.')
        exit()
    elif agreement:
        data_collect = mb.confrim('Thanks!', 'Starting collecting data, icon = 'warning')
        if data_collect:
            mb.alert('Done!', 'Have a nice day!')
        else:
            mb.alert('Data collecting canced!', 'Canceled by user')
    else:
        mb.alert('Oooh', 'Sorry', icon = 'error')

#### Compability
Compatatable with all Python 3 versions!

This is my first module ever! 


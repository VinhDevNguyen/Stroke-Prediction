import pickle 

def save_model(model, filename, mode ='wb'): 
    ''' 
    param: 
        model: sklearn model  
        filename: saved file name  
        mode: mode perform on file based on python file method  
    return: 
        None
    ''' 
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
    return 




def load_model(filename, mode ='rb'): 
    ''' 
    param: 
        filename: saved file name  
        mode: mode perform on file based on python file method  
    return: 
        model
    '''
    with open(filename, 'rb') as file:
        pickle_model = pickle.load(file)
    return pickle_model 

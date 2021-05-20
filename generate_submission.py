import pandas as pd 

def generate_submission(model, test_data, model_name = ""): 
    ''' 
    Generate submission based on given model and test set 
    param: 
        model: model must have predict method 
        test_data: dataframe 
        model_name  
    return: 
        None
    '''  
    test_data.drop(columns= 'Unnamed: 0', inplace=True)
    x = test_data.copy()
    x.drop(columns='id', inplace=True)
    id_test = test_data['id']
    y_pred = model.predict(x)

    data_test_submit = {'id': id_test, 'stroke': y_pred}
    df_test_submit = pd.DataFrame(data= data_test_submit)
    df_test_submit.to_csv('./Submission/submission_' + model_name + '.csv', index= False)

    return 
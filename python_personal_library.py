
#version fonction
def get_datasets(directory = "dataset") :
    """
    Récupère tous les datasets du dossier passé en paramètre.
    """
    from pathlib import Path # Créer un objet chemin absolu
    from os import listdir # Pour parcourir le dossier
    directory_path = './'+directory+'/'
    return listdir(directory_path)
    
    del listdir; del Path;
    
#********************************************************************************************************


from IPython.display import display_html
import pandas as pd # dataframe / Import CSV
def all_corr(p_dataframe) :
    '''
    Display correlation matrix by all the way pearson (default) / kendall / spearman
    
    parameters :
    ___________
    :p_dataframe : dataframe on which to do the correlation

    return:
    ______
    A string html
    '''
    display_side_by_side(
        p_dataframe.corr(method='pearson').style.background_gradient(cmap ='coolwarm'),
        p_dataframe.corr(method='kendall').style.background_gradient(cmap ='coolwarm'), 
        p_dataframe.corr('spearman').style.background_gradient(cmap ='coolwarm') 
    )
    #********************************************************************************************************
def display_side_by_side(*args):
    """
    display dataframes in row
    """


    from IPython.display import display_html
    html_str=''
    for df in args:
        type(df)
        if type(df) == pd.core.frame.DataFrame :
            html_str+=df.to_html()
        elif type (df) == pd.io.formats.style.Styler :
            html_str+=df.render()
    display_html(html_str.replace('table','table style="display:inline"'),raw=True); del display_html

#********************************************************************************************************

def exhaustiveDescribe(p_dataframe) : 
    """
    @parameter = Dataframe
    Display info, sum of nan, head6, shape & describe from a data frame in row 
    using "display_side_by_side" function from IPython.display import display_html
    set option to see all columns and all lines
    
    """
    pd.set_option('display.max_rows', p_dataframe.shape[0])
    pd.set_option('display.max_columns', p_dataframe.shape[1])
    pd.set_option('display.width', 1000)
    
    # Vars (it's useless to make var here, but I'm trying to change the style, but it doesn't work)
    df_shape = pd.DataFrame(p_dataframe.shape, index=['Lines', 'Columns'], columns=["Shape"])
    df_head = p_dataframe.head(6)
    df_info = pd.DataFrame(p_dataframe.info())
    df_nan = pd.DataFrame(p_dataframe.isna().sum(), columns=["Number of NaN"])
    df_describe = pd.DataFrame(p_dataframe.describe())
    
# Display dataframes or Styler side by side
    display_side_by_side(
        df_shape,
        df_head,
        df_info,
        df_nan,
        df_describe
    )
    
#********************************************************************************************************


def all_distplot(_bins=3) :
    """
    Affiche le distplot de chaque column
    """
    for column in df_all_data_diabete.columns :
        sns.distplot(df_all_data_diabete[column], bins=_bins)
        plt.title(column)
        plt.show()
    
#********************************************************************************************************

def describe_nans(_df) :
    """
    Display a dataframe with 3 columns :
        number of Nan by columns
        percent of Nan by columns
        remaining values count by columns
    """
    sum_na = _df.isna().sum()
    lines = _df.shape[0]
    df_temp= pd.DataFrame(sum_na, columns=["Number of NaN"])
    df_temp["Percents Nan"] = pd.DataFrame(sum_na/lines)
    df_temp["Values count"] = lines-sum_na
    df_temp.sort_values(by="Number of NaN", ascending=False).style.background_gradient()

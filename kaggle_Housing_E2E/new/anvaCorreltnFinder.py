from scipy.stats import f_oneway
def anova_correlation_calculator(df,st,y):
    cat_names = []
    for i in range(len(df[st].value_counts())):
        cat_names.append(df[st].value_counts().keys()[i])


    sec_list = [list(df[df[st] == i ][y]) for i in cat_names]
    final = f_oneway(*sec_list)
    if final[1] > 0.05:
        return "Correlated"
    else:
        return "Not Correlated"
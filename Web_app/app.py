# File Name          :    main.py
# Purpose            :    Machine Learning Model for Churn Prediction using Streamlit 
# Author             :    DeepSphere.AI, Inc.
# Date and Time      :    03/10/2020 11:00hrs 
# Version            :    0.83.0




import streamlit as vAR_st
import pandas as pd
from IPython.display import HTML
import time
import base64 
timestr = time.strftime("%Y%m%d-%H%M%S")
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from lime import lime_tabular
from streamlit import components
import numpy as np

#for Setting the page layout to wide
vAR_st.set_page_config(layout="wide")
col1, col2, col3 = vAR_st.columns([2, 5, 2])
with col1:
    vAR_st.write('')
with col2:
    vAR_st.image('https://raw.githubusercontent.com/tarun243/Streamlit-commonToAllIndustry/master/Web_app/Logo_final.png')
with col3:
    vAR_st.write('')

#setting font size and colour for the title 
#by this text-align: centre, we can align the title to the centre of the page
vAR_st.markdown("<h1 style='text-align: center; color: black; font-size:29px;'>Learn to Build Industry Standard Data Science Applications</h1>", unsafe_allow_html=True)

vAR_st.markdown("<p style='text-align: center; color: blue; font-size:29px;'>MLOPS Built On Google Cloud and Streamlit</p>", unsafe_allow_html=True)

vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Develop a Retail Machine Learning Applications (MLOPS): Customer Churn: Who is Going to Churn, When the Churn will Occur, Why it Occurs, and How to Prevent?</p>", unsafe_allow_html=True)

#for background color of sidebar
vAR_st.markdown("""<style>.css-1d391kg, .e1fqkh3o1 {
    background-color: #4c85e4;
    width: 19rem;
}
</style>""", unsafe_allow_html=True)



#for clear/reset button
vAR_st.markdown("""<style>.button  
{
    background-color:rgb(47 236 106);  
    top: 40px; 
    border: 0px solid; 
    padding: 10px;
    border-radius:3px; }
</style>""", unsafe_allow_html=True)


#for clear/reset button
vAR_st.markdown("""<style>p, ol, ul, dl {
    margin: 0px 80px 1rem;
    font-size: 1rem;
    font-weight: 400;
}
</style>""", unsafe_allow_html=True)

vAR_st.markdown("""<style>a {
    text-decoration: none;
}
</style>""", unsafe_allow_html=True)


#To customize the background colour of the submit button  
m = vAR_st.markdown("""
<style>
div.stButton > button:first-child {border: 1px solid; width: 55%;
    background-color: rgb(47 236 106) ;
}
</style>""", unsafe_allow_html=True)

m = vAR_st.markdown("""
<style>
div.stDownloadButton > button:first-child {border: 1px solid; width: 55%;
    background-color: rgb(47 236 106) ;
}
</style>""", unsafe_allow_html=True)

#for horizontal line
vAR_st.markdown("""
<hr style="width:100%;height:3px;background-color:gray;border-width:10">
""", unsafe_allow_html=True)


#for training the model 
def training(method):

  #training dataset
  training_data = df_training 
  training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]

  #feature selection for training
  training_data_features = training_data_features[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]

  #Label for Training
  training_data_label = training_data[['Churn']]

  #model training 
  model = method(random_state=42)
  model_training = model.fit(training_data_features,training_data_label)

  return model_training


#for testing the model
def testing(method):

  #training dataset
  training_data = df_training 
  training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]

  #feature selection for training
  training_data_features = training_data_features[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]

  #Label for Training
  training_data_label = training_data[['Churn']]

  #model training 
  # model = method()
  model_training = training(method)

  #Test Dataset
  test_data = df_testing

  #Feature Selection for Model Testing
  test_data_features = test_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
  test_data_features = training_data_features[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]

  #Model Testing
  model_testing = model_training.predict(test_data_features)
  model_prediction = pd.DataFrame(model_testing)
  model_prediction = pd.DataFrame(model_testing,columns=['Churn Prediction'])

  prediction_result = test_data.merge(model_prediction,left_index=True,right_index=True)
  vAR_st.write('')

  #Getting the Probability of Churn
  prediction_result_probability_all_features = model_training.predict_proba(test_data_features)
  prediction_result_probability_all_features = pd.DataFrame(prediction_result_probability_all_features,
    columns=['Probability of Non Churn', 'Probability of Churn'])
  churn_probability = prediction_result.merge(prediction_result_probability_all_features,
    left_index=True,right_index=True)
  table_7 = HTML(churn_probability.to_html(col_space=None,max_rows=10,max_cols=6))
  vAR_st.write(table_7)
  vAR_st.write('')

  # def explainable_ai():
  #   # Explainable AI Implementation
  #   vAR_st.write('')
  #   vAR_st.write('')
  #   vAR_st.subheader('Model Explainability with LIME package')
  #   vAR_st.write('')
  #   vAR_st.write('')
  #   interpreter = lime_tabular.LimeTabularExplainer(
  #   training_data=np.array(training_data_features),
  #   feature_names=training_data_features.columns,
  #   mode='classification'
  # )
  #   exp = interpreter.explain_instance(
  #   data_row=test_data_features.iloc[0], ##new data
  #   predict_fn=model_training.predict_proba
  # )
  #   print('$$$ len- ',len(test_data_features))
  #   components.v1.html(exp.as_html(), height=400)

  #   for idx in range(0,len(test_data_features)):
  #     exp = interpreter.explain_instance(
  #   data_row=test_data_features.iloc[idx], ##new data
  #   predict_fn=model_training.predict_proba
  # )
  #     vAR_st.write(str(test_data_features.iloc[idx]))
  #     vAR_st.write(str(exp.as_list()))


  # explainable_ai()

  


def explainable_ai(method):

  model_training = training(method)

  #training dataset
  training_data = df_training 
  training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]

  #Test Dataset
  test_data = df_testing

  #Feature Selection for Model Testing
  test_data_features = test_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
  test_data_features = training_data_features[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]


  #Model Testing
  model_testing = model_training.predict(test_data_features)
  model_prediction = pd.DataFrame(model_testing)
  model_prediction = pd.DataFrame(model_testing,columns=['Churn Prediction'])

  prediction_result = test_data.merge(model_prediction,left_index=True,right_index=True)
  vAR_st.write('')

  #Getting the Probability of Churn
  prediction_result_probability_all_features = model_training.predict_proba(test_data_features)
  prediction_result_probability_all_features = pd.DataFrame(prediction_result_probability_all_features,
    columns=['Probability of Non Churn', 'Probability of Churn'])
  churn_probability = prediction_result.merge(prediction_result_probability_all_features,
    left_index=True,right_index=True)


  # Explainable AI Implementation
  interpreter = lime_tabular.LimeTabularExplainer(
  training_data=np.array(training_data_features),
  feature_names=training_data_features.columns,
  mode='classification'
)
  exp = interpreter.explain_instance(
  data_row=test_data_features.iloc[0], ##new data
  predict_fn=model_training.predict_proba
)
  components.v1.html(exp.as_html(), height=400)
  churn_probability_trunc = churn_probability.copy()
  with vAR_st.spinner('Generating Prediction Explanation...'):
    vAR_exp_list = []
    for idx in range(0,len(test_data_features)):
        exp = interpreter.explain_instance(
      data_row=test_data_features.iloc[idx], ##new data
      predict_fn=model_training.predict_proba
    )
        vAR_exp_list.append(str(exp.as_list()))
    churn_probability_trunc['Explainable AI feature explanation'] = vAR_exp_list
    vAR_st.dataframe(churn_probability_trunc)
    churn_probability_trunc = churn_probability_trunc.to_csv().encode('utf-8')
    return churn_probability_trunc


# Used in streamlit<0.87
# def download_explainable_ai_result(vAR_df):
#   csv = vAR_df.to_csv(index=False)
#   b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
#   href = f'<a href="data:file/csv;base64,{b64}" download="explainable-ai.csv">Download csv file</a>'
#   return href

def test_code_log():
  with vAR_st.echo():
    #training dataset
    training_data = df_training 
    training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
    #feature selection for training
    training_data_features = training_data_features[['Customer Lifetime(Days)','Service Call','Service Failure Rate%','Price']]

    #Label for Training
    training_data_label = training_data[['Churn']]

    #model training 
    model = LogisticRegression()
    model_training = model.fit(training_data_features,training_data_label)

    #Test Dataset
    test_data = df_testing

    #Feature Selection for Model Testing
    test_data_features = test_data[['Customer Lifetime(Days)']]
    test_data_features = training_data_features[['Customer Lifetime(Days)','Service Call','Service Failure Rate%','Price']]

    #Model Testing
    model_testing = model.predict(test_data_features)
    model_prediction = pd.DataFrame(model_testing)
    model_prediction = pd.DataFrame(model_testing,columns=['Churn Prediction'])

    prediction_result = test_data.merge(model_prediction,left_index=True,right_index=True)

    #Getting the Probability of Churn
    prediction_result_probability_all_features = model.predict_proba(test_data_features)
    prediction_result_probability_all_features = pd.DataFrame(prediction_result_probability_all_features,
      columns=['Probability of Non Churn', 'Probability of Churn'])
    churn_probability = prediction_result.merge(prediction_result_probability_all_features,
      left_index=True,right_index=True)
    table_7 = HTML(churn_probability.to_html(col_space=None,max_rows=10,max_cols=6))


def visual_graphs(method):
  #training dataset
  training_data = df_training 
  training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]

  #feature selection for training
  training_data_features = training_data_features[['Customer Lifetime(Days)']]

  #Label for Training
  training_data_label = training_data[['Churn']]

  #model training 
  model = method()
  model_training = model.fit(training_data_features,training_data_label)

  #Test Dataset
  test_data = df_testing

  #Feature Selection for Model Testing
  test_data_features = test_data[['Customer Lifetime(Days)']]
  test_data_features = training_data_features[['Customer Lifetime(Days)']]

  #Model Testing
  model_testing = model.predict(test_data_features)
  model_prediction = pd.DataFrame(model_testing)
  model_prediction = pd.DataFrame(model_testing,columns=['Churn Prediction'])

  prediction_result = test_data.merge(model_prediction,left_index=True,right_index=True)
  vAR_st.write('')

  #Getting the Probability of Churn
  prediction_result_probability_all_features = model.predict_proba(test_data_features)
  prediction_result_probability_all_features = pd.DataFrame(prediction_result_probability_all_features,
    columns=['Probability of Non Churn', 'Probability of Churn'])
  churn_probability = prediction_result.merge(prediction_result_probability_all_features,
    left_index=True,right_index=True)
  #table_7 = HTML(churn_probability.to_html(col_space=None,max_rows=10,max_cols=7))
  return churn_probability;

def train_code_log():
  with vAR_st.echo():
    def training():

      #training data
      training_data = df_training 
      training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
      #feature selection for training
      training_data_features = training_data_features[['Customer Lifetime(Days)']]

      #Label for Training
      training_data_label = training_data[['Churn']]

      #model training 
      model = LogisticRegression()
      model_training = model.fit(training_data_features,training_data_label)


def test_code_ran():
  with vAR_st.echo():
    #training dataset
    training_data = df_training 
    training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
    #feature selection for training
    training_data_features = training_data_features[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]

    #Label for Training
    training_data_label = training_data[['Churn']]

    #model training 
    model = RandomForestClassifier()
    model_training = model.fit(training_data_features,training_data_label)

    #Test Dataset
    test_data = df_testing

    #Feature Selection for Model Testing
    test_data_features = test_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
    test_data_features = training_data_features[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]

    #Model Testing
    model_testing = model.predict(test_data_features)
    model_prediction = pd.DataFrame(model_testing)
    model_prediction = pd.DataFrame(model_testing,columns=['Churn Prediction'])

    prediction_result = test_data.merge(model_prediction,left_index=True,right_index=True)

    #Getting the Probability of Churn
    prediction_result_probability_all_features = model.predict_proba(test_data_features)
    prediction_result_probability_all_features = pd.DataFrame(prediction_result_probability_all_features,
      columns=['Probability of Non Churn', 'Probability of Churn'])
    churn_probability = prediction_result.merge(prediction_result_probability_all_features,
      left_index=True,right_index=True)
    table_7 = HTML(churn_probability.to_html(col_space=None,max_rows=10,max_cols=6))
    vAR_st.write(table_7)


def train_code_ran():
  with vAR_st.echo():
    def training():

      #training data
      training_data = df_training 
      training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
      #feature selection for training
      training_data_features = training_data_features[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]

      #Label for Training
      training_data_label = training_data[['Churn']]

      #model training 
      model = RandomForestClassifier()
      model_training = model.fit(training_data_features,training_data_label)


def test_code_dec():
  with vAR_st.echo():
    #training dataset
    training_data = df_training 
    training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
    #feature selection for training
    training_data_features = training_data_features[['Customer Lifetime(Days)']]

    #Label for Training
    training_data_label = training_data[['Churn']]

    #model training 
    model = DecisionTreeClassifier()
    model_training = model.fit(training_data_features,training_data_label)

    #Test Dataset
    test_data = df_testing

    #Feature Selection for Model Testing
    test_data_features = test_data[['Customer Lifetime(Days)']]
    test_data_features = training_data_features[['Customer Lifetime(Days)']]

    #Model Testing
    model_testing = model.predict(test_data_features)
    model_prediction = pd.DataFrame(model_testing)
    model_prediction = pd.DataFrame(model_testing,columns=['Churn Prediction'])

    prediction_result = test_data.merge(model_prediction,left_index=True,right_index=True)

    #Getting the Probability of Churn
    prediction_result_probability_all_features = model.predict_proba(test_data_features)
    prediction_result_probability_all_features = pd.DataFrame(prediction_result_probability_all_features,
      columns=['Probability of Non Churn', 'Probability of Churn'])
    churn_probability = prediction_result.merge(prediction_result_probability_all_features,
      left_index=True,right_index=True)
    table_7 = HTML(churn_probability.to_html(col_space=None,max_rows=10,max_cols=6))
    vAR_st.write(table_7)


def train_code_dec():
  with vAR_st.echo():
    def training():

      #training data
      training_data = df_training 
      training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
      #feature selection for training
      training_data_features = training_data_features[['Customer Lifetime(Days)']]

      #Label for Training
      training_data_label = training_data[['Churn']]

      #model training 
      model = DecisionTreeClassifier()
      model_training = model.fit(training_data_features,training_data_label)


#to download model outcome 
def download(method):

  #training dataset
  training_data = df_training 
  training_data_features = training_data[['Quantity','Price','Service Call','Service Failure Rate%','Customer Lifetime(Days)']]
            
  #feature selection for training
  training_data_features = training_data_features[['Customer Lifetime(Days)']]

  #Label for Training
  training_data_label = training_data[['Churn']]

  #model training 
  model = method()
  model_training = model.fit(training_data_features,training_data_label)

  #Test Dataset
  test_data = df_testing

  #Feature Selection for Model Testing
  test_data_features = test_data[['Customer Lifetime(Days)']]
  test_data_features = training_data_features[['Customer Lifetime(Days)']]

  #Model Testing
  model_testing = model.predict(test_data_features)
  model_prediction = pd.DataFrame(model_testing)
  model_prediction = pd.DataFrame(model_testing,columns=['Churn Prediction'])

  prediction_result = test_data.merge(model_prediction,left_index=True,right_index=True)
  vAR_st.write('')

  #Getting the Probability of Churn
  prediction_result_probability_all_features = model.predict_proba(test_data_features)
  prediction_result_probability_all_features = pd.DataFrame(prediction_result_probability_all_features,
    columns=['Probability of Non Churn', 'Probability of Churn'])
  churn_probability = prediction_result.merge(prediction_result_probability_all_features,
    left_index=True,right_index=True)

  csvfile = churn_probability.to_csv()
  b64 = base64.b64encode(csvfile.encode()).decode()
  vAR_filename = "new_text_file_{}_.csv".format(timestr)
  #vAR_st.markdown("#### Download File ###")
  href = f'<a href="data:file/csv;base64,{b64}" download="{vAR_filename}">Download!!</a>'
  vAR_st.markdown(href,unsafe_allow_html=True)
  

#for visual charts
def visual_6(data):
  print('visual 6 - data - ',type(data))
  print('visual 6 - data - ',data.columns)
  percentage = (cum_churn/60)*100
  fig = go.Figure(
    data=[go.Scatter(
      x=data['When the Churn Occurs'],
      y=cum_churn,
      marker_color='#483D8B'
    )],

    layout=go.Layout(
      title=go.layout.Title(text="When the Churn Occurs")))
  fig.update_xaxes(
      title_text = "Days",showgrid=False)
  fig.update_yaxes(
      title_text = "Percentage of Churn",showgrid=False)
  fig.update_layout(plot_bgcolor='rgba(0,0,0,1.0)')
  vAR_st.plotly_chart(fig)


#for visual charts
def visual_5(data):
  percentage = (cum_churn/60)*100
  fig = go.Figure(
    data=[go.Scatter(
      x=data['Service Start Date'],
      y=cum_churn,
      marker_color='black'
    )],
    layout=go.Layout(
      title=go.layout.Title(text="Churn Trend")))
  fig.update_xaxes(
      title_text = "Year")
  fig.update_yaxes(
      title_text = "Percentage of Churn")

  vAR_st.plotly_chart(fig)


#for visual charts
def visual_3(data):
    group = data.groupby('Gender')
    new_df = group.size().reset_index(name='Count')
    new_df = new_df.sort_values('Count')


    colors = ['lightslategray',] * 2
    colors[0] = '#1E90FF'
    colors[1] = '#9400D3'
    fig = go.Figure()


    fig = go.Figure(data=[go.Bar(
        x=new_df['Gender'],
        y=new_df['Count'],
        marker_color=colors
    )])
    fig.update_xaxes(
        title_text = "Gender")
    fig.update_yaxes(
        title_text = "Churn Count")

    fig.update_layout(title_text='Customer Churn Count By Gender')
    vAR_st.plotly_chart(fig)


#for visual charts
def visual_4(data):
    group = data.groupby('Reason for The customer to Churn / Non Churn')
    new_df = group.size().reset_index(name='counts')
    new_df = new_df.sort_values('counts')


    colors = ['lightslategray',] * 3
    colors[0] = '#00FA9A'
    colors[1] = '#7B68EE'
    colors[2] = '#708090'
    fig = go.Figure()


    fig = go.Figure(data=[go.Bar(
        x=new_df['Reason for The customer to Churn / Non Churn'],
        y=new_df['counts'],
        marker_color=colors # marker color can be a single color value or an iterable
    )])
    fig.update_xaxes(
        title_text = "Reason to Churn")
    fig.update_yaxes(
        title_text = "Churn Count")

    fig.update_layout(title_text='Customer Churn Count By Reason')
    vAR_st.plotly_chart(fig)


#for visual charts
def visual_1(data):
  no = data['Churn Prediction'].tolist().count(0)
  yes = data['Churn Prediction'].tolist().count(1)

  labels = 'Non Churn', 'Churn'
  sizes = [no, yes]
  explode = (0, 0.1)
  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
  vAR_st.pyplot(fig1)


#for visual charts
def visual_2(data):
  m = data['Gender'].tolist().count('Male')
  f = data['Gender'].tolist().count('Female')
  labels = 'Female', 'Male'
  sizes = [f, m]
  explode = (0, 0.1)
  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
  vAR_st.pyplot(fig1)


#for extract feature 
def feature():
  features = df_training.drop(['CustomerID','Churn'], axis =1)
  for col in training_data_features_s:
    vAR_st.write(col)

def feature_code():
  with vAR_st.echo():
    def feature():
      training_data_features_s = vAR_st.multiselect('Select the features to train the model',feature_col)
      vAR_st.write(str(training_data_features_s))

#hyperparameter
def hyperparamater():
    for ele in hyperparameters:
        vAR_st.write(ele)

menu = ["Home","Model Validation","Download Model Outcome","Data visualization","Deploy the Model"]
choice = vAR_st.sidebar.selectbox("Menu",menu)

#for problem statement selection box
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col5:
    vAR_st.write('')
with col2:
    vAR_st.write('')
    vAR_st.write('')
    vAR_st.subheader("Problem Statement")
with col3:
    vAR_problem = vAR_st.selectbox('',('Select the Problem Statement','Customer Churn: Who is going to churn?','Customer Churn: When will the churn occur?','Customer Churn: Why does the churn occurs?'),index=0)


#for problem type selection type
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col5:
    vAR_st.write('')
with col2:
  if vAR_problem != 'Select the Problem Statement':
    vAR_st.write('')
    vAR_st.write('')
    vAR_st.subheader("Problem type")
with col3:
  if vAR_problem != 'Select the Problem Statement':
    vAR_type = vAR_st.selectbox('',('Select the Problem type','Classification','Regression','Clustering','Continued Decision Making'),index=0)


#for model selection selection model 
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col2:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      vAR_st.write('')
      vAR_st.write('')
      vAR_st.subheader("Model Selection")
with col5:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      vAR_st.write('')
      vAR_st.write('')
      model_selection_source_code = vAR_st.button('Source Code',key='13')
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      vAR_model = vAR_st.selectbox('',('Select the Model','Decision Tree','Random Forest','Logistic Regression','Linear Regression','K Means Clustering'),index=0)
      if model_selection_source_code:
        if vAR_model == 'Decision Tree':
          with vAR_st.echo():
            if vAR_model == 'Decision Tree':
              import pandas as pd
              from sklearn.tree import DecisionTreeClassifier
              import matplotlib.pyplot as plt
              import plotly.graph_objects as go
        elif vAR_model == 'Random Forest':
          with vAR_st.echo():
            if vAR_model == 'Random Forest':
              import pandas as pd
              from sklearn.ensemble import RandomForestClassifier
              import matplotlib.pyplot as plt
              import plotly.graph_objects as go              
        elif vAR_model == 'Logistic Regression':
          with vAR_st.echo():
            if vAR_model == 'Logistic Regression':
              import pandas as pd
              from sklearn.linear_model import LogisticRegression
              import matplotlib.pyplot as plt
              import plotly.graph_objects as go              
        elif vAR_model == 'Linear Regression':
          with vAR_st.echo():
            if vAR_model == 'Linear Regression':
              import pandas as pd
              from sklearn.linear_model import LinearRegression
              import matplotlib.pyplot as plt
              import plotly.graph_objects as go              
        elif vAR_model == 'K Means Clustering':
          with vAR_st.echo():
            if vAR_model == 'K Means Clustering':
              import pandas as pd
              from sklearn.cluster import KMeans
              import matplotlib.pyplot as plt
              import plotly.graph_objects as go              


#for uploading training dataset
vAR_st.write('')
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col2:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        vAR_st.write('')
        vAR_st.write('')
        vAR_st.subheader("Training Dataset")
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        vAR_training_data = vAR_st.file_uploader("Upload CSV file")
with col5:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data is not None:
          if vAR_training_data.type == 'application/vnd.ms-excel':
            df_training = pd.read_csv(vAR_training_data, encoding = 'unicode_escape',error_bad_lines=False)
            vAR_st.markdown('#')
            vAR_st.write('')
            preview_training = vAR_st.button('Preview', key="1")
          elif vAR_training_data.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            df_training = pd.read_excel(vAR_training_data)
            vAR_st.markdown('#')
            vAR_st.write('')
            preview_training = vAR_st.button('Preview', key="1")
          else:
            vAR_st.markdown('#')
            vAR_st.write('Upload CSV file you uploaded',vAR_training_data.type)


col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col5:
    vAR_st.write('')
with col2:
    vAR_st.write('')
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data is not None:
          if vAR_training_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            full_table_1 = vAR_st.button('Click for all Set of rows')


#to preview the uploaded training file  
if vAR_problem != 'Select the Problem Statement':
  if vAR_type != 'Select the Problem type':
    if vAR_model != 'Select the Model':
      if vAR_training_data is not None:
        if vAR_training_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
          if preview_training:
            table_1 = HTML(df_training.to_html(col_space=None,max_rows=7,max_cols=6))
            vAR_st.write(table_1)
          vAR_st.write('')  
          if full_table_1:
            table_2 = HTML(df_training.to_html(col_space=None))
            vAR_st.write(table_2)           



#for feature engineering 
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col2:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          vAR_st.subheader("Feature Engineering")
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          vAR_st.write('')
          features_1 = df_training.drop(['CustomerID','Churn'], axis =1)
          feature_col = features_1.columns
          training_data_features_s = vAR_st.multiselect('Select the features to train the model',feature_col)
          vAR_st.write(str(training_data_features_s))

with col5:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          vAR_st.write('')
          feature_source_code = vAR_st.button('Source Code',key='12')

#to display feature engineering source code
if vAR_problem != 'Select the Problem Statement':
  if vAR_type != 'Select the Problem type':
    if vAR_model != 'Select the Model':
      if vAR_training_data:
        if feature_source_code:
          feature_code()
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col5:
    vAR_st.write('')
with col2:
    vAR_st.write('')
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          vAR_st.write('')
          button_feature = vAR_st.button('Extract Feature')
          vAR_st.write('')  

col1, col2, col3, col4, col5= vAR_st.columns([0.25,1.5,3.5,5,0.5])
with col1:
    vAR_st.write('')
with col5:
    vAR_st.write('')
with col2:
    vAR_st.write('')
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          if button_feature:
            features = df_training.drop(['CustomerID','Churn'], axis =1)
            for i in range(len(training_data_features_s)):
              vAR_st.write('Feature ',i+1)  
with col4:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          if button_feature:
            feature()

#for hyperparameter tuning
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col5:
    vAR_st.write('')
with col2:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          vAR_st.subheader("Hyperparameter Tuning")
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          if vAR_model == 'Logistic Regression':
            vAR_st.write('')
            hyperparameters = vAR_st.slider('max_iter:', 100, 1000, 100)
            vAR_st.write(str(hyperparameters))
          if (vAR_model == 'Decision Tree') or (vAR_model == 'Random Forest'):
            vAR_st.write('')
            hyperparameters = vAR_st.selectbox('criterion:', ['gini', 'entropy'])
            vAR_st.write(str(hyperparameters))
          if vAR_model == 'K Means Clustering':
            vAR_st.write('')
            hyperparameters = vAR_st.slider('n_clusters:', 2, 30, 8)
            vAR_st.write(str(hyperparameters))

col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col5:
    vAR_st.write('')
with col2:
    vAR_st.write('')
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          vAR_st.write('')
          button_feature = vAR_st.button('Set Hyperparameter')
          vAR_st.write('')

#for training the dataset 
vAR_st.write('') 
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col2:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          vAR_st.subheader("Model Engineering")
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          vAR_st.write('')
          button_train = vAR_st.button('Train the Model')
          if button_train:
            vAR_st.image('https://i.gifer.com/IPNp.gif',width = 200)
            if vAR_model == "Logistic Regression":
              method = LogisticRegression
              training(method)
            elif vAR_model == "Random Forest":
              method = RandomForestClassifier
              training(method)
            elif vAR_model == "Decision Tree":
              method = DecisionTreeClassifier
              training(method)
            vAR_success = vAR_st.success('Model training completed')
with col5:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          vAR_st.write('')
          train_source_code = vAR_st.button('Source Code',key="10")



#to display traning code
if vAR_problem != 'Select the Problem Statement':
  if vAR_type != 'Select the Problem type':
    if vAR_model != 'Select the Model':
      if vAR_training_data:
        if train_source_code:
          if vAR_model == "Logistic Regression":
            train_code_log()
          elif vAR_model == "Random Forest":
            train_code_ran()
          elif vAR_model == "Decision Tree":
            train_code_dec()


#to test the model 
vAR_st.write('')
col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col2:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          #time.sleep(10)
          vAR_st.write('')
          vAR_st.write('')
          vAR_st.markdown('#')
          vAR_st.subheader('Model Engineering')
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          vAR_st.subheader('Test the Model')
          vAR_testing_data = vAR_st.file_uploader("upload CSV file")
with col5:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel':
              df_testing = pd.read_csv(vAR_testing_data, encoding = 'unicode_escape',error_bad_lines=False)
              vAR_st.markdown('#')
              vAR_st.markdown('#')
              vAR_st.write('')
              preview_testing = vAR_st.button('Preview', key="2")
            elif vAR_training_data.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
              df_testing = pd.read_excel(vAR_testing_data)
              vAR_st.markdown('#')
              vAR_st.markdown('#')
              vAR_st.write('')
              preview_testing = vAR_st.button('Preview', key="2")
            else:
              vAR_st.markdown('#')
              vAR_st.write('Upload CSV file you uploaded',vAR_testing_data.type)



col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col5:
    vAR_st.write('')
with col2:
    vAR_st.write('')
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 
              vAR_st.write('')
              full_table_2 = vAR_st.button('Click for all Set of Rows')



if vAR_problem != 'Select the Problem Statement':
  if vAR_type != 'Select the Problem type':
    if vAR_model != 'Select the Model':
      if vAR_training_data:
        if vAR_testing_data is not None:
          if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            if preview_testing:
              table_3 = HTML(df_testing.to_html(col_space=None,max_rows=7,max_cols=6))
              vAR_st.write(table_3)
            vAR_st.write('')  
            if full_table_2:
              table_4 = HTML(df_testing.to_html(col_space=None))
              vAR_st.write(table_4)
            vAR_st.write('')



col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col2:
    vAR_st.write('')
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 
              button_test = vAR_st.button('Test the Model')
              if button_test:
                vAR_st.image('https://i.gifer.com/IPNp.gif',width = 200)
                vAR_success_1 = vAR_st.success('Model testing completed')
with col5:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':             
              test_source_code = vAR_st.button('Source Code',key="11")




#to display test code
if vAR_problem != 'Select the Problem Statement':
  if vAR_type != 'Select the Problem type':
    if vAR_model != 'Select the Model':
      if vAR_training_data:
        if vAR_testing_data is not None:
          if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            if test_source_code:
              if vAR_model == "Logistic Regression":
                test_code_log()
              elif vAR_model == "Random Forest":
                test_code_ran()
              elif vAR_model == "Decision Tree":
                test_code_dec()



col1, col2, col4 = vAR_st.columns([0.5,4,0.5])
with col1:
    vAR_st.write('')
with col4:
    vAR_st.write('')
with col2:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
              if button_test:
                if vAR_model == "Logistic Regression":
                  method = LogisticRegression
                  testing(method)
                elif vAR_model == "Random Forest":
                  method = RandomForestClassifier
                  testing(method)
                elif vAR_model == "Decision Tree":
                  method = DecisionTreeClassifier
                  testing(method)


# to display explainable ai
col1, col2, col3 = vAR_st.columns([0.25,1.5,4.75])
with col1:
    vAR_st.write('')

with col2:
    if vAR_problem != 'Select the Problem Statement':
      if vAR_type != 'Select the Problem type':
        if vAR_model != 'Select the Model':
          if vAR_training_data:
            if vAR_testing_data is not None:
              if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                #time.sleep(10)
                vAR_st.write('')
                vAR_st.write('')
                vAR_st.markdown('#')
                vAR_st.subheader('Explainable AI')
with col3:
  if vAR_problem != 'Select the Problem Statement':
    if vAR_type != 'Select the Problem type':
      if vAR_model != 'Select the Model':
        if vAR_training_data:
          if vAR_testing_data is not None:
            if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 
              vAR_st.write('')
              vAR_st.write('')
              vAR_st.write('')
              vAR_st.write('')
              vAR_st.write('')
              button_test = vAR_st.button('Click Here to Know the Prediction Explanation')
              if button_test:
                if vAR_model == "Logistic Regression":
                  method = LogisticRegression
                  churn_probability_trunc = explainable_ai(method)
                  vAR_st.write('')
                  vAR_st.write('')
                  vAR_st.download_button(label='Download Explainable AI Outcome', data = churn_probability_trunc, file_name='explainable-ai.csv',mime='text/csv')
                elif vAR_model == "Random Forest":
                  method = RandomForestClassifier
                  churn_probability_trunc = explainable_ai(method)
                  vAR_st.write('')
                  vAR_st.write('')
                  vAR_st.download_button(label='Download Explainable AI Outcome', data = churn_probability_trunc, file_name='explainable-ai.csv',mime='text/csv')
                elif vAR_model == "Decision Tree":
                  method = DecisionTreeClassifier
                  churn_probability_trunc = explainable_ai(method)
                  vAR_st.write('')
                  vAR_st.write('')
                  vAR_st.download_button(label='Download Explainable AI Outcome', data = churn_probability_trunc, file_name='explainable-ai.csv',mime='text/csv')
                else:
                  vAR_st.error('Please select the different model')


vAR_st.markdown('#')
if choice == "Home":
  pass

if choice == "Model Validation":
  col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
  with col1:
    vAR_st.write('')
  with col4:
    vAR_st.write('')
  with col5:
    vAR_st.write('')
  with col2:
    vAR_st.subheader("Model Validation")
  with col3:
    vAR_st.button("Click here", key="6")

#to download the model outcome 
if choice == "Download Model Outcome":
  col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
  with col1:
    vAR_st.write('')
  with col4:
    vAR_st.write('')
  with col5:
    vAR_st.write('')
  with col2:  
    vAR_st.subheader("Download Model Outcome")
  with col3:
    if vAR_problem != 'Select the Problem Statement':
      if vAR_type != 'Select the Problem type':
        if vAR_model != 'Select the Model':
          if vAR_training_data is not None:
            if vAR_testing_data is not None:
              if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                button_download = vAR_st.button("Click here", key="9")
                if button_download:
                  if vAR_model == "Logistic Regression":
                    method = LogisticRegression
                    download(method)
                  elif vAR_model == "Random Forest":
                    method = RandomForestClassifier
                    download(method)
                  elif vAR_model == "Decision Tree":
                    method = DecisionTreeClassifier
                    download(method)
                

#to display visual charts 
if choice == "Data visualization":
  col1, col2, col3, col4, col5 = vAR_st.columns([0.25,1.5,2.75,0.25,1.75])
  with col1:
    vAR_st.write('')
  with col4:
    vAR_st.write('')
  with col5:
    vAR_st.write('')
  with col2:  
    vAR_st.subheader("Data visualization")
  with col3:
    visual_button = vAR_st.button("Visual Charts", key="8")
    if vAR_problem != 'Select the Problem Statement':
      if vAR_type != 'Select the Problem type':
        if vAR_model != 'Select the Model':
          if vAR_training_data:
            if vAR_testing_data is not None:
              if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                if visual_button:   
                  if vAR_model == "Random Forest":
                    method = RandomForestClassifier
                    data = visual_graphs(method)
                    visual_1(data)
                  elif vAR_model == "Logistic Regression":
                    method = LogisticRegression
                    data = visual_graphs(method)
                    visual_1(data)
                  elif vAR_model == "Decision Tree":
                    method = DecisionTreeClassifier
                    data = visual_graphs(method)
                    visual_1(data)


  with col3:
    if vAR_problem != 'Select the Problem Statement':
      if vAR_type != 'Select the Problem type':
        if vAR_model != 'Select the Model':
          if vAR_training_data:
            if vAR_testing_data is not None:
              if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                if visual_button:   
                  if vAR_model == "Random Forest":
                    method = RandomForestClassifier
                    data = visual_graphs(method)
                    visual_2(data)
                  elif vAR_model == "Logistic Regression":
                    method = LogisticRegression
                    data = visual_graphs(method)
                    visual_2(data)
                  elif vAR_model == "Decision Tree":
                    method = DecisionTreeClassifier
                    data = visual_graphs(method)
                    visual_2(data)

  col1, col2, col3 = vAR_st.columns([1,3,1])
  with col1:
    vAR_st.write('')
  with col3:
    vAR_st.write('')
  with col2:
    if vAR_problem != 'Select the Problem Statement':
      if vAR_type != 'Select the Problem type':
        if vAR_model != 'Select the Model':
          if vAR_training_data:
            if vAR_testing_data is not None:
              if vAR_testing_data.type == 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                if visual_button:   
                  if vAR_model == "Random Forest":
                    method = RandomForestClassifier
                    data = visual_graphs(method)
                    ch = data['Churn Prediction']
                    cum_churn = ch.cumsum()
                    visual_3(data)
                    visual_4(data)
                    visual_5(data)
                    # visual_6(data)
                  elif vAR_model == "Logistic Regression":
                    method = LogisticRegression
                    data = visual_graphs(method)
                    ch = data['Churn Prediction']
                    cum_churn = ch.cumsum()
                    visual_3(data)
                    visual_4(data)        
                    visual_5(data)
                    # visual_6(data)
                  elif vAR_model == "Decision Tree":
                    method = DecisionTreeClassifier
                    data = visual_graphs(method)
                    ch = data['Churn Prediction']
                    cum_churn = ch.cumsum()
                    visual_3(data)
                    visual_4(data)
                    visual_5(data)
                    # visual_6(data)


if choice == "Deploy the Model":
  vAR_st.subheader("To Deploy the Model")



library = ["Library Used","Streamlit","Pandas","IPython.display","sklearn.linear_model"]
lib = vAR_st.sidebar.selectbox(" ",library)

models_implemented = ['Models Implemented','Decision Tree','Random Forest','Logistic Regression']
mi = vAR_st.sidebar.selectbox(" ",models_implemented)

services = ["GCP Services Used","VM Instance","Compute Engine",'Cloud Storage']
gcp = vAR_st.sidebar.selectbox(" ",services)


href = f'<a style="color:black;" href="http://localhost:8501/" class="button">Clear/Reset</a>'
vAR_st.sidebar.markdown(href, unsafe_allow_html=True)




# Disclaimer.
# We are providing this code block strictly for learning and researching, this is not a production
# ready code. We have no liability on this particular code under any circumstances; users should
# use this code on their own risk. All software, hardware and othr products that are referenced
# in these materials belong to the respective vendor who developed or who owns this product.


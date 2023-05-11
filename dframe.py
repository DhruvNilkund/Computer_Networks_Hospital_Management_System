import pandas as pd
from pathlib import Path

# path = Path("C:/Users/Desktop/Sem-5/CS301 CN/Project/Voting/database")
path = Path("database")

def count_reset():
    df=pd.read_csv(path/'PatientList.csv')
    df=df[['Patient_id','Name','Gender','Zone','City','Passw','admitted']]
    for index, row in df.iterrows():
        df['admitted'].iloc[index]=0
    df.to_csv(path/'PatientList.csv')

    df=pd.read_csv(path/'dept_list.csv')
    df=df[['Sign','Department','Bed Count']]
    for index, row in df.iterrows():
        df['Bed Count'].iloc[index]=0
    df.to_csv (path/'dept_list.csv')


def reset_voter_list():
    df = pd.DataFrame(columns=['Patient_id','Name','Gender','Zone','City','Passw','admitted'])
    df=df[['Patient_id','Name','Gender','Zone','City','Passw','admitted']]
    df.to_csv(path/'PatientList.csv')

def reset_cand_list():
    df = pd.DataFrame(columns=['Sign','Department','Bed Count'])
    df=df['Sign','Department','Bed Count']
    df.to_csv(path/'dept_list.csv')


def verify(vid,passw):
    df=pd.read_csv(path/'PatientList.csv')
    df=df[['Patient_id','Passw','admitted']]
    for index, row in df.iterrows():
        if df['Patient_id'].iloc[index]==vid and df['Passw'].iloc[index]==passw:
            return True
    return False


def isEligible(vid):
    df=pd.read_csv(path/'PatientList.csv')
    df=df[['Patient_id','Name','Gender','Zone','City','Passw','admitted']]
    for index, row in df.iterrows():
        if df['Patient_id'].iloc[index]==vid and df['admitted'].iloc[index]==0:
            return True
    return False


def vote_update(st,vid):
    if isEligible(vid):
        df=pd.read_csv (path/'dept_list.csv')
        df=df[['Sign','Department','Bed Count']]
        for index, row in df.iterrows():
            if df['Sign'].iloc[index]==st:
                if df['Bed Count'].iloc[index]==0:
                    return False
                df['Bed Count'].iloc[index]-=1

        df.to_csv (path/'dept_list.csv')

        df=pd.read_csv(path/'PatientList.csv')
        df=df[['Patient_id','Name','Gender','Zone','City','Passw','admitted']]
        for index, row in df.iterrows():
            if df['Patient_id'].iloc[index]==vid:
                df['admitted'].iloc[index]=1

        df.to_csv(path/'PatientList.csv')

        return True
    return False


def show_result():
    df=pd.read_csv (path/'dept_list.csv')
    df=df[['Sign','Department','Bed Count']]
    v_cnt = {}
    for index, row in df.iterrows():
        v_cnt[df['Sign'].iloc[index]] = df['Bed Count'].iloc[index]
    # print(v_cnt)
    return v_cnt


def taking_data_voter(name,gender,zone,city,passw):
    df=pd.read_csv(path/'PatientList.csv')
    df=df[['Patient_id','Name','Gender','Zone','City','Passw','admitted']]
    row,col=df.shape
    if row==0:
        vid = 10001
        df = pd.DataFrame({"Patient_id":[vid],
                    "Name":[name],
                    "Gender":[gender],
                    "Zone":[zone],
                    "City":[city],
                    "Passw":[passw],
                    "admitted":[0]},)
    else:
        vid=df['Patient_id'].iloc[-1]+1
        df1 = pd.DataFrame({"Patient_id":[vid],
                    "Name":[name],
                    "Gender":[gender],
                    "Zone":[zone],
                    "City":[city],
                    "Passw":[passw],
                    "admitted":[0]},)

        df=df.append(df1,ignore_index=True)

    df.to_csv(path/'PatientList.csv')

    return vid

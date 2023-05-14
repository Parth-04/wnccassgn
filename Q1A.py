# Caution: Code Incomplete!
import itertools

N = int(input("Enter the number of participants: "))        #Number of Participants
participant_data = []
print("Enter the participant data in the following format: Roll_Number[SPACE]HTML_Skill_Level[SPACE]Python_Skill_Level[SPACE]DSA_Skill_Level[SPACE]Java_Skill_Level[SPACE]SQL_Skill_Level: ")

html_prt = {}       #{Roll_Number: Skill Level}
python_prt = {}     #{Roll_Number: Skill Level}
dsa_prt = {}        #{Roll_Number: Skill Level}
java_prt = {}       #{Roll_Number: Skill Level} 
sql_prt = {}        #{Roll_Number: Skill Level}
prt_list = []       #Roll Number list of all participants

for i in range(N):
    data = input("Enter data: ")
    participant_data.append(data)
    data_list = data.split(" ")
    print(data_list)
    prt_list.append(data_list[0])
    html_prt[data_list[0]] = data_list[1]
    python_prt[data_list[0]] = data_list[2]
    dsa_prt[data_list[0]] = data_list[3]
    java_prt[data_list[0]] = data_list[4]
    sql_prt[data_list[0]] = data_list[5]


M = int(input("Enter the number of projects: "))        #Number of Projects
project_data = []
print("Enter the project data in the following format: Project_Name(In One Word)[SPACE]HTML_Skill_Level_Required[SPACE]Python_Skill_Level_Required[SPACE]DSA_Skill_Level_Required[SPACE]Java_Skill_Level_Required[SPACE]SQL_Skill_Level_Required: ")

html_prj = {}       #{Project: Skill Level}
python_prj = {}     #{Project: Skill Level}
dsa_prj = {}        #{Project: Skill Level}
java_prj = {}       #{Project: Skill Level}
sql_prj = {}        #{Project: Skill Level}
prj_list = []       #List of all projects

for i in range(M):
    data = input("Enter data: ")
    project_data.append(data)
    data_list = data.split(" ")
    prj_list.append(data_list[0])
    html_prj[data_list[0]] = data_list[1]
    python_prj[data_list[0]] = data_list[2]
    dsa_prj[data_list[0]] = data_list[3]
    java_prj[data_list[0]] = data_list[4]
    sql_prj[data_list[0]] = data_list[5]



temp_part_data = participant_data
temp_proj_data = project_data


permutations = list(itertools.permutations(prt_list))
prj_num = []

for permutation in permutations:
    compl_prj = 0
    prt_list = list(permutation)
    for i in prj_list:
        flag = 0
        prt_slc = {}        #{Role:Roll_Number}

        
        if (html_prj[i] == "0"):
            pass
        else:
            for j in prt_list:
                if (int(html_prt[j]) >= int(html_prj[i])):
                    prt_slc["html"] = j
                    #print("Participant ",j," selected for HTML in Project ",i)
                    prt_list.remove(j)
                    break
                elif (int(html_prt[j]) == int(html_prj[i]) - 1):
                    for k in prt_slc.values():
                        if int(html_prt[k]) > int(html_prj[i]):
                            #print("Participant ",j," selected for HTML in Project",i," under mentorship of ",k)
                            prt_slc["html"] = j
                            prt_list.remove(j)
                            break
            else:
                flag = 1

        if (python_prj[i] == "0"):
            pass
        else:
            for j in prt_list:
                if (int(python_prt[j]) >= int(python_prj[i])):
                    prt_slc["python"] = j
                    #print("Participant ",j," selected for Python in Project ",i)
                    prt_list.remove(j)
                    break
                elif (int(python_prt[j]) == int(python_prj[i]) - 1):
                    for k in prt_slc.values():
                        if int(python_prt[k]) > int(python_prj[i]):
                            #print("Participant ",j," selected for Python in Project ",i," under mentorship of ",k)
                            prt_slc["python"] = j
                            prt_list.remove(j)
                            break
            else:
                flag = 1

        if (dsa_prj[i] == "0"):
            pass
        else:
            for j in prt_list:
                if (int(dsa_prt[j]) >= int(dsa_prj[i])):
                    prt_slc["dsa"] = j
                    #print("Participant ",j," selected for DSA in Project ",i)
                    prt_list.remove(j)
                    break
                elif (int(dsa_prt[j]) == int(dsa_prj[i]) - 1):
                    for k in prt_slc.values():
                        if int(dsa_prt[k]) > int(dsa_prj[i]):
                            #print("Participant ",j," selected for DSA in Project ",i," under mentorship of ",k)
                            prt_slc["dsa"] = j
                            prt_list.remove(j)
                            break
            else:
                flag = 1

        if (java_prj[i] == "0"):
            pass
        else:
            for j in prt_list:
                if (int(java_prt[j]) >= int(java_prj[i])):
                    prt_slc["java"] = j
                    #print("Participant ",j," selected for Java in Project ",i)
                    prt_list.remove(j)
                    break
                elif (int(java_prt[j]) == int(java_prj[i]) - 1):
                    for k in prt_slc.values():
                        if int(java_prt[k]) > int(java_prj[i]):
                            #print("Participant ",j," selected for Java in Project ",i," under mentorship of ",k)
                            prt_slc["java"] = j
                            prt_list.remove(j)
                            break
            else:
                flag = 1

        if (sql_prj[i] == "0"):
            pass
        else:
            for j in prt_list:
                if (int(sql_prt[j]) >= int(sql_prj[i])):
                    prt_slc["sql"] = j
                    #print("Participant ",j," selected for SQL in Project ",i)
                    prt_list.remove(j)
                    break
                elif (int(sql_prt[j]) == int(sql_prj[i]) - 1):
                    for k in prt_slc.values():
                        if int(sql_prt[k]) > int(sql_prj[i]):
                            #print("Participant ",j," selected for SQL in Project ",i," under mentorship of ",k)
                            prt_slc["sql"] = j
                            prt_list.remove(j)
                            break
            else:
                flag = 1

        if (flag != 1):
            compl_prj = compl_prj+1
            print(compl_prj)
    
    prj_num.append(compl_prj)
            
    

print("Number of completed Projects = ",max(prj_num))

    


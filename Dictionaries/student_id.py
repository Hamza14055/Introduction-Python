student_id = {'id1':
    {'name':['sara'],'class':['V'],'subject_integration':['english','math','science']},
    'id2':
    {'name':['ali'],'class':['V'],'subject_integration':['english','math','science']},
    'id3':
    {'name':['zain'],'class':['V'],'subject_integration':['english','math','science']},
    'id4':
    {'name':['ali'],'class':['V'],'subject_integration':['english','math','science']}
}
result = {}
for key,value in student_id.items():
    if value not in result.values():
        result[key]=value
print(result)

     
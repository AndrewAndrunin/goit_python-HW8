from datetime import datetime, date

users = [
    {
        'name' : 'Bill',
        'birthday': '1983-6-1'  #2022-05-17
    },
        {
        'name' : 'Kim',
        'birthday': '1980-5-25', #2022-05-17
    },
        {
        'name' : 'Jan',
        'birthday': '1997-5-18', #2022-05-17
    },
        {
        'name' : 'Alexandr',
        'birthday': '1991-5-18', #2022-05-17
    },    
        {
        'name' : 'Sasha',
        'birthday': '1991-5-21', #2022-05-17
    },    
        {
        'name' : 'Andrew',
        'birthday': '1991-5-17', #2022-05-17
    },    
        {
        'name' : 'Jill',
        'birthday': '1990-5-20', #2022-05-17
    }
]

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wenesday", 
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}



def difference(m, d): #Функція рахує кількість днів різниці між сьогоднішнім днем і заданими даним (місяцем і датою)
    d_now = datetime.now()
    d_ord = d_now.toordinal()
    diff = date(int(d_now.year), int(m), int(d)).toordinal() - d_ord + 1
    return diff


def get_birhdays_per_week(users):
    list_data = []
    days_list = {
    "Monday": [],
    "Tuesday": [],
    "Wenesday": [], 
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}

    for i in users:
        name_d = []
        for k, v in i.items():
            diff = None
            if k == 'name':
                name_d.append(v)
            if k == 'birthday':
                y, m, d = v.split('-')
                diff = difference(m, d)
            if type(diff) is int and (diff < 0 or diff >=7):
                name_d.clear()
                continue
            if type(diff) is int and diff >= 0 and diff <7:
                y, m, d = v.split('-')
                d_now = datetime.now()
                date = datetime(day=int(d), month=int(m), year=d_now.year)
                weekday = date.weekday()
                if weekday == 5 or weekday == 6:
                    name_d.append(days_name.get(0))
                else:
                    name_d.append(days_name.get(weekday))
        if name_d != []:
            char = {name_d[1]: name_d[0]}
            list_data.append(char)
            for k1, v1 in days_list.items():
                for n in list_data:
                    for k2, v2 in n.items():
                        if k1 == k2 and v2 not in v1:
                            v1.append(v2)
    #print(list_data)
    #print(days_list)
    end_list = []
    for k4, v4 in days_list.items():
        if len(v4) > 1:
            list_names = ', '.join(v4)
            end_list.append(f'{k4}: {list_names}')
        elif len(v4) == 1:
            for i in v4:
                n_v = str(i)
            end_list.append(f'{k4}: {n_v}')
    for i in end_list:
        print(i)

get_birhdays_per_week(users)
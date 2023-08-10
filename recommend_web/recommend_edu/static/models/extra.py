import pickle

images_print = {'Program Management': 'img/program_managment.png',
                'Manufacturing & Supply Chain': 'img/Marketing_Communications.png',
                'Technical Solutions': 'img/technical_solution.png',
                'Developer Relations': 'img/line.png',
                'Hardware Engineering': 'img/line.png',
                'Partnerships': 'img/line.png',
                'Product & Customer Support': 'static/img/line.png',
                'Software Engineering': 'img/software.png',
                'Data Center & Network': 'img/line.png',
                'Business Strategy': 'img/strategy.png',
                'Technical Writing': 'img/line.png',
                'Technical Infrastructure': 'img/line.png',
                'IT & Data Management': 'img/line.png',
                'Marketing & Communications': 'img/Marketing_Communications.png',
                'Network Engineering': 'img/line.png',
                'Sales & Account Management': 'img/line.png',
                'Sales Operations': 'img/line.png',
                'Finance': 'img/line.png',
                'Legal & Government Relations': 'img/line.png',
                'Administrative': 'img/line.png',
                'User Experience & Design': 'img/users_design.png',
                'People Operations': 'img/line.png',
                'Real Estate & Workplace Services': 'img/line.png'}

with open('recommend_edu/static/models/model_preffered.pkl', 'rb') as f:
    model_preferred = pickle.load(f)

with open('recommend_edu/static/models/model_responsibilities.pkl', 'rb') as f:
    model_responsibilities = pickle.load(f)


def s_killer(feedback, subjects, work_in_team, logic_1, logic_2, tech_1, tech_2, responsible):
    skills = feedback + ',  ' + subjects
    if work_in_team:
        skills += ' communicative, management, '
    else:
        skills += ' home office, remote, '

    if logic_1 == 4 and logic_2 == 2:
        skills += ' logic, analytic, good english, '
    else:
        skills += ' sense of humour, business'

    if tech_1 == 3 and tech_2 == 2:
        skills += ' technical, data analysis, computer science, '
    else:
        skills += 'Design, creativity, people oriented, '

    if responsible in [2, 5]:
        skills += 'Strong Organization,  team lead, strategy, goal oriented '
    else:
        skills += 'People, psychology, marketing, '

    return skills

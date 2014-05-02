import json
import pandas as pd
import vincent

vincent.core.initialize_notebook()

user_1 = {'44': 100, '185': 97, '190': 96, '192': 90, '196': 26, '202': 87, '204':100, '220':100,'225':100, '226':100 }
user_2 = {'44': 98, '185': 98, '190': 96, '192': 90, '196': 35, '202': 88, '204':0, '220':0,'225':0, '226':0 }
user_3 = {'44': 96, '185': 100, '190': 100, '192': 0, '196': 0, '202': 88, '204':87.5, '220':0,'225':0, '226':100 }

user_data = [user_1, user_2, user_3]

user_index = ['User 1', 'User 2', 'User 3']
df_user = pd.DataFrame(user_data, index=user_index)

group = vincent.GroupedBar(df_user)
group.axis_titles(x='Score', y='Users')
group.legend(title='User Scores')
group.colors(brew='Set2')

group.to_json('vega.json')
group.display()
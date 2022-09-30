# Представьте, что вы работаете аналитиком данных в больнице. Пусть переменные diagnosis_1, diagnosis_2 и diagnosis_3
# хранят информацию о наличии у пациента различных хронических заболеваний ('yes' — да, 'no' — нет). С помощью
# операторов сравнения и логических операторов проверьте, что пациент страдает хотя бы одним из этих заболеваний?
# Результатом должно стать булево число - True или False. Занесите этот результат в переменную result
diagnosis_1 = 'yes'
diagnosis_2 = 'no'
diagnosis_3 = 'no'
result = 'yes' in [diagnosis_1, diagnosis_2, diagnosis_3]
print(result)

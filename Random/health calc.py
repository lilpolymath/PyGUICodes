def health_calc(age, apples_ate, cigs_smoked):
	answer = (100-age) + (apples_ate*3.5) - (cigs_smoked*2)
	print(answer)
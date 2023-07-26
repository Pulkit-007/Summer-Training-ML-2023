import joblib
joblib.load("mymarks.model")





h=input("Input your hours of study")



final_score=mind.predict([[int(h)]])


print(final_score)
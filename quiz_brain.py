
class QuizBrain:
	def __init__(self, list):
		self.question_number = 0
		self.list = list
		self.score=0
	
	def still_has_questions(self):
		return self.question_number <len(self.list)
	
	def next_question(self):
		user_input = input (f"Q.{self.question_number+1}: {self.list[self.question_number].text} (True/False):")
		self.question_number += 1
		self.check_answer(user_input,self.list[self.question_number-1].answer)
	
	def check_answer(self,user_input,answer):
		if user_input.lower() == answer.lower():
			print("You got it right !")
			self.score +=1
		else:
			print("That's wrong")
		print(f"The correct answer was {answer}")
		print(f"Your current score is : {self.score}/{self.question_number}")
		print("\n")
			
			
			



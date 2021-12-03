
# Checkpoint No.3 90% code
# Title: ENGINEERING TOPICS QUIZ GAME
# Albios, Hannie Mae
# Lingo, Isagani Jr.
# Costorio, Jeiboy


print ("Welcome to the Engineering Topics Quiz Game!")
print ("-----------------------------------------------------------------")
print ("There are 10 questions for every topic and no time limit.")


def play_again():
	playing = input("Do you want to play? (YES/NO)  ")
	playing = playing.upper()
	if playing == "YES":
		return True
	else:
		return False

def score():
	score = 0
	print ("\nQUIZ COMPLETED!")
	print("\n SCORE:"  +  str(score)  + "/10")
	print("\n PERCENT:" + str((score/4) * 100) )		
	print("--------------------------------------------------")
	
					
def new_game():
	score = 0
	print (f"\nPlease choose from the three categories.")
	topics = [ " A. Workshop Theory and Practice", "B.Physics for Engineers" , "C.Engineering Management, D. Create own Quiz"]
	print (f"\nEngineering Topics: {topics}") 
	A = "Workshop Theory and Practice"
	B = "Physics for Engineers"
	C = "Engineering Management"
	D = "Create own Quiz"
	
	choice = print(f"\nWhat topic do you want to answer? ")
	choice_a = input ("Enter the letter of your choice: ")
	choice_a = choice_a.upper()

# show Work shop and theory questionnaire
		
	if choice_a == "A":
		print(f"\nLet's start with Workshop Theory and Practice quiz!")
		
		Q_1 = print ("\n1. In welding, what do you call the yellow zone where fusion of melted metal and filler occurs?")
		answer = input("Answer: ")
		answer = answer.upper()
		if answer == "WELD MELT":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is WELD MELT.")
		
		Q_2 = print ("\n2. A marking material used to enhance the visibility of the layout being generated.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "BLUE DYE":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is BLUE DYE.")
		
		Q_3 = print ("\n3.(TRUE or FALSE) Proper measurement reading is very important in order to reduce the error or uncertainties of the measuring tool.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "TRUE":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is TRUE.")
	
		Q_4 =  print ("\n4.A process that involves the cutting of array of holes that are spaced closely with each other. This operation is used as vents and aeration of a certain closed space.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "PERFORATING OPERATION":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is  PERFORATING OPERTION.")
				
		Q_5 = print ("\n5. PPE is defined as all equipment which is intended to be worn or held to protect against risk to health and safety. What does PPE stands for?")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "PERSONAL PROTECTIVE EQUIPMENT":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is PERSONAL PROTECTIVE EQUIPMENT.")
		
		Q_6 = print ("\n6. TRUE or FALSE: Ergonomic hazard is not considered as a workplace hazard.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "FALSE":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is FALSE: Ergonomic hazard refers to workplace conditions that stress and strain the body.")
		
		
		Q_7 = print ("\n7. A joining process that utilizes adhesive chemicals such as epoxy based, silicon based, acrylic based, and cyanoarcylic adhesives in order to produce a permanent joint on sheet metals.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "ADHESIVE BONDING":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is ADHESIVE BONDING.")
		
		Q_8 = print ("\n8.A process that comprise of shearing and forming operation that creates an extruded hole of slot on the workpiece.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "PIERCING OPERATION":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is PIERCING OPERATION.")
		
		Q_9 = print ("\n9. A measuring tool also known as micrometer screw gauge, is more powerful than a Vernier since it can measure objects with accuracy up to thousandths of an inch or mm.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "MICROMETER CALIPER":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is MICROMETER CALIPER.")
		
		Q_10 = print ("\n10. A process that involves the application of force on a sheet metal enough to change its geometry.")
		answer = input("Answer:")
		if answer == "BINDING PROCESS":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is BINDING.")
																		
# show Engineering Physics questionnaire
	elif choice_a == "B":
		print(f"\nLet's start with Engineering Physics quiz!")
		
		Q_1 = print ("\n1. A basic law of electromagnetism predicting how a magnetic field will interact with an electric circuit to produce an electromotive force (EMF)?")
		answer = input("Answer: ")
		answer = answer.upper()
		if answer == "FARADAY'S LAW":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is FARADAY'S LAW.")
		
		Q_2 = print ("\n2. In a Simple Harmonic Motion, the maximum displacement from an equilibrium point is ______.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "AMPLITUDE":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is AMPLITUDE.")
		
		Q_3 = print ("\n3.TRUE or FALSE : Concurrent forces are forces acting on the same point .")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "TRUE":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is TRUE.")
	
		Q_4 =  print ("\n4.Potential Energy increases along with ________.")
		answer = input ("Answer:")
		answer = answer.upper()
		if answer == "HEIGHT":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is  HEIGHT")
				
		Q_5 = print ("\n5. This is the velocity at which a body will be able to leave the Earth's Gravitational pull.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "ESCAPE VELOCITY":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is ESCAPE VELOCITY.")
		
		Q_6 = print ("\n6. TRUE or FALSE: Viscous force is directly proportional to the Area and Velocity gradient.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "TRUE":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is TRUE.")
		
		
		Q_7 = print ("\n7. Heat is transferred where there is actual movement of the molecules transmitting Heat from one place to another.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "CONVECTION":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is CONVECTION:")
		
		Q_8 = print ("\n8.The force which acts towards the centre along the radius of the circular path on which the particle is moving with uniform velocity .")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "CENTRIPETAL FORCE":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is CENTRIPETAL FORCE.")
		
		Q_9 = print ("\n9. A quantity that involves both magnitude and direction and obeys the commutative law for addition,")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "VECTOR":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is VECTOR.")
		
		Q_10 = print ("\n10. A quantity that does not involve direction.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "SCALAR":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is SCALAR.")
			
	
	
		
#shows Engineering Management questionnare	
	elif choice_a == "C":
		print(f"\nLet's start with Engineering Management  quiz!")
		Q_1 = print ("1.A ______ provides a methodical way of achieving desired goals. ")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "PLAN":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is PLAN.")
		
		Q_2 = print ("2. Is the process of determining the major goals of the organization and the policies and strategies for obtaining and using resources to achieve those goals")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "STRATEGIC PLANNING":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is STRATEGIC PLANNING.")
		
		Q_3 = print ("3.TRUE or FALSE : The first task of the engineer manager is to provide a sense of direction to his firm, to his division, or to his unit.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "TRUE":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is TRUE.")
	
		Q_4 =  print ("4.Is the process of determining the contributions that subunits can make with allocated resources.")
		answer = input ("Answer:")
		answer = answer.upper()
		if answer == "INTERMEDIATE PLANNING":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is  INTERMEDIATE PLANNING")
				
		Q_5 = print ("5. The precise statement of results sought, quantified in time and magnitude, where possible.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "GOALS":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is GOALS.")
		
		Q_6 = print ("6.TRUE or FALSE: A standard may be defined as “a quantitative or qualitative measuring device designed to help monitor the performances of people, capital goods, or processes.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "TRUE":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is TRUE.")
		
		
		Q_7 = print ("7. A course of action aimed at ensuring that the organization will achieve its objectives.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "STRATEGY":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is STRATEGY.")
		
		Q_8 = print ("8.Plans intended to cover a period of less than one year. ")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "SHORT RANGE PLANS":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is SHORT RANGE PLANS.")
		
		Q_9 = print ("9.Is a short-term action taken by management to adjust negative internal or external influences.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "TACTIC":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is TACTIC.")
		
		Q_10 = print ("10. Plans covering a time span of more than one year.")
		answer = input("Answer:")
		answer = answer.upper()
		if answer == "LONG RANGE PLANS":
			print ("Correct!")
			score += 1
		else:
			print("Incorrect! The correct answer is LONG RANGE PLANS.")

	
#let user create his own quiz questionnaire		
	elif choice_a == "D":
		print(f"\nGreat! Let's create your own quiz.")
#consists the item's name, description, and it's count
		
		title = input("Enter Quiz Title: ")
		quiz = {"Question: Answer":1}
		
		
		for add_question, data in quiz.items():
		    print(f"\n{add_question}")  
		
		# loops the program 
		while True:
		    add_question = input("\nDo you want to add a question in the quiz? (Yes/No): ") 
		    # capitalizes the first letter of the input
		    add_question_a = add_question.title( ) 
		    
		    # executes the code below if user wants to add a tool
		    if add_question == "Yes":
		    
		        while not False: 
		            try:
		                #asks user to input number of tools
		                num = int(input("Enter the number of this tool to be placed in the quiz: "))  
		                #executes code below if i is not an integer
		                i = True
		                #ends loop
		                break  
		                
		            except ValueError:
		                #notifies user to input integers only
		                print("Error: Input value must be an integer.")  
		    
		  
		    
		       #asks user for tool's name 
		        question = input("Enter the question: ") 
		        #capitalizes  the first letter of the input
		        question_b = question.title( ) 
		        #asks user for tool's description
		        ans = input("Enter the answer: ")  
		        #capitalizes the first letter of the input
		        ans_c = ans.title( )
		        
		        #values of i should be an integer
		        
		         
		        #adds the tool's name, description and count on the inventory list
		        quiz[f"'{question_b}' : '{ans_c}'"] = f"{num}"  
		        # shows message stating that the inventory is updated
		        print(f"\nQuestion successfuly added.")
		  
		    #executes code below if user is done adding new tools 
		    elif add_question_a  == "No":  
		        #ends loop
		        break  
		      
		        
		    #executes the code below if user's answer is not in the choices  
		    else:  
		        print("Error: Enter 'Yes' or 'No' only.")
		        
		#displays updated inventory list      
		print("\n Let's start with",   title , "Quiz!")
		for add_question, data in quiz.items():
			quest = ({add_question})
		for key in quest:
			print ("-----------------------------------------------------")
			print (key)
		
		def check_answer():
			if answer == guess:
				answer = input("Answer:")
				answer = answer.upper()
				print ("Correct!")
				score += 1
			else:
				print("Incorrect!")	
							
			check_answer(question.get(key), guess)
		
		
									
												
# if user wants to continue				
new_game ()
score()
      
while play_again ():
	new_game()
	
print("GAME OVER!")
	
	
	
	
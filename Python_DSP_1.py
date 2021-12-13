import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
object1 = 0
object2 = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The path is broken into sections, starting with "intro". Everyone starts at intro for
def intro():
  print ("So, you want to run a research project on a social science topic and want to flex your data skills. So far, you have:")
  time.sleep(1)
  print ("""  A. A research question but no data.
  B. Some data to analyse but no idea what to do with it.
  C. Neither of these, just some vague ideas. """)
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_have_question_no_data()
  elif choice in answer_B:
    option_have_data_no_question()
  elif choice in answer_C:
    print ("\nHere is a guide on how to turn vague ideas into well-formed research questions. Links to relevant info. \n\n End of this path, but more paths exist!")
    intro()
  else:
    print (required)
    intro()

def option_have_question_no_data(): 
  print ("\n So, you know what research you want to do but don't have the data to do it. Let's dig into that a bit. You have:")
  time.sleep(1)
  print ("""  A. Have a solid research question, but need to know more about data acquisition.
  B. Have a good start on a research question but maybe it would be a good idea to compare it to a list of what makes for a good research question before diving into data acquisition.""")
  choice = input(">>> ")
  if choice in answer_A:
    option_general_data_acquisition()
  elif choice in answer_B:
    print ("\nHere is a guide on how to turn vague ideas into well-formed research questions. Links to relevant info. \n\n End of this path, but more paths exist!")
    intro()
  else:
    print (required)
    option_have_question_no_data()

def option_have_data_no_question(): 
  print ("\nSo, you have some data that may be really cool, but you don't really know how to move forward. You want:")
  time.sleep(1)
  print ("""  A. To learn how to formulate a good research question?
  B. To identify appropriate methods to use with this data.
  C. To learn about different kinds of data in case I want more.""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nHere is a guide on how to turn vague ideas into well-formed research questions. Links to relevant info. \n\n End of this path, but more paths exist!")
    intro()
  elif choice in answer_B:
    option_general_research_methods()
  elif choice in answer_C:
    option_general_data_acquisition()
  else:
    print (required)
    option_have_data_no_question()

def option_have_nothing(): 
  print ("\n This is a tricky start, but maybe it helps to explore some basics. Do you want to start with:")
  time.sleep(1)
  print ("""  A. Learning about how to formulate good research questions?
  B. Learning about what kinds of data you might be able to acquire?
  C. Learning about reserach methods you might want to use?""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nHere is a guide on how to turn vague ideas into well-formed research questions. Links to relevant info. \n\n End of this path, but more paths exist!")
    intro()
  elif choice in answer_B:
    option_general_data_acquisition()
  elif choice in answer_C:
    option_general_research_methods()
  else:
    print (required)
    option_have_nothing()

def option_general_data_acquisition(): 
  print ("\nRight. You know you need data, but you don't know what kind or kinds of data you will need. Are you:")
  time.sleep(1)
  print ("""  A. Interested in primary data collection.
  B. More interested in secondary data, data reuse, and/or data published by official sources?
  C. Something far out, like social media data, data from distributed censor networks, or the like. """)
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nDefinition of primary data, links to relevant info. \n\n You can move through this path again if you like!")
    intro()
  elif choice in answer_B:
    option_secondary_data_acquisition()
  elif choice in answer_C:
    print ("\nDefinition of CSS data, links to relevant info. \n\n If you want to know more, you can go throug the path again.")
    intro()
  else:
    print (required)
    option_general_data_acquisition()


def option_secondary_data_acquisition(): 
  print ("\nSo, you want to use secondary data what kind of data you want to acquire. Are you looking to get:")
  time.sleep(1)
  print ("""  A. Longitudinal data
  B. Microdata
  C. Other?""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nDefinition of longitudinal data, links to relevant info. \n\n End of this path! Consider starting again from the beginning.")
    intro()
  elif choice in answer_B:
    print ("\nDefinition of microdata data, links to relevant info. \n\n End of this path! Maybe have another go.")
  elif choice in answer_C:
    print ("\nDefinition of third secondary data choice. \n\n You have reached the end of this path, but you can always start over from scratch.")
    print (required)
    option_specific_data_acquisition()


def option_general_research_methods(): 
  print ("\nThere are so many options for research methods! Let's start with some broad categories. Do you want to learn about:")
  time.sleep(1)
  print ("""  A. Methods suitable for longitudinal data
  B. Methods suitable for microdata
  C. Computational social science methods""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nSome info on some of the methods that are most commonly used to analyse longitudinal data, links to relevant info. \n\n End of this path! Consider starting again from the beginning.")
    intro()
  elif choice in answer_B:
    print ("\nSome info on some of the methods that are most commonly used to analyse microdata data, links to relevant info. \n\n End of this path! Maybe have another go.")
    intro()
  elif choice in answer_C:
    print ("\nSome info on some popular CSS methods and links to revelant github repos, etc.. \n\n You have reached the end of this path, but you can always start over from scratch.")
    intro()
  else:
    print (required)
    option_learn_to_form_good_research_questions()


intro()







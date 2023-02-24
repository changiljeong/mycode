#!/usr/bin/env python3

# Create an application that give MBTI results per user-selected input.
import os


def main():

  mbti_type = {
    "INTJ": "The Architect",
    "INTP": "The Logician",
    "ENTJ": "The Commander",
    "ENTP": "The Debater",
    "INFJ": "The Advocate",
    "INFP": "The Mediator",
    "ENFJ": "The Protagonist",
    "ENFP": "The Campaigner",
    "ISTJ": "The Logistician",
    "ISFJ": "The Defender",
    "ESTJ": "The Executive",
    "ESFJ": "The Consul",
    "ISTP": "The Virtuoso",
    "ISFP": "The Adventurer",
    "ESTP": "The Entrepreneur",
    "ESFP": "The Entertainer",
  }

  mbti_description = {
    "INTJ":
    "imaginative and strategic thinkers, with a plan for everything.",
    "INTP":
    "innovative inventors with an uniquechable thirst for knowledge.",
    "ENTJ":
    "bold, imaginative and strong-willed leaders, always finding a way-ormaking one.",
    "ENTP":
    "smart and curious thinkers who cannot resist an intellectual challenge.",
    "INFJ":
    "quite and mystical, yet very inspiring and tireless idealists.",
    "INFP":
    "poetic, kind and altruistic people, always eager to help a good cause.",
    "ENFJ":
    "charismatic and inspring leaders, able to mesmerize their listeners.",
    "ENFP":
    "enthusiastic, creative and sociable free spirits, who can always find a reason to smile.",
    "ISTJ":
    "practical and fact-minded individuals, whose reliability cannot be doubted.",
    "ISFJ":
    "very dedicated and warm protectors, always ready to defend their loved ones",
    "ESTJ":
    "excellent administrators, unsurpassed at managing things-or peole.",
    "ESFJ":
    "extraordinarily caring, social and popular people, always eager to help.",
    "ISTP":
    "bold and practical experimenters, masters of all kinds of tools.",
    "ISFP":
    "flexible and charming artists, always ready to explore and experience something new.",
    "ESTP":
    "smart, energetic and very perceptive people, who truly enjoy living on the edge.",
    "ESFP":
    "spontaneous, energetic and enthusiastic entertainers - life is never boring aroudn them.",
  }

  # Extraversion vs. Introversion | Sensing vs. Intuition | Thinking vs. Feeling | Judging vs. Perceiving

  while True:
    try:

      # Initialize dictionary to store data input from the user & apply logical conditions.
      answers = {"name": "", "EI": "", "SN": "", "TF": "", "JP": ""}

      # Capture the name from user-input and store to dict immediately.
      answers["name"] = input(
        ":::: **** Welcome to CJ's Myers-Briggs Type Indicator**** ::::\n\nI will be asking you few questions and please answer numeric value of '1' for YES or '2' for NO in most of questions.\n\nBefore we get to the business, who am I speaking with today? :)\n >>> "
      )
      os.system('clear')

      answer_ei = int(
        input(
          f"\n**********************************************************************\nAlright, {answers.get('name')}! Here is the first question for you. Which option describe you the most? \n\n1 - I am described as taltative, outgoing. Tend to work out ideas with others, think out loud and enjoy being the center of attention.\n2 - I am described as reserved, private and prefer observing than be the center of attention.\n >>> "
        ))

      os.system('clear')
      if answer_ei == 1:
        answers["EI"] = "E"
      elif answer_ei == 2:
        answers["EI"] = "I"
      else:
        print(
          "You can only select the value of 1 or 2. Let's start again from the top! \n=========================================== \n"
        )
        main()

      answer_sn = int(
        input(
          "\n**********************************************************************\nAwesome! Next question is about how do you prefer to take in information. Select the number describe you the most. \n\n1 - I focus on the reality of how things are and pay attention to concret facts and details. I like to describe things in a specific, literal way.\n2 - I imagine the possibilities of how things could be and notice the big picture, see how everything connects. I like to describe things in a figurative, poetic way. \n >>> "
        ))
      os.system('clear')
      if answer_sn == 1:
        answers["SN"] = "S"
      elif answer_sn == 2:
        answers["SN"] = "N"
      else:
        print(
          "You can only select the value of 1 or 2. Let's start again from the top! \n=========================================== \n"
        )
        main()

      answer_tf = int(
        input(
          "\n**********************************************************************\nYou are doing fantastic! Next question is about how do you prefer to make decisions. \n\n1 - I make decision in an impersonal way, using logical reasoning. I value justice, fairness, and could be described as level-headed. \n2 - I value harmony, forgiveness, and like to please others and point out the best in people. I cloud be described as warm, empathetic. \n >>> "
        ))
      os.system('clear')
      if answer_tf == 1:
        answers["TF"] = "T"
      elif answer_tf == 2:
        answers["TF"] = "F"
      else:
        print(
          "You can only select the value of 1 or 2. Let's start again from the top! \n=========================================== \n"
        )
        main()

      answer_jp = int(
        input(
          "\n**********************************************************************\nLast question! The final question is about how do you prefer to live your outer life. \n\n1 - I prefer to have matters settled. I think rules and deadlines should be respected and like making plans. \n2 - I prefer to leave options open and see rules & deadlines as flexible. I am spontaneous & enjoy suprises. \n >>> "
        ))
      os.system('clear')
      if answer_jp == 1:
        answers["JP"] = "J"
      elif answer_jp == 2:
        answers["JP"] = "P"
      else:
        print(
          "You can only select the value of 1 or 2. Let's start again from the top! \n=========================================== \n"
        )
        main()

    # Concat dict values to create MBTI
      if answer_ei and answer_sn and answer_tf and answer_jp:
        result = answers.get('EI') + answers.get('SN') + answers.get(
          'TF') + answers.get('JP')
        final_type = mbti_type[result]
        final_description = mbti_description[result]

        print(
          f"\n\n**********************************************************************\nFantastic, {answers.get('name')}! So it appears as your MBTI is {result} which the type is known as: {final_type}. You are {final_description} Does it sound about right?\n\n and have a wonderful day!\n**********************************************************************"
        )

    # Restarting Inquiry
      restart = input(
        "Thank you so much for your participation. Would you like to restart this again? (Y/N)"
      )
      if restart == "yes" or restart == "y":
        main()
      if restart == "n" or restart == "no":
        print("Script terminating. Goodbye.")
        break
        
    # Exception to catch ValueError of non-integer input
    except ValueError:
      os.system('clear')
      print("You can only select the value of 1 or 2. Let's start again from the top! \n=========================================== \n")
      main()


if __name__ == "__main__":
  main()


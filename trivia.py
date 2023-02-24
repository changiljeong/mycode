#!/usr/bin/env python3
import html
trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }



print(html.unescape(trivia["question"]))
print("Incorrect answers ==>")
for answer in trivia["incorrect_answers"]:
    print(html.unescapte(answer))

print("Correct answers ==> ")
print(html.unescapte(trivia["correct_answer"])

# 📝 Project Planning Worksheet

**Name:** james 
**Date:** 5/6/2026- 5/7/2026
**Project Title:** grade calculotor final

---

## Step 1 — What will your program do?

*Write 2–3 sentences describing your project. What happens when the user runs it? What will they see or do?*

> my program will allow a user to calculate their grade and if it will havew a heavy impact. when the usere opens the code they will be asked how amny questons, how many they got right after the calculaton it will ask what kind of assinment and then say its impact over all

---

## Step 2 — What will you ask the user?

*List every `input()` question you plan to use.*

1. imput(int(print"how many questions are there))
2. imput(int(print"how many questions did you get right))
3. imput(str(print"is this a quiz,homework or a test))

---

## Step 3 — What variables do you need?

*List the variable names you plan to use and what each one stores.*

| Variable Name | What It Stores | Data Type |
|---------------|---------------|-----------|
| numerQestions|how many queston there are | - INT|
| questionsCorrect| how many are corect | | INT
| assimentType| if its a test,quiz or home work | string| 
|grade | what you gor post calulaton| int|

---

## Step 4 — What decisions will your program make?

*Describe each `if/elif/else` check your program will use.*

- If grade >= 90 , then print "you got an A great job"
- Elif grade < 90 or >= 80, then print "you got a B your doing great"
- elif grade < 80 or >= 70 then print "you got a C keep trying harder every day"
- elif grade < 70 or >=60, then print "you got a D dont give up "
- Else print "you failed"

- if assimentType == "test", then print " this will have a major impact"
- Elif assimentType =="quiz", then print "thsi will have a medium impact"
- else print "this will have a minor impact"

*(Add more rows if needed.)*

---

## Step 5 — What will the output look like?

*Write out what a sample run of your program might look like. Pretend you are the user.*

```
Program output: here how many questions are there,how many questions did yoy get right,what kind of assinment is this
User types: 10,8, test
Program responds: you got a B your doinng great 
this will have a major impact
```

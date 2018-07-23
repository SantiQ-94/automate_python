#!/usr/bin/env python3
#random quiz generator, idea took from the book 
#'Automate the boring stuff with python', chapter 8

import random

capitales = {'Beni': 'Trinidad', 'Chuquisaca': 'Sucre', 
	'Cochabamba': 'Cochabamba', 'La Paz': 'La Paz', 'Oruro': 'Oruro',
	'Pando': 'Cobija', 'Potosi': 'Potosi', 'Santa Cruz': 'Santa Cruz',
	'Tarija': 'Tarija'}

for quizN in range(35):
	quizFile = open('capitalsquiz%s.txt' % (quizN + 1), 'w')
	answerKeyFile = open('capitalsquiz_answer%s' % (quizN + 1), 'w')

	#write the header of the quiz
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'Departaments Capitals Quiz (Form %s)' % (quizN + 1))
	quizFile.write('\n\n')

	departamentos = list(capitales.keys())
	random.shuffle(departamentos)

	for questionNum in range(9):
		correctAnswer = capitales[departamentos[questionNum]]
		wrongAnswers = list(capitales.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, departamentos[questionNum]))
		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')

		answerKeyFile.write('%s. %s\n' % (questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()

	




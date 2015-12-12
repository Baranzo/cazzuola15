from django.shortcuts import render

def index(request):
	
	content = {
		"titolo_pagina": "Cazzuola prova",
		"titolo_testo": "Titolo di prova",
		"testo": "testo di prova"
	}
	
	return render(request, 'base_template.html', content)

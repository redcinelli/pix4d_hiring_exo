.DEFAULT_GOAL := debug

debug:
	uvicorn main:app --reload


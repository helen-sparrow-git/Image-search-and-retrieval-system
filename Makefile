start server:
	uvicorn app.main:app --reload

update git:
	git add .
	git commit -m "FastAPI and Pydantic done"
	git push origin main
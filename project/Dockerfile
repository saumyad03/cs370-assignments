FROM python:3.9
WORKDIR /app
COPY requirements.txt .
COPY Milestone1.ipynb .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

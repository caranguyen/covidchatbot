1. Run Django:
<pre>python .\manage.py runserver</pre>


2. Run rasa:
<pre>rasa train</pre>
<pre>rasa run -m models --enable-api --cors "*" --debug</pre>
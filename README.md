# covidchatbot

Python requirements setup: python 3.0+, pip

This program is run and tested on Windows 10 with Anaconda Compiler. 

Optional to wrap the project in virtualenv: 
<pre><code>C:\> python3 -m venv ./venv
C:\> .\venv\Scripts\activate
</code></pre>

To install rasa open source:
<pre><code>pip3 install rasa</code></pre>

To run the current model:
<pre><code>rasa shell</code></pre>

The shell will prompt user input. Currently, here are the topic chat bot can answer
- success rate of 3 main vaccine providers
- number of and time between dose of 3 main vaccine providers
- covid demographic
- who should not take vaccine
- after care instruction


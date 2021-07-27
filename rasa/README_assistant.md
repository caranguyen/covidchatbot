# covidchatbot

Python requirements setup: python 3.3+, pip

This program is run and tested on Windows 10. 

Optional to wrap the project in some virtual environment such as virtualenv or anaconda: 
<pre><code>C:\> python3 -m venv ./venv
C:\> .\venv\Scripts\activate
</code></pre>

For Mac: 
<pre><code>python3 -m venv ./venv
source ./venv/bin/activate
</code></pre>

On Anaconda (on Windows):
<pre><code>conda create --name py37 python=3.7
conda activate py37
</code></pre>

To install Rasa:
<pre><code>pip3 install rasa</code></pre>

to see where are Rasa directory and files, run:
<pre><code>rasa init</code></pre>

Then, clone files in this repo in the same directory as venv folder. If you are in the correct Rasa directory, files in this repo will replace files created by rasa init.

Next, train the model:
<pre><code>rasa train</code></pre>

To run the current model on command prompt:
<pre><code>rasa shell</code></pre>

The shell will prompt user input, then responses accordingly to the user input

To run Rasa for website widget:
<pre><code>rasa run -m models --enable-api --cors "*" </code></pre>

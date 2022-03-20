<h1>Sbancatore Bot</h1>
<p>Bot di telegram privato botta e risposta, spiegazione sul funzionamento, come personalizzarlo e la personalizzazione standard per i privati interessati.</p>

  * [Introduzione](#introduzione)
  * [Funzionamento](#funzionamento)
  * [trigger & answers (tea)](#tea)
<br>

## Introduzione
<p>Prima di tutto, questo bot si basa sulla libreria 
<a href= "https://github.com/eternnoir/pyTelegramBotAPI" target="_blank">pyTelegramBotAPI</a>, un implementazione della <a href="https://core.telegram.org/api" target="_blank"> API di telegram</a> per python, specificatamente per i <a href="https://core.telegram.org/bots/api"target="_blank">bot</a>.</p>

<p>Tutte le informazioni sono di conseguenza prese da li, ma essendo che questo bot usa solo una piccola parte di tutta la documentazione, riporteró di seguito cosa fa e come, piú i collegamenti alla documentazione originale.</p>
<p>Il bot semplicemente legge ogni messaggio di una chat e risponde quando certe parole, piú due semplici comandi per le informazioni (/start o /help; /commands) che molto probabilemente ti hanno portato qui.</p>
<p>Nel paragrafo funzionamento spiegheró come funziona il bot e come tu puoi personalizzarlo con i tuoi trigger e le tue risposte a suddetti trigger.</p>
<p>Direi di iniziare.</p>

## Funzionamento
### Libreria, import e apikey
<p>Prima di tutto, bisogna installare la libreria <a href="https://github.com/eternnoir/pyTelegramBotAPI#getting-started"target="_blank">pyTelegramBotAPI</a> (cliccare per le istruzioni, son quelle standard).</p> 
<p>Fatto ció, importa la classe telebot e crea un instanza di essa (bot):</p>

```python
import os
import telebot
import random
import answers

API_KEY = os.environ['apikey']
bot = telebot.TeleBot("apikey")
text = ""
```

Dó per scontato che sei giá in possesso della apikey, se cosi non fosse crea un bot con [botfather](https://core.telegram.org/bots#3-how-do-i-create-a-bot) e ottienila.

La variabile text ci servirá dopo, forse nel tuo caso non servirá proprio.

Parleremo piú avanti di random e answers.

### Environment variable
Per far funzionare:
```python
API_KEY = os.environ['apikey']
```
Devi creare un Environment variable, la cui creazione cambia in base all'ambiente di sviluppo, di conseguenza non so dare istruzioni precise.

Nel mio specifico caso, avendo usato [Replit](replit.com), ho sfruttato la sezione Secrets. 

L'utilizzo di questa speciale variabile é molto importante nel caso vuoi condividere il tuo codice su piattaforme come GitHub, dato che permette di non mostrare l'apikey, che dá completo accesso al bot. 

In caso tu non progetti di condividere in nessun modo il codice, suppongo puoi usare una variabile normale, ma non penso sia una buona idea.

### Funzione
Fatti tutti i preparativi, possiamo finalmente impegnarci nella funzione principale, quella che si accorgerá dei trigger e scriverá le risposte.


Il template standard é questo:
```python
@bot.message_handler(regexp='pizza')
def funzione1(message):
  bot.send_message(message.chat.id, random.choice(answers.pizze))
```
Ok, svisceriamo questo codice. 

La prima stringa,
```python
@bot.message_handler(regexp='pizza')
```
é il gestore dei messaggi. Con esso il bot analizza i messaggi in arrivo, in questo si triggera con tutti i messaggi con la parola pizza all'interno.

Quando tale mesaggio arriva, il programma esegue la funzione funzione1, che prende il messaggio trigger.

Tale funzione ha il semplice compito di rispondere con una frase, e lo fa con questa linea di codice:

```python
  bot.send_message(message.chat.id, random.choice(answers.pizze))
```

bot.send_message é abbastanza auto esplicativo, é la funzione dell'istanza bot per mandare un messaggio.

Tra le parentesi invece, vengono inseriti due parametri. 

Il primo,

```python
  message.chat.id
```

dice al bot di mandare il messaggio nella stessa chat dove é stato inviato il messaggio trigger, é ovviamente importante.

#### Random
Il secondo parametro invece,

```python
random.choice(answers.pizze)
```

dice il testo da mandare  via messaggio. In questo caso, si usa 
```python
random.choice 
```

per permettere piú risposte allo stesso trigger, al fine di rendere il bot meno monotono.

Si riconduce a questa scelta, non necessaria, l'inserimento a inizio codice di
```python
import random
```

Tra le parentesi di random.choice c'é invece l'array da cui le risposte vanno, casualmente, prese.
```python
answers.pizze
```
pizze é il nome dell'array, mentre answers é il file dove vengono salvati gli array per tutti i trigger.

Creare un altro file non é necessario, ma rende piú pulito il codice. 

Si riconduce a questa scelta la linea di codice iniziale
```python
import answers
```
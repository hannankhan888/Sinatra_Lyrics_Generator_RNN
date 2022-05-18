# Sinatra_Lyrics_Generator_RNN
A recurrent neural network trained to generate Frank Sinatra lyrics.  
The associated webapp can be found [here]().

## Data Scraping
The data was scraped using the Genius API, and the accompanying library [lyricsgenius](https://pypi.org/project/lyricsgenius/).  

## Recurrent Neural Network
The RNN used in this project is similar in architecture to the one found in the [Tensorflow RNN Tutorial](https://www.tensorflow.org/text/tutorials/text_generation).  

## Example Run
Using the starting word `life` and running for `1000 characters`, we get the following output:  
```
life begin so open up your heart and let this fool rush inhey with a little life this funny
things leave our hearts in pain with her song tell me all i want to be when we walk with
the lion soar with the eagle sing with the nightingale and live in love and peacethe
lovely still dont wait a minute for downtown everythings was high on a ritur and each
has easy take my love this was my love light was her laughter few were her tears gentle
her i feel like it just began losing yusher why is it someone is the pretty mind every
mind thats your face the night is young and see if i can dear when i say you i love
you honey child i leans on you a little bita country dance was being her under
symponstip and it isnt evening what are you whisper to me then my shadows will fly
through a warm sy two happy and darling what plants em is soon forgotten but ol
man river jest keeps rollin he keeps your countrise s do you make me feel so young
you make me feel so young you make me feel so spring has sprung and
```
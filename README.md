# LLMStock

Lightweight GPT 3.5 Analysis on a stock based on Medium article from Franck Stéphane Ndzomga. Support his articles and AI/ML work at https://medium.com/@fsndzomga. 

Made a few changes to the original code which I may decide to continuously update. As of 6/2023, this is a very early version, so expect hiccups. Like an old car, it will drive, but treat it gently. I thus, made analogous file names off major car parts. 

## Made changes to
-Major prompt changes in markdown format
-Couple metrics, matplotlib and data input changes
-Context length, gpt-3.5-16k


**6/2023-** If you clone locally, you will likely run into environment, or API key errors even if you load_dotenv and create a .env file. Export your API keys to your current shell environment: 

## 1
Clone the repo. 
I will eventually add a requirements.txt file. You need the standard apps of matplotlib, pandas, yahoo finance, openai, streamlit. 

## 2 

```
<export SERP_API_KEY=your_api_key_here 
```

```
export OPENAI_API_KEY=your_api_key_here
```


Check to see if in current shell by 
```
echo $SERP_API_KEY 
```

Like I said, I will get it correct, but just got it running first. Was having issues and got impatient. I will likely be changing it to Bing API Search because it allows up to 1000 searches/month vs. serp api. 

## 3 

Once you've cloned the repos run the following command to get it running: 
``` 
streamlit run body.py
 ```



### Quirks I found 

I'm not a pro yet at streamlit, css, or front end. 
1. If you click the space bar after entering the company name, you will get a data_object load error. Not sure why yet, but you can enter any public company name or ticker and it should work if on yahoo finance. i.e. entering Alcon or ALC. Both will recognize.
2. I haven't added really any animations as got a few errors and like I said, wanted it to work first.
3. I've seen it have different fonts such as italics randomly within a paragraph before, but should be fixed. Let me know if you see such.
4. It will say "Thinking" even after it is done loading. 



## Not financial advice or recommendations
Note of course, if you made it this far, by no means is this repository or its outputs financial advice by me or the code. You likely know that LLMs can hallucinate especially if you make adverse or poor running changes to the prompt to make it more likely to do such. You should check the metrics, data, and information it gives you. This is only an introductory tool/foundation to making analysis easy. 

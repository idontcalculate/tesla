
import os 
os.environ["OPENAI_API_KEY"] = ""

from embedchain import App

#Please use the chromadb version 0.3.29
import chromadb
import sqlite3

bench_bot = App()

bench_bot.add('web_page', 'https://mlcommons.org/en/training-normal-30/')
bench_bot.add('web_page', 'https://mlcommons.org/en/training-hpc-20/')
bench_bot.add('web_page', 'https://mlcommons.org/en/inference-datacenter-30/')
bench_bot.add('web_page', 'https://mlcommons.org/en/inference-tiny-11/')
bench_bot.add('web_page', 'https://mlcommons.org/en/groups/datasets/')



#sitemap
bench_bot.add('https://mlcommons.org/en/groups/research-storage/', data_type='web_page')

#langchain under the hood will download the video, perform audio-to-text, 
# take the transcript and load it with yt_loader ;)
bench_bot.add('youtube_video', 'https://www.youtube.com/watch?v=uMNtTBRCHXA') #ml commons link
bench_bot.add('youtube_video', 'https://www.youtube.com/watch?v=eyK-9UehYPo')
bench_bot.add('youtube_video', 'https://www.youtube.com/watch?v=woGaG3ZcTbU')
bench_bot.add('youtube_video', 'https://www.youtube.com/watch?v=woGaG3ZcTbU')
bench_bot.add('youtube_video', 'https://www.youtube.com/watch?v=txtvMhzEDu8')

#notion page data
#bench_bot.add('https://signalism.notion.site/MLCommons-An-In-Depth-Whitepaper-on-Benchmarking-Machine-Learning-Performance-d21aabe85304439fb5ae4ca7ac3826f7?pvs=4', 'notion')

#pdf data arxiv on bench
bench_bot.add('https://arxiv.org/pdf/2207.10062.pdf', data_type='pdf_file')

answer = bench_bot.query('what is ml commons?')
print(answer)
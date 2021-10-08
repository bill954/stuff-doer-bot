FROM python:3.9-buster
WORKDIR /src/discord-bot

# Install ffmpeg
RUN apt-get update -y && apt-get install ffmpeg -y
RUN apt-get clean
# Instalar dependencias py
RUN pip install -U "discord.py[voice]"
RUN pip install -U youtube_dl
RUN pip install -U nest_asyncio

COPY ./code/music_bot .

CMD [ "python3", "./music_player.py" ]

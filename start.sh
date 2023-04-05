if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/GouthamKL16/EvaMaria.git /EvaMaria
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /EvaMaria
fi
cd /EvaMaria
pip3 install -U -r requirements.txt
echo "𝙆𝙪𝙩𝙩𝙪 𝘽𝙤𝙩 𝙞𝙨 𝙎𝙏𝘼𝙍𝙏𝙄𝙉𝙂.........𝙉𝙊𝙒!!!!!"
python3 bot.py

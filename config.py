import os

api_id = int(os.environ.get("API_ID", "29486311"))
api_hash = os.environ.get("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.environ.get("BOT_TOKEN", "6596425760:AAEie9x9r5F5VcOk9-k4G9JMIo3YLbpjBP0")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://reonly:reon@cluster0.du3qvty.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "reon")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001884106616"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001973439933"))
channel_3 = int(os.environ.get("CHANNEL_3", "-1001884106616"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001941178911"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "957521020"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "2"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "20"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#Girl #Boy #Ask #Story").replace(" ", "|").lower()
# ============================================================#

pesan_join = os.environ.get("PESAN_JOIN", "{mention} silahkan join melalui tombol dibawah untuk mengirim pesan")
start_msg = os.environ.get("START_MSG", """"
CPV Autopost bot, adalah bot autopost yang akan otomatis mengirimkan pesan yang ada kirimkan di bot ini, dan akan di post di channel @ChannelCPF. untuk mengirim pesan silahkan gunakan hastag:

#Boy / #Girl untuk mencari pasangan,teman , partner dll
#Ask untuk bertanya
#Story untuk berbagi cerita

""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
Hai {mention} pesan mu gagal terkirim 🙅, silahkan gunakan hastag:

#Boy / #Girl untuk mencari pasangan,teman , partner dll
#Ask untuk bertanya
#Story untuk berbagi cerita
""")

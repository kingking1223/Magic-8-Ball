import discord
from discord.ext import commands
import random
import keep_alive

en = ["It is certain","It is decidedly so","Without a doubt","Yes, definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
zh = ["這是必然","肯定是的","不用懷疑","毫無疑問","你能依靠它","如我所見，是的","很有可能","外表很好","是的","種種跡象指出「是的」","回覆攏統，再試試","待會再問",
"最好現在不告訴你","現在無法預測","專心再問一遍","想的美","我的回覆是「不」","我的來源說「不」","外表不太好","很可疑"]
fr = ["Il est certain que","Sans aucun doutes","Vous pouvez compter sur elle","Oui certainement","Il en est décidément ainsi","À mon titre, oui","Très probablement","Oui","Perspectives bonnes","Les signes indiquent oui","Réponse brumeux essayer à nouveau","Mieux vaut ne pas te le dire maintenant","Demandez à nouveau plus tard","Impossible de prédire maintenant","Concentrez-vous et demandez à nouveau","Ne comptez pas là-dessus","Perspectives pas si bonnes","Mes sources disent non","Très douteux","Ma réponse n’est pas"]
es = ["Es inevitable", "Es seguro", "No lo dudes", "absolutamente", "sin duda", "puedes confiar en él", "sí", "probablemente", "buen aspecto", "todas las indicaciones son \"sí\"", "de vuelta a ella, inténtelo de nuevo", "Preguntaré más tarde", "Es mejor no decírtelo ahora", "Impredecible ahora", "Concéntrese en preguntar de nuevo", "Piensa en la belleza", "Mi respuesta es \"no\"", "Mi fuente dice \"no\"", "no es muy bueno", "Es sospechoso"]
hi = ["यह अपरिहार्य है", "यह सुनिश्चित करने के लिए है", "इस पर संदेह न करें", "इसमें कोई शक नहीं।", "आप इस पर भरोसा कर सकते हैं", "जैसा कि मैं देख सकता हूं, हां", "एक अच्छा मौका है", "यह अच्छा लग रहा है", "हाँ।", "संकेत है कि \"हां.\"", "सामान्य को जवाब दें, फिर से प्रयास करें", "मैं आपसे बाद में वापस पूछूंगा", "बेहतर होगा कि अब आपको न बताएं", "अभी भविष्यवाणी करना असंभव है", "फिर से पूछें att ध्यान केंद्रित", "सौंदर्य के बारे में सोचो", "मेरा उत्तर नहीं है।", "मेरे सूत्र ने कहा कि नहीं ।", "यह बहुत अच्छा नहीं लगता है", "यह संदिग्ध है"]
ar = ["هذا أمر لا مفر منه", "انها آمنة", "لا تشك في ذلك", "يمكنك الاعتماد عليه", "كما أرى، نعم", "هناك فرصة جيدة", "يبدو جيدا", "هذا صحيح.", "هناك علامات على أن \"نعم\".", "الرد على العام، حاول مرة أخرى", "سأسألك لاحقاً", "من الأفضل ألا أخبرك الآن", "من المستحيل التنبؤ الآن", "ركز على السؤال مرة أخرى", "فكر في الجمال", "ردي هو لا.", "مصدري قال لا", "لا يبدو جيداً جداً", "إنه أمر مريب"]
ru = ["Это неизбежно", "определенно", "Не сомневайтесь в этом", "без сомнения", "Вы можете положиться на него", "Как я вижу, да", "Очень вероятно", "хороший вид", "Да", "Есть признаки того, что \"да\"", "Ответьте генералу, повторите попытку", "Я попрошу тебя вернуться позже", "Лучше не говорить тебе сейчас", "Сейчас невозможно предсказать", "Спросите еще раз att концентрат", "Подумайте о красоте", "Мой ответ - нет.", "Мой источник сказал нет.", "Это выглядит не очень хорошо", "Это подозрительно."]
bn = ["এটা অবশ্যম্ভাবী।", "অবশ্যই", "সন্দেহ করো না", "কোনো সন্দেহ নেই।", "আপনি এটার উপর নির্ভর করতে পারেন", "আমি দেখতে পাচ্ছি, হ্যাঁ", "একটা ভালো সুযোগ আছে", "এটা ভালো দেখাচ্ছে", "এটা ঠিক।", "কিছু লক্ষণ আছে যে \"হ্যাঁ\"।", "জেনারেলকে উত্তর দিন, আবার চেষ্টা করুন", "আমি তোমাকে পরে জিজ্ঞেস করবো", "এখন না বলাই ভালো", "এই মুহূর্তে ভবিষ্যদ্বাণী করা অসম্ভব", "আবার জিজ্ঞাসা করে মনোনিবেশ করুন", "সৌন্দর্যের কথা ভাবুন", "আমার উত্তর হচ্ছে না।", "আমার সোর্স বলেছে না।", "এটা খুব ভালো দেখাচ্ছে না", "এটা সন্দেহজনক"]
pt = ["É inevitável", "definitivamente", "não duvides", "Sem dúvida", "pode confiar nele", "Como posso ver, sim", "É muito provável", "bonito", "sim", "Há sinais de que \"sim\"", "Responda ao todo, tente de novo", "peça novamente mais tarde",
"É melhor não te dizer agora", "imprevisível agora", "concentra-te em perguntar outra vez", "Pense na beleza", "A minha resposta é não", "A minha fonte disse que não.", "Não é muito bom", "é suspeito"]
ind = ["Ini tak terelakkan," "pasti," "jangan ragu", "tidak diragukan lagi," "Anda dapat mengandalkannya", "Seperti yang saya lihat, ya", "Sangat mungkin", "tampan", "ya", "Ada tanda-tanda bahwa \"ya\"", "Balas ke keseluruhan, coba lagi", "tanya lagi nanti", "Lebih baik tidak memberitahu Anda sekarang", "tidak dapat diprediksi sekarang", "fokus pada bertanya lagi", "Pikirkan keindahan", "Jawabanku adalah tidak", "Sumber saya mengatakan \"tidak\"", "tidak terlalu tampan", "sangat mencurigakan"]
de = ["Es ist sicher", "Es ist entschieden so", "Ohne Zweifel", "Ja, definitiv", "Sie können sich darauf verlassen", "Wie ich es sehe, ja", "Höchstwahrscheinlich", "Ausblick gut","Ja","Zeichen zeigen auf Ja","Trübe Antwort erneut versuchen","Später erneut fragen","Jetzt besser nicht sagen","Jetzt nicht vorhersagen","Konzentrieren und noch einmal fragen","Don'Ich zähle nicht darauf","Meine Antwort ist nein","Meine Quellen sagen nein","Ausblick nicht so gut","Sehr zweifelhaft"]
jp = ["確かに", "間違いなくそうだ", "間違いなく", "はい", "間違いなく", "信頼できる", "私が見ているように", "はい", "可能性が高い", "見通しは良い", "はい",  "兆候はイエスを指します ", "返信はかすんでもう一度やり直してください ", "後でもう一度質問してください ", "今は教えないでください ", "今は予測できません ", "集中してもう一度質問してください ", "しない 頼りにしています」", "私の返事はノーです", "私の情報源はノーと言っています", "見通しはあまり良くありません", "非常に疑わしい"]

lang = "en"
sylang = "en"
hplang = "en"
pglang = "en"
anstxt = "Yes"
ansnum = 0
hpss = "paper"
cpss = "paper"
FMT = '%Y-%m-%d %H:%M:%S' 

bot = commands.Bot(command_prefix='mb!')
bot.remove_command('help')

@bot.event
async def on_ready():
  print("Magic 8 Ball is here")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="mb!help en"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Type all argument first!")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Can't find that command. Please check the help menu.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the permission to do that.")

@bot.command()
async def help(ctx, hplang):
    if hplang == "en":
        embedhen=discord.Embed(title="Help menu", color=0x00ff00)
        embedhen.add_field(name="mb!help [language]", value="Show this help menu", inline=False)
        embedhen.add_field(name="mb!ping [language]", value="Show the latency of the bot", inline=False)
        embedhen.add_field(name="mb!m8b [language] [question]", value="Main command of the bot", inline=False)
        embedhen.addfield(name="mb!pss []")
        embedhen.add_field(name="Version", value="M-1.4.1", inline=False)
        embedhen.add_field(name="Language code:", value="en: English zh: Chinese fr: French es: Spanish hi: Hindi ar: Arabic ru: Russian bn: Bengali pt: Portuguese id: Indonesian de: German jp: Japanese", inline=False)
        await ctx.send(embed=embedhen)
    elif hplang == "zh":
        embedhzh=discord.Embed(title="幫助選單", color=0x00ff00)
        embedhzh.add_field(name="mb!help [語言]", value="顯示此幫助功能", inline=False)
        embedhzh.add_field(name="mb!ping [語言]", value="顯示自動程式的延遲", inline=False)
        embedhzh.add_field(name="mb!m8b [語言] [問題]", value="機器人的主命令", inline=False)
        embedhzh.add_field(name="版本", value="M-1.4.1", inline=False)
        embedhzh.add_field(name="語言代碼:", value="en: 英文 zh: 中文 fr: 法語 es: 西班牙文 hi: 印地語 ar: 阿拉伯文 ru: 俄語 bn: 孟加拉語pt: 葡萄牙文 id: 印尼文 de: 德語 jp: 日語", inline=False)
        await ctx.send(embed=embedhzh)
    elif hplang == "fr":
        embedhfr=discord.Embed(title="Menu d’aide", color=0x00ff00)
        embedhfr.add_field(name="mb!help [langue]", value="Ce menu d’aide s’affiche", inline=False)
        embedhfr.add_field(name="mb!ping [langue]", value="Montre le retard de l’automate", inline=False)
        embedhfr.add_field(name="mb!m8b [langue] [question]", value="La commande principale du robot", inline=False)
        embedhfr.add_field(name="Version", value="M-1.4.1", inline=False)
        embedhfr.add_field(name="Langue Code:", value="fr: Anglais zh: Chinois fr: Français es: Espagnol salut: Hindi ar: Arabe ru: Russe bn: Bengali pt: portugais id: Indonésien de: Allemand jp: Japonais", inline=False)
        await ctx.send(embed=embedhfr)
    elif hplang == "es":
        embedhes=discord.Embed(title="Menú de ayuda", color=0x00ff00)
        embedhes.add_field(name="mb!help [idioma]", value="Este menú de ayuda se muestra", inline=False)
        embedhes.add_field(name="mb!ping [idioma]", value="Muestra el retraso del automat", inline=False)
        embedhes.add_field(name="mb!m8b [idioma] [pregunta]", value="El mando principal del robot", inline=False)
        embedhes.add_field(name="Versión", value="M-1.4.1", inline=False)
        embedhes.add_field(name="Versión Código:", value="es: Inglés zh: chino fr: francés es: español hi: Hindi ar: árabe ru: ruso bn: Bengalí pt: Portugués id: indonesio de: Alemán jp: Japonés")
        await ctx.send(embed=embedhes)
    elif hplang == "hi":
        embedhhi=discord.Embed(title="मेनू में मदद करें", color=0x00ff00)
        embedhhi.add_field(name="mb!help [भाषा।]", value="इस मदद सुविधा दिखाएं", inline=False)
        embedhhi.add_field(name="mb!ping [भाषा।]", value="ऑटोमेट की देरी को दर्शाता है", inline=False)
        embedhhi.add_field(name="mb!m8b [भाषा।] [समस्या।]", value="रोबोट की मुख्य कमान", inline=False)
        embedhhi.add_field(name="विवरण।", value="-1.4.1", inline=False)
        embedhhi.add_field(name="भाषा कोड:", value="en: अंग्रेजी zh: चीनी fr: फ्रेंच es: स्पेनिश hi: हिंदी ar: अरबी ru: रूसी bn: बांग्ला pt: इंडोनेशियाई id: पुर्तगाली de: जर्मन jp: जापानी ", inline=False)
        await ctx.send(embed=embedhhi)
    elif hplang == "ar":
        embedhar=discord.Embed(title="قائمة التعليمات", color=0x00ff00)
        embedhar.add_field(name="mb!help [اللغة]", value="إظهار ميزة التعليمات هذه", inline=False)
        embedhar.add_field(name="mb!ping [اللغة]", value="إظهار تأخير التلقائي", inline=False)
        embedhar.add_field(name="mb!m8b [اللغة] [السؤال]", value="الأمر الرئيسي للروبوت", inline=False)
        embedhar.add_field(name="الإصدار.", value="M-1.4.1", inline=False)
        embedhar.add_field(name="رمز اللغة:", value="en: الإنجليزية zh: الصينية fr:  الإسبانية es: الإسبانية hi: لا ar: العربية ru: الروسية bn: البنغالية pt: البرتغالية id: الإندونيسية de: ألمانية jp: اليابانية", inline=False)
        await ctx.send(embed=embedhar)
    elif hplang == "ru":
        embedhru=discord.Embed(title="Меню справки", color=0x00ff00)
        embedhru.add_field(name="mb!help [Язык]", value="Показать это меню справки", inline=False)
        embedhru.add_field(name="mb!ping [Язык]", value="Показать задержку бота", inline=False)
        embedhru.add_field(name="mb!m8b [Язык] [Вопрос]", value="Главное командование ботом", inline=False)
        embedhru.add_field(name="Версия", value="M-1.4.1", inline=False)
        embedhru.add_field(name="Языковой код:", value="en: Английский zh: Китайский fr: Французский es: Испанский hi: Хинди аr: Арабский ru: Русский bn: бенгальский pt: португальский id: индонезийский de: Немецкий jp: Японский", inline=False)
        await ctx.send(embed=embedhru)
    elif hplang == "bn":
        embedhbn=discord.Embed(title="সহায়তা মেনু", color=0x00ff00)
        embedhbn.add_field(name="mb!help [ভাষা]", value="এই সহায়তা মেনু টি দেখান", inline=False)
        embedhbn.add_field(name="mb!ping [ভাষা]", value="রোবটের ল্যাটেন্সি দেখান", inline=False)
        embedhbn.add_field(name="mb!m8b [ভাষা] [প্রশ্ন]", value="রোবটের প্রধান কমান্ড", inline=False)
        embedhbn.add_field(name="সংস্করণ", value="M-1.4.1", inline=False)
        embedhbn.add_field(name="ভাষা কোড", value="en: ইংরাজি zh: চিনা fr: ফরাসী es: স্প্যানিশ hi: না ar: আরবি ru: রুশ bn: বাংলা pt: পর্তুগিজ id: ইন্দোনেশীয় de: জার্মান jp: জাপানি", inline=False)
        await ctx.send(embed=embedhbn)
    elif hplang == "pt":
        embedhpt=discord.Embed(title="Menu de ajuda", color=0x00ff00)
        embedhpt.add_field(name="mb!help [idioma]", value="Mostre este menu de ajuda", inline=False)
        embedhpt.add_field(name="mb!ping [idioma]", value="Mostre a latência do bot", inline=False)
        embedhpt.add_field(name="mb!m8b [idioma] [pergunta]", value="Comando principal do bot", inline=False)
        embedhpt.add_field(name="Versão", value="M-1.4.1", inline=False)
        embedhpt.add_field(name="código de linguagem:", value="en: Inglês zh: Chinês fr: Francês es: Espanhol hi: Hindi ar: Árabe ru: Russo bn: Bengali pt: Português id: Indonésio de: Alemão jp: japonês", inline=False)
        await ctx.send(embed=embedhpt)
    elif hplang == "id":
        embedhid=discord.Embed(title="Menu Bantuan", color=0x00ff00)
        embedhid.add_field(name="mb!help [bahasa]", value="Mostre este menu de ajuda", inline=False)
        embedhid.add_field(name="mb!ping [bahasa]", value="Mostre a latência do bot", inline=False)
        embedhid.add_field(name="mb!m8b [bahasa] [pertanyaan]", value="Comando principal do bot", inline=False)
        embedhid.add_field(name="Versi", value="M-1.4.1", inline=False)
        embedhid.add_field(name="kode bahasa:", value="en: Inggris zh: Cina fr: Prancis es: Spanyol hi: Hindi ar: Arab ru: Rusia bn: Bengali pt: Portugis id: Indonesia de: Jerman jp: Jepang", inline=False)
        await ctx.send(embed=embedhid)
    elif hplang == "de":
        embedhde=discord.Embed(title="Hilfemenü", color=0x00ff00)
        embedhde.add_field(name="mb!help [Sprache]", value="Dieses Hilfemenü anzeigen", inline=False)
        embedhde.add_field(name="mb!ping [Sprache]", value="Zeigen Sie die Latenz des Bots an", inline=False)
        embedhde.add_field(name="mb!m8b [Sprache] [Frage]", value="Hauptbefehl des Bots", inline=False)
        embedhde.add_field(name="Ausführung", value="M-1.4.1", inline=False)
        embedhde.add_field(name="Sprachcode:", value="en: Englisch zh: Chinesisch fr: Französisch es: Spanisch hi: Hindi ar: Arabisch ru: Russisch bn: Bengali pt: Portugiesisch id: Indonesisch de: Deutsche jp: Japanisch", inline=False)
        await ctx.send(embed=embedhde)
    elif hplang == "jp":
        embedhjp=discord.Embed(title="ヘルプメニュー ", color=0x00ff00)
        embedhjp.add_field(name="mb!help [言語]", value="このヘルプメニューを表示する", inline=False)
        embedhjp.add_field(name="mb!ping [言語]", value="ボットのレイテンシーを表示する", inline=False)
        embedhjp.add_field(name="mb!m8b [言語] [質問]", value="ボットのメインコマンド", inline=False)
        embedhjp.add_field(name="バージョン", value="M-1.5.2", inline=False)
        embedhjp.add_field(name="言語コード:", value="en:英語 zh:中国語 fr:フランス語 es:スペイン語 hi:ヒンディー語 ar:アラビア語 ru:ロシア語 bn:ベンガル語 pt:ポルトガル語 id:インドネシア語 de:ドイツ語 jp:日本語", inline=False)
        await ctx.send(embed=embedhjp)

@bot.command()
async def ping(ctx, pglang):
    if pglang == "en":
        embedpen = discord.Embed(title="", description="", color=0x00ff00)
        embedpen.add_field(name="Current latency", value=str(bot.latency*1000) + " miliseconds", inline=False)
        await ctx.send(embed=embedpen)
    elif pglang == "zh":
        embedpzh = discord.Embed(title="", description="", color=0x00ff00)
        embedpzh.add_field(name="當前延遲", value=str(bot.latency*1000) + " 毫秒", inline=False)
        await ctx.send(embed=embedpzh)
    elif pglang == "fr":
        embedpfr = discord.Embed(title="", description="", color=0x00ff00)
        embedpfr.add_field(name="Latence actuelle", value=str(bot.latency*1000) + " milliseconde", inline=False)
        await ctx.send(embed=embedpfr)
    elif pglang == "es":
        embedpes = discord.Embed(title="", description="", color=0x00ff00)
        embedpes.add_field(name="Latencia actual", value=str(bot.latency*1000) + " milisegundo", inline=False)
        await ctx.send(embed=embedpes)
    elif pglang == "hi":
        embedphi = discord.Embed(title="", description="", color=0x00ff00)
        embedphi.add_field(name="वर्तमान देरी", value=str(bot.latency*1000) + " मिलीसेकंड।", inline=False)
        await ctx.send(embed=embedphi)
    elif pglang == "ar":
        embedpar = discord.Embed(title="", description="", color=0x00ff00)
        embedpar.add_field(name="زمن الوصول الحالي",value=str(bot.latency*1000) + " ميلي ثانيه",inline=False)
        await ctx.send(embed=embedpar)
    elif pglang == "ru":
        embedpru = discord.Embed(title="", description="", color=0x00ff00)
        embedpru.add_field(name="Текущая задержка", value=str(bot.latency*1000) + " Миллисекунд",inline=False)
        await ctx.send(embed=embedpru)
    elif pglang == "bn":
        embedpbn = discord.Embed(title="", description="", color=0x00ff00)
        embedpbn.add_field(name="বর্তমান ল্যাটেন্সি", value=str(bot.latency*1000) + " মিলিসেকেন্ড",inline=False)
        await ctx.send(embed=embedpbn)
    elif pglang == "pt":
        embedppt = discord.Embed(title="", description="", color=0x00ff00)
        embedppt.add_field(name="Latência atual", value=str(bot.latency*1000) + " milissegundos",inline=False)
        await ctx.send(embed=embedppt)
    elif pglang == "id":
        embedppt = discord.Embed(title="", description="", color=0x00ff00)
        embedppt.add_field(name="Latensi saat ini", value=str(bot.latency*1000) + " milidetik",inline=False)
        await ctx.send(embed=embedppt)
    elif pglang == "de":
        embedpde = discord.Embed(title="", description="", color=0x00ff00)
        embedpde.add_field(name="Aktuelle Latenz", value=str(bot.latency*1000) + "millisekunde",inline=False)
        await ctx.send(embed=embedpde)
    elif pglang == "jp":
        embedpjp = discord.Embed(title="", description="", color=0x00ff00)
        embedpjp.add_field(name="現在の待ち時間 ", value=str(bot.latency*1000) + " ミリ秒 ", inline=False)
        await ctx.send(embed=embedpjp)

@bot.command()
async def m8b(ctx, lang):
    ansnum = random.randint(0,19)
    if lang == "en":
        anstxt = en[ansnum]
        embeden=discord.Embed(title="", color=0x38e907)
        embeden.add_field(name=anstxt, value="\u200b", inline=True)
        await ctx.send(embed=embeden)
    elif lang == "zh":
        ans = random.randint(0,19)
        anstxt = zh[ans]
        embedzh=discord.Embed(title="", color=0x38e907)
        embedzh.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedzh)
    elif lang == "fr":
        ans = random.randint(0,19)
        anstxt = fr[ans]
        embedfr=discord.Embed(title="", color=0x38e907)
        embedfr.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedfr)
    elif lang == "es":
        ans = random.randint(0,19)
        anstxt = es[ans]
        embedes=discord.Embed(title="", color=0x38e907)
        embedes.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedes)
    elif lang == "hi":
        ans = random.randint(0, 19)
        anstxt = hi[ans]
        embedhi=discord.Embed(title="", color=0x38e907)
        embedhi.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedhi)
    elif lang == "ar":
        ans = random.randint(0, 19)
        anstxt = ar[ans]
        embedar=discord.Embed(title="", color=0x38e907)
        embedar.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedar)
    elif lang == "ru":
        ans = random.randint(0, 19)
        anstxt = ru[ans]
        embedru=discord.Embed(title="", color=0x38e907)
        embedru.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedru)
    elif lang == "bn":
        ans = random.randint(0, 19)
        anstxt = bn[ans]
        embedbn=discord.Embed(title="", color=0x38e907)
        embedbn.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedbn)
    elif lang == "pt":
        ans = random.randint(0, 19)
        anstxt = pt[ans]
        embedpt=discord.Embed(title="", color=0x38e907)
        embedpt.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedpt)
    elif lang == "id":
        ans = random.randint(0, 19)
        anstxt = ind[ans]
        embedid=discord.Embed(title="", color=0x38e907)
        embedid.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedid)
    elif lang == "de":
        ans = random.randint(0,19)
        anstxt = de[ans]
        embedde=discord.Embed(title="", color=0x38e907)
        embedde.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedde)
    elif lang == "jp":
        ans = random.randint(0,19)
        anstxt = jp[ans]
        embedjp=discord.Embed(title="", color=0x38e907)
        embedjp.add_field(name=anstxt, value="\u200b", inline=False)
        await ctx.send(embed=embedjp)

keep_alive.keep_alive()
bot.run('')


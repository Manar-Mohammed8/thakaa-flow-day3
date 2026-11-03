message = input("Message: ").strip()

# لو الرسالة ما تبدأ بـ ZT: أطبع وأوقف
if not message.startswith("ZT:"):
    print("Not a message from planet Zeta")
else:
    # أحذف ZT: من البداية وأشيل المسافات من الأطراف
    text = message[3:].strip()

    # فك التشفير: 4=a, 3=e, 0=o, 1=i
    decoded = text.replace("4", "a").replace("3", "e").replace("0", "o").replace("1", "i")
    decoded_upper = decoded.upper()

    # عدد الحروف بدون مسافات
    letters = len(decoded.replace(" ", ""))

    # التصنيف
    if "help" in decoded.lower():
        msg_type = "DISTRESS"
    elif "hello" in decoded.lower():
        msg_type = "GREETING"
    elif "?" in decoded:
        msg_type = "QUESTION"
    else:
        msg_type = "UNKNOWN"

    # الاستعجال حسب عدد علامات !
    marks = decoded.count("!")
    if marks >= 3:
        urgency = "HIGH"
    elif marks >= 1:
        urgency = "MEDIUM"
    else:
        urgency = "LOW"

    # الرد مشفر بالعكس: a=4, e=3, o=0, i=1
    reply = "we come in peace"
    encoded_reply = reply.replace("a", "4").replace("e", "3").replace("o", "0").replace("i", "1")

    print(f"Message: {message}")
    print(f"Message: {decoded_upper}")
    print(f"Letters (no spaces): {letters}")
    print(f"Type: {msg_type}")
    print(f"Urgency: {urgency}")
    print(f"Encoded reply: EA: {encoded_reply}")

    # سؤال التفكير:
    # لو فحصت hello قبل help، الرسالة الأولى (فيها الكلمتين) تتصنف GREETING
    # لأن أول شرط صحيح ينفذ وبايثون ما يكمل الباقي، فتضيع كلمة help.
    # فحصت help أول عشان الرسائل الضرورية تنكشف قبل غيرها.
    # في نظام استقبال بلاغات حقيقي هذا مهم، لأن بلاغ طارئ ممكن يتعامل معه
    # كأنه تحية عادية ويتأخر الرد عليه.

    # التجارب:
    # 1) ZT: h3ll0 34rth, w3 n33d h3lp!!!  -> DISTRESS, HIGH
    # 2) ZT: wh3r3 1s y0ur pl4n3t?         -> QUESTION, LOW
    # 3) ZT: wh3r3 4r3 y0u fr0m?!          -> QUESTION, MEDIUM
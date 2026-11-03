name = input("Name: ")
email = input("Email: ")
phone = input("Phone: ")

# أشيل المسافات وأرتب الاسم
clean_name = name.strip().title()

# أشيل المسافات وأخلي الحروف سمول
clean_email = email.strip().lower()

# أتأكد فيه @ و . وما يبدأ بـ @
email_ok = "@" in clean_email and "." in clean_email and not clean_email.startswith("@")

# أشيل المسافات اللي بالداخل
clean_phone = phone.replace(" ", "")

# أتأكد أرقام فقط، يبدأ بـ 05، وطوله 10
phone_ok = clean_phone.isdigit() and clean_phone.startswith("05") and len(clean_phone) == 10

# أي حقل غلط أطبع له رسالة خطأ
if clean_name == "":
    print("Invalid name")
if not email_ok:
    print("Invalid email")
if not phone_ok:
    print("Invalid phone")

# إذا كل شي صح أطبع السجل النظيف وأقترح اسم مستخدم
if clean_name != "" and email_ok and phone_ok:
    print(f"{clean_name} | {clean_email} | {clean_phone} OK")

    # أدور على أول مسافة بـ find عشان ألقى أول كلمة (بدون split)
    space = clean_name.find(" ")

    # لو ما فيه مسافة (-1) يعني الاسم كلمة وحدة وآخذه كله
    if space == -1:
        first = clean_name
    else:
        first = clean_name[:space]

    # أول كلمة صغيرة + نقطة + آخر رقمين من الجوال
    username = first.lower() + "." + clean_phone[-2:]
    print("Suggested username:", username)

    # التجارب:
    # 1) مثال الورقة -> Mohamed  Ali | mohamed@gmail.com | 0551234567 OK
    #                   Suggested username: mohamed.67
    # 2) بياناتي -> Manar  Salam | manarsalam.888@gmail.com | 0531130732 OK
    #               Suggested username: manar.32
    # 3) حالة خاطئة (sara / sara.gmail.com / 0612345) -> Invalid email
